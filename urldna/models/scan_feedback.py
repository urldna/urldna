from enum import Enum

class ScanFeedbackEnum(Enum):
    MALICIOUS = "MALICIOUS"
    SAFE = "SAFE"

class ScanFeedback(object):

    def __init__(self,
                malicious_count=None,
                safe_count=None,
                user_feedback=None) -> None:
        # Fields
        self.malicious_count = malicious_count
        self.safe_count = safe_count
        self.user_feedback = user_feedback

    def __repr__(self):
        return "<ScanFeedback malicious_count: %r, safe_count: %r, user_feedback: %r>" % (self.malicious_count, self.safe_count, self.user_feedback)
