# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.redirect_chain import RedirectChain

class RedirectChainSchema(Schema):
    redirect_url = fields.String(allow_none=True)
    status = fields.String(allow_none=True)
    elapsed_time = fields.Float(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return RedirectChain(**data)


redirect_chains_schema = RedirectChainSchema(many=True)
