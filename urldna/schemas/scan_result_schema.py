# Marshmallow
from marshmallow import Schema, fields, post_load

# Schemas
from urldna.schemas.scan_schema import scan_schema
from urldna.schemas.page_schema import page_schema
from urldna.schemas.cookie_schema import cookies_schema
from urldna.schemas.favicon_schema import favicon_schema
from urldna.schemas.malicious_schema import malicious_schema
from urldna.schemas.ip_address_schema import ip_address_schema
from urldna.schemas.screenshot_schema import screenshot_schema
from urldna.schemas.technology_schema import technologies_schema
from urldna.schemas.certificate_schema import certificate_schema
from urldna.schemas.scan_feedback_schema import scan_feedback_schema
from urldna.schemas.console_message_schema import console_messages_schema
from urldna.schemas.http_transaction_schema import http_transactions_schema

# Models
from urldna.models.scan_result import ScanResult


class ScanResultSchema(Schema):
    scan = fields.Nested(scan_schema, allow_none=True)
    page = fields.Nested(page_schema, allow_none=True)
    dom = fields.String(allow_none=True)
    cookies = fields.Nested(cookies_schema, allow_none=True)
    favicon = fields.Nested(favicon_schema, allow_none=True)
    malicious = fields.Nested(malicious_schema, allow_none=True)
    ip_address = fields.Nested(ip_address_schema, allow_none=True)
    screenshot = fields.Nested(screenshot_schema, allow_none=True)
    certificate = fields.Nested(certificate_schema, allow_none=True)
    technologies = fields.Nested(technologies_schema, allow_none=True)
    scan_feedback = fields.Nested(scan_feedback_schema, allow_none=True)
    console_messages = fields.Nested(console_messages_schema, allow_none=True)
    http_transactions = fields.Nested(http_transactions_schema, allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return ScanResult(**data)


scan_result_schema = ScanResultSchema()
scan_results_schema = ScanResultSchema(many=True)
