from graphene import relay, ObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Profile, DoctorProfile
from .profileSerializers import ProfileSerializer, DoctorSerializer




class ProfileNode(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields = ['id', 'email', 'first_name', 'last_name']
        interfaces = (relay.Node,)


class ProfileMutation(SerializerMutation):
    class Meta:
        serializer_class = ProfileSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class DoctorNode(DjangoObjectType):
    class Meta:
        model = DoctorProfile
        fields = '__all__'
        interfaces = (relay.Node,)


class DoctorMutation(SerializerMutation):
    class Meta:
        serializer_class = DoctorSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


#<------Query--------->
class Query(ObjectType):
    profile = relay.Node.Field(ProfileNode)
    all_profile = DjangoFilterConnectionField(ProfileNode)

    doctorProfile = relay.Node.Field(DoctorNode)
    all_doctorProfile = DjangoFilterConnectionField

    def resolve_all_profile(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_all_doctorProfile(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Profile.DoctorProfile.objects.all()

#<---Mutation---->
class Mutation(ObjectType):
    profile_creator = ProfileMutation.Field()
    #doctor_creator = DoctorMutation.Field()