# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.fast_check import FastCheck

class FastCheckSchema(Schema):
    url = fields.String(allow_none=True)
    malicious_score = fields.Float(allow_none=True)
    status = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return FastCheck(**data)

fast_check_schema = FastCheckSchema()
