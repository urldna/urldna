class ScanFeedback(object):

    def __init__(self,
                phishing_count=None,
                safe_count=None,
                user_feedback=None) -> None:
        # Fields
        self.phishing_count = phishing_count
        self.safe_count = safe_count
        self.user_feedback = user_feedback

    def __repr__(self):
        return "<ScanFeedback phishing_count: %r, safe_count: %r, user_feedback: %r>" % (self.phishing_count, self.safe_count, self.user_feedback)
