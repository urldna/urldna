# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from models.screenshot import Screenshot

class ScreenshotSchema(Schema):
    blob_uri = fields.String(allow_none=True)
    name = fields.String(allow_none=True)
    phash = fields.String(allow_none=True)
    width = fields.Integer(allow_none=True)
    height = fields.Integer(allow_none=True)
    mimetype = fields.String(allow_none=True)
    format = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Screenshot(**data)

screenshot_schema = ScreenshotSchema()
