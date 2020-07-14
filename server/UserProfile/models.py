from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, active=True, )
    " create user manager "

class Profile(SafeDeleteModel, AbstractUser):
    pass

