# Marshmallow
from marshmallow import Schema, fields, post_load

# Model
from models.user_agent import UserAgent


class UserAgentSchema(Schema):
    device =  fields.String(allow_none=True)
    browser = fields.String(allow_none=True)
    user_agent = fields.String(allow_none=True)
    share = fields.Float(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return UserAgent(**data)

user_agent_schema = UserAgentSchema()
user_agents_schema = UserAgentSchema(many=True)
