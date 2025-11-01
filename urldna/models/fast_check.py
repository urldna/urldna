class FastCheck(object):

    def __init__(self, 
                url=None, 
                malicious_score=None, 
                status=None,
                scan_id=None):
        """
        Init fast check
        :param url: Submitted url
        :param malicious_score: Malicious score [0-1]
        :param status: Status ["SAFE","MALICIOUS","UNRATED"]
        :param scan_id: matched Scan ID
        """
        self.url = url
        self.malicious_score = malicious_score
        self.status = status
        self.scan_id = scan_id

    def __repr__(self):
        return "<FastCheck url: %r malicious_score: %r status: %r>" % (self.url, self.malicious_score, self.status)
