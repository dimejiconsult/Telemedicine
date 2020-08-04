import graphene
from UserProfile import schema as profileSchema


class Query(profileSchema.Query, graphene.ObjectType):
    pass

class Mutation(profileSchema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)