# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.scan_feedback import ScanFeedback

class ScanFeedbackSchema(Schema):
    malicious_count = fields.Integer(allow_none=True)
    safe_count = fields.Integer(allow_none=True)
    user_feedback = fields.String(allow_none=True)
    
    @post_load
    def create(self, data, **kwargs):
        return ScanFeedback(**data)

scan_feedback_schema = ScanFeedbackSchema()
