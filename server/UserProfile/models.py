from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,  PermissionsMixin
from django.utils.translation import ugettext_lazy as _


Gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, active=False, staff=False, admin=False, **extra_fields):
        """ usermanager for creating users """
        if not email:
            raise  ValueError('please provide a email')
        email = self.normalize_email(email)
        user =self.model(email=email, **extra_fields)
        user.active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        """ create super user """
        user =self.create_user(email,password)
        user.admin = True
        user.staff = True
        user.active = True
        user.superuser =True
        user.save(using=self._db)
        return user

    def create_DoctorProfile(self,email,password,**extra_fields):
        """ create super user """
        user =self.create_user(email,password,**extra_fields)
        user.is_active = False
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class Profile(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
 
 
    def get_full_name(self):
        return (self.first_name+' '+self.last_name)
 
    def get_short_name(self):
        return self.first_name
 
    def natural_key(self):
        return (self.first_name, self.last_name)
 
    def __str__(self):
        return self.first_name+' '+self.last_name
        
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.staff

    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

   



class DoctorProfile(Profile, PermissionsMixin):
    gender = models.CharField(max_length=7, choices=Gender)
    date_of_birth = models.DateField()
    Year_of_Graduation = models.DateField()
    Sch_of_Graduation = models.CharField(max_length=255) 
    Hospital_of_housemanship = models.CharField(max_length=255)
    Folio_Number = models.CharField(max_length=50)
    Full_License = models.FileField(upload_to='../media/License_document/%Y/%m/%d/')
    Evidence_of_License_Reg = models.FileField(upload_to='../media/Evidence_of_Annual_License_Reg/%Y/%m/%d/')
    CV = models.FileField(upload_to='../media/CV/%Y/%m/%d/')
    Specialization = models.CharField(max_length=50)

    objects = UserManager()
 
    def __str__(self):
        return self.first_name+' '+self.last_name
 