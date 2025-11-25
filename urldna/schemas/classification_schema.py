# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.classification import Classification

class ClassificationSchema(Schema):
    verdict = fields.String(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Classification(**data)


classification_schema = ClassificationSchema()
