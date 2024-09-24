class FastCheck(object):

    def __init__(self, 
                url=None, 
                malicious_score=None, 
                status=None):
        """
        Init fast check
        :param url: Submitted url
        :param malicious_score: Malicious score [0-1]
        :param status: Status ["SAFE","MALICIOUS","UNRATED"]
        """
        self.url = url
        self.malicious_score = malicious_score
        self.status = status

    def __repr__(self):
        return "<FastCheck url: %r malicious_score: %r status: %r>" % (self.url, self.malicious_score, self.status)
