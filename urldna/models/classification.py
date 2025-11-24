class Classification(object):

    def __init__(self,
                verdict=None,
                threat=None) -> None:
        
        # Fields
        self.verdict = verdict
        self.threat = threat

    def __repr__(self):
        return "<Classification verdict: %r >" % self.verdict
