# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.scan_whois import ScanWhois

class ScanWhoisSchema(Schema):
    domain_name = fields.String(allow_none=True)
    registrar = fields.String(allow_none=True)
    creation_date = fields.DateTime(allow_none=True)
    expiration_date = fields.DateTime(allow_none=True)
    updated_date = fields.DateTime(allow_none=True)
    name = fields.String(allow_none=True)
    org = fields.String(allow_none=True)
    address = fields.String(allow_none=True)
    registrant_postal_code = fields.String(allow_none=True)
    country = fields.String(allow_none=True)
    state = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return ScanWhois(**data)


scan_whois_schema = ScanWhoisSchema()
