class Page(object):

    def __init__(self,
                text=None,
                title=None,
                blob_uri=None,
                meta_tags=None,
                headers=None,
                ssdeep=None,
                outgoing_links=None) -> None:
        # Fields
        self.text = text
        self.title = title
        self.blob_uri = blob_uri
        self.meta_tags = meta_tags
        self.headers = headers
        self.ssdeep = ssdeep
        self.outgoing_links = outgoing_links

    def __repr__(self):
        return "<Page title: %r, text: %r>" % (self.title, self.text[:50])
