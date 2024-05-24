# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.ip_address import IpAddress

class IpAddressSchema(Schema):
    ip = fields.String(allow_none=True)
    asn = fields.String(allow_none=True)
    city = fields.String(allow_none=True)
    country = fields.String(allow_none=True)
    country_code = fields.String(allow_none=True)
    isp = fields.String(allow_none=True)
    latitude = fields.Float(allow_none=True)
    longitude = fields.Float(allow_none=True)
    org = fields.String(allow_none=True)
    region = fields.String(allow_none=True)
    timezone_gmt = fields.String(allow_none=True)
    type = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return IpAddress(**data)


ip_address_schema = IpAddressSchema()
