from django.db import models
from django.conf import settings
from oauth2_provider import models as oauth2_models


class Policy(models.Model):
    service_id = models.ForeignKey(oauth2_models.Application, related_name='Policy')
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name


class RolePolicy(models.Model):
    role_id = models.ForeignKey(Role, related_name='RolePolicy')
    policy_id = models.ForeignKey(Policy, related_name='PolicyRole')

    def __str__(self):
        return self.role_id.role_name + " " + self.policy_id.label