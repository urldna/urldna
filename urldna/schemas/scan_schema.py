# Marshmallow
from marshmallow import Schema, fields, post_load

# Models
from urldna.models.scan import Scan

class ScanSchema(Schema):
    id = fields.String(allow_none=True)
    submitted_url = fields.String(allow_none=True)
    target_url = fields.String(allow_none=True)
    protocol = fields.String(allow_none=True)
    device = fields.String(allow_none=True)
    user_agent = fields.String(allow_none=True)
    nsfw = fields.Boolean(allow_none=True)
    scanned_from = fields.String(allow_none=True)
    origin = fields.String(allow_none=True)
    width = fields.Integer(allow_none=True)
    height = fields.Integer(allow_none=True)
    domain = fields.String(allow_none=True)
    private_scan = fields.Boolean(allow_none=True)
    status = fields.String(allow_none=True)
    submitted_date = fields.DateTime(allow_none=True)
    waiting_time = fields.Integer(allow_none=True)
    submitter_tags = fields.List(fields.String, required=False, allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return Scan(**data)

scan_schema = ScanSchema()
scans_schema = ScanSchema(many=True)
