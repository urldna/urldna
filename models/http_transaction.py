class HttpTransaction(object):

    def __init__(self,
                url=None,
                ip=None,
                method=None,
                mimetypes=None,
                content_type=None,
                status_code=None,
                size=None,
                phash=None) -> None:
        # Fields
        self.url = url
        self.ip = ip
        self.method = method 
        self.mimetypes = mimetypes
        self.content_type = content_type
        self.status_code = status_code
        self.size = size
        self.phash = phash

    def __repr__(self):
        return "<HttpTransaction url: %r, ip: %r, content_type: %r>" % (
            self.url[:50], self.ip, self.content_type)
