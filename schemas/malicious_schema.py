# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from models.malicious import Malicious

class MaliciousSchema(Schema):
    malicious = fields.Boolean(allow_none=True)
    threat = fields.String(allow_none=True)
    
    @post_load
    def create(self, data, **kwargs):
        return Malicious(**data)


malicious_schema = MaliciousSchema()
