# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.technology import Technology


class TechnologySchema(Schema):
    name = fields.String(allow_none=True)
    category = fields.String(allow_none=True)
    version = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Technology(**data)


technologies_schema = TechnologySchema(many=True)
