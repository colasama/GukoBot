from datetime import datetime

from tortoise import fields
from tortoise.models import Model


class Nickname(Model):
    uid = fields.IntField()
    group_id = fields.IntField()
    up_nickname = fields.TextField(null=True)
    last_update = fields.DatetimeField(default=datetime.fromordinal(1))