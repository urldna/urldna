class Screenshot(object):

    def __init__(self,
                blob_uri = None,
                phash=None,
                width=None,
                height=None,
                mimetype=None,
                format=None) -> None:
        
        # Fields
        self.blob_uri = blob_uri
        self.phash = phash
        self.width = width
        self.height = height
        self.mimetype = mimetype
        self.format = format

    def __repr__(self):
        return "<Screenshot phash: %r, blob_uri: %r>" % (
            self.phash, self.blob_uri)
