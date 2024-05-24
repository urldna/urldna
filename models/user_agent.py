class UserAgent(object):

    def __init__(self,
                device=None,
                browser=None,
                user_agent=None,
                share=None) -> None:    
        # Fields
        self.device = device
        self.browser = browser
        self.user_agent = user_agent
        self.share = share

    def __repr__(self):
        return "<UserAgent device: %r, browser: %r, user_agent: %r>" % (
            self.device, self.browser, self.user_agent)
