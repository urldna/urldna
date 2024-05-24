class ConsoleMessage(object):

    def __init__(self,
                text=None,
                type=None) -> None:
        # Fields
        self.text = text
        self.type = type

    def __repr__(self):
        return "<ConsoleMessage text: %r, type: %r>" % (
            self.text[:50], self.type)
