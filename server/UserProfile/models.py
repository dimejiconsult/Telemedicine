from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteManager


Gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, staff=False, 
                    active=True, admin=False, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """ create superuser"""
        user = self.create_user(email, password)
        user.active = True
        user.superuser = True
        user.staff = True
        user.admin =True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)    
    

class Profile(SafeDeleteModel, AbstractBaseUser, PermissionsMixin):
    """ user model """
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    username = models.CharField(max_length=100,blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
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
        return self.email
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

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class DoctorProfile(Profile, PermissionsMixin):
    checked = models.BooleanField(default=False)
    Year_of_Graduation = models.DateField()
    Sch_of_Graduation  = models.CharField(max_length=150)
    Hospital_of_housemanship = models.CharField(max_length=255)
    Folio_Number = models.CharField(max_length=50)
    Full_License_document = models.ImageField(upload_to='License_document/%Y/%m/%d/')
    Evidence_of_Annual_License_Reg = models.ImageField(upload_to='Evidence_of_Annual_License_Reg/%Y/%m/%d/')
    CV = models.ImageField(upload_to='CV/%Y/%m/%d/')
    Specialization = models.CharField(max_length=255)
    gender = models.CharField(max_length=7, choices=Gender,blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

class PatientProfile(Profile, PermissionsMixin):
    # active = models.BooleanField(default=True)
    pass