# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.console_message import ConsoleMessage

class ConsoleMessageSchema(Schema):
    text = fields.String(allow_none=True)
    type = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return ConsoleMessage(**data)

console_messages_schema = ConsoleMessageSchema(many=True)
