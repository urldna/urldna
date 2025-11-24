class ScanResult(object):

    def __init__(self, scan=None,
                 ip_address=None,
                 certificate=None,
                 favicon=None,
                 screenshot=None,
                 page=None,
                 dom=None,
                 cookies=None,
                 technologies=None,
                 http_transactions=None,
                 console_messages=None,
                 classification=None,
                 scan_whois=None,
                 redirect_chains=None):
        """
        Init Full Scan result
        :param scan: Scan
        :param ip_address: IpAddress
        :param certificate: Certificate
        :param favicon: Favicon
        :param screenshot: Screenshot
        :param dom: Page DOM
        :param cookies: List of Cookie
        :param technologies: List of Technology
        :param http_transactions: List of HttpTransaction
        :param console_messages: List of ConsoleMessage
        :param classification: Classification
        :param scan_whois: ScanWhois
        :param redirect_chains: List of RedirectChain
        """
        self.scan = scan
        self.ip_address = ip_address
        self.certificate = certificate
        self.favicon = favicon
        self.screenshot = screenshot
        self.page = page
        self.dom = dom
        self.cookies = cookies
        self.technologies = technologies
        self.http_transactions = http_transactions
        self.console_messages = console_messages
        self.classification = classification
        self.scan_whois = scan_whois
        self.redirect_chains = redirect_chains

    def __repr__(self):
        return "<ScanResult scan: %r >" % self.scan
