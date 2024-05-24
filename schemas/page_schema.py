# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from models.page import Page

class PageSchema(Schema):
    text = fields.String(allow_none=True)
    title = fields.String(allow_none=True)
    meta_tags = fields.Dict(keys=fields.String, values=fields.String, allow_none=True)
    headers = fields.Dict(keys=fields.String, values=fields.String, allow_none=True)
    ssdeep = fields.String(allow_none=True)
    outgoing_links = fields.List(fields.String, allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Page(**data)

page_schema = PageSchema()
