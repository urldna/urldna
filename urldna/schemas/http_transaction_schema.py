# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.http_transaction import HttpTransaction

class HttpTransactionSchema(Schema):
    url = fields.String(allow_none=True)
    ip = fields.String(allow_none=True)
    method = fields.String(allow_none=True)
    mimetypes = fields.String(allow_none=True)
    content_type = fields.String(allow_none=True)
    status_code = fields.Int(allow_none=True)
    size = fields.Float(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return HttpTransaction(**data)


http_transactions_schema = HttpTransactionSchema(many=True)
