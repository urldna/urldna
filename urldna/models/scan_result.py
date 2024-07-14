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
                 scan_feedback=None,
                 http_transactions=None,
                 console_messages=None,
                 malicious=None):
        """
        Init Full Scan result
        :param scan: Scan
        :param ip_address: IpAddress
        :param certificate: Certificate
        :param favicon: Favicon
        :param screenshot: Screenshot
        :param dom: Page DOM
        :param cookies: List of Cookie
        :param scan_feedback: Scan Feedback
        :param technologies: List of Technology
        :param http_transactions: List of HttpTransaction
        :param console_messages: List of ConsoleMessage
        :param malicious: Malicious
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
        self.scan_feedback = scan_feedback
        self.http_transactions = http_transactions
        self.console_messages = console_messages
        self.malicious = malicious

    def __repr__(self):
        return "<ScanResult scan: %r >" % self.scan
