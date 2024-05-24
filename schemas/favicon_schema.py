# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from models.favicon import Favicon

class FaviconSchema(Schema):
    url = fields.String(allow_none=True)
    blob_uri = fields.String(allow_none=True)
    name = fields.String(allow_none=True)
    phash = fields.String(allow_none=True)
    width = fields.Integer(allow_none=True)
    height = fields.Integer(allow_none=True)
    mimetype = fields.String(allow_none=True)
    format = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Favicon(**data)


favicon_schema = FaviconSchema()
