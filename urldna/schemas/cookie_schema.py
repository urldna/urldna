# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.cookie import Cookie

class CookieSchema(Schema):
    domain = fields.String(allow_none=True)
    expiry = fields.DateTime(allow_none=True)
    http_only = fields.Boolean(allow_none=True)
    name = fields.String(allow_none=True)
    path = fields.String(allow_none=True)
    secure = fields.Boolean(allow_none=True)
    value = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Cookie(**data)


cookies_schema = CookieSchema(many=True)
