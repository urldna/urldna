# Marshmallow
from marshmallow import Schema, fields, post_load

# Model
from urldna.models.viewport import Viewport

class ViewportSchema(Schema):
    device =  fields.String(allow_none=True)
    width = fields.Integer(allow_none=True)
    height = fields.Integer(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Viewport(**data)


viewport_schema = ViewportSchema()
viewports_schema = ViewportSchema(many=True)
