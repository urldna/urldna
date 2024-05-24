class Cookie(object):

    def __init__(self,
                domain=None,
                expiry=None,
                secure=None,
                http_only=None,
                name=None,
                path=None,
                value=None) -> None:
        # Fields
        self.domain = domain
        self.expiry = expiry
        self.secure = secure
        self.http_only = http_only
        self.name = name
        self.path = path
        self.value = value

    def __repr__(self):
        return "<Cookie name: %r, domain: %r, value: %r>" % (
            self.name, self.domain, self.value[:50])
