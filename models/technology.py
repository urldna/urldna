class Technology(object):

    def __init__(self,
                name=None,
                category=None,
                version=None) -> None:
        # Fields
        self.name = name
        self.category = category
        self.version = version

    def __repr__(self):
        return "<Technology name: %r, category: %r, version: %r>" % (
            self.name, self.category, self.version)
