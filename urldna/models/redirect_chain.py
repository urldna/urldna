class RedirectChain(object):

    def __init__(self,
                redirect_url=None,
                status=None,
                elapsed_time=None) -> None:
        # Fields
        self.redirect_url = redirect_url
        self.status = status
        self.elapsed_time = elapsed_time

    def __repr__(self):
        return "<RedirectChain redirect_url: %r, status: %r, elapsed_time: %r>" % (
            self.redirect_url[:50], self.status, self.elapsed_time)
