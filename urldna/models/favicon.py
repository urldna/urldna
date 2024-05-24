class Favicon(object):

    def __init__(self,
                url=None,
                blob_uri=None,
                name=None,
                phash=None,
                width=None,
                height=None,
                mimetype=None,
                format=None) -> None:
        # Fields
        self.url = url
        self.blob_uri = blob_uri
        self.name = name
        self.phash = phash
        self.width = width
        self.height = height
        self.mimetype = mimetype
        self.format = format

    def __repr__(self):
        return "<Favicon url: %r, name: %r>" % (self.url[:50], self.name)
