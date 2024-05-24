# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from models.certificate import Certificate

class CertificateSchema(Schema):
    authority_info_access = fields.String(allow_none=True)
    authority_key_identifier = fields.String(allow_none=True)
    basic_constraints = fields.String(allow_none=True)
    certificate_policies = fields.String(allow_none=True)
    ct_precert_scts = fields.String(allow_none=True)
    extended_key_usage = fields.String(allow_none=True)
    issuer = fields.String(allow_none=True)
    key_usage = fields.String(allow_none=True)
    not_after = fields.DateTime(allow_none=True)
    not_before = fields.DateTime(allow_none=True)
    serial_number = fields.String(allow_none=True)
    subject = fields.String(allow_none=True)
    subject_key_identifier = fields.String(allow_none=True)
    version = fields.Integer(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Certificate(**data)


certificate_schema = CertificateSchema()
