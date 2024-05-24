class Viewport(object):

    def __init__(self,
                device=None,
                width=None,
                height=None) -> None:
        # Fields
        self.device = device
        self.width = width
        self.height = height

    def __repr__(self):
        return "<Viewport device: %r, width: %r, height: %r>" % (
            self.device, self.width, self.height)
