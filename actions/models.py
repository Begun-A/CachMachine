from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, card_number, password=None, name=None):
        if not card_number:
            raise ValueError('Users must have an card_number')

        user = self.model(
            card_number=card_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, card_number, password=None):
        user = self.create_user(
            card_number,
            password=password
        )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """ Changed User model, which describe card """
    card_number = models.IntegerField(unique=True, null=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    objects = UserManager()

    USERNAME_FIELD = 'card_number'

    def get_card_number(self):
        return self.ca1rd_number

    def get_password(self):
        return self.password

    def get_full_name(self):
        return str(self.card_number)

    def get_short_name(self):
        return str(self.card_number)

    def __unicode__(self):
        return str(self.card_number)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'auth_user'


class Operation(models.Model):
    """Model describe card operations """
    OPERATION_TYPE = (
        ('0', 'balance'),
        ('1', 'withdrawal')
    )
    card = models.ForeignKey('User', null=False, to_field='card_number',
                             related_name='operations')
    date = models.DateTimeField(null=False)
    amount = models.IntegerField(null=True)
    operation = models.CharField(max_length=1, choices=OPERATION_TYPE)
