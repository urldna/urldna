class Scan(object):

    def __init__(self,
                id=None,
                submitted_url=None,
                scanned_from=None,
                target_url=None,
                protocol=None,
                domain=None,
                nsfw=None,
                device=None,
                user_agent=None,
                origin=None,
                width=None,
                height=None,
                waiting_time=None,
                submitted_date=None,
                status=None,
                private_scan=None,
                submitter_tags=None):

        # Fields
        self.id = id
        self.submitted_url = submitted_url
        self.target_url = target_url
        self.protocol = protocol
        self.domain = domain
        self.nsfw = nsfw
        self.device = device
        self.user_agent = user_agent
        self.origin = origin
        self.width = width
        self.height = height
        self.waiting_time = waiting_time
        self.submitted_date = submitted_date
        self.status = status
        self.private_scan = private_scan
        self.scanned_from = scanned_from
        self.submitter_tags = submitter_tags

    def __repr__(self):
        return "<Scan id: %r, submitted_date: %r>" % (self.id, self.submitted_date.isoformat())
