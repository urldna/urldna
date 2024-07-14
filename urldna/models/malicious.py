class Malicious(object):

    def __init__(self,
                malicious=None,
                threat=None) -> None:
        
        # Fields
        self.malicious = malicious
        self.threat = threat

    def __repr__(self):
        return "<Malicious threat: %r, malicious: %r>" % (
            self.threat, self.malicious)
