class Classification(object):

    def __init__(self, verdict=None) -> None:
        
        # Fields
        self.verdict = verdict

    def __repr__(self):
        return "<Classification verdict: %r >" % self.verdict
