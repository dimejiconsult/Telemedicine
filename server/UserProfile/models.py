from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteManager


class UserManager(BaseUserManager):
    pass


class Profile(SafeDeleteModel, AbstractBaseUser):
    pass