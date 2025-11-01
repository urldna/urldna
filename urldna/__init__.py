import time
import requests

# Exception
from urldna.exceptions.api_exception import ApiException

# Schemas
from urldna.schemas.scan_schema import scan_schema, scans_schema
from urldna.schemas.viewport_schema import viewports_schema
from urldna.schemas.scan_result_schema import scan_result_schema
from urldna.schemas.user_agent_schema import user_agents_schema
from urldna.schemas.fast_check_schema import fast_check_schema
from urldna.schemas.scan_feedback_schema import scan_feedback_schema


class UrlDNA:

    # URL
    ENDPOINT_URL = "http://api.urldna.io/v1"

    def __init__(self, api_key):
        """
        Initialize urlDNA client with API KEY, register to get a FREE API key.
        :param api_key: API key, see https://urldna.io/profile
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

    def get_scan(self, scan_id):
        """
        Get Scan by Scan ID
        :param scan_id: Scan ID
        :return: Scan object
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/scan/"+str(scan_id)

        # Get response
        response = requests.get(api_url, headers=self.headers)

        if response.status_code==200:
            return scan_result_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())

    def search(self, query, page=1):
        """
        Search by query text
        :param query: Domain or CQL syntax
        :param page: Pagination (only for PREMIUM users)
        :return: Search results
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/search"
        # payload
        payload = {"query": query}
        # params
        params = {"page": page}

        # Get response
        response = requests.post(api_url, headers=self.headers, json=payload, params=params)

        if response.status_code==200:
            return scans_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())

    def viewports(self):
        """
        Get list of all available viewports
        :return: List of viewports (device, height, width)
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/viewports"

        # Get response
        response = requests.get(api_url, headers=self.headers)

        if response.status_code==200:
            return viewports_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())

    def user_agents(self):
        """
        Get list of all available user agents
        :return: List of user agents (browser, device, user_agent)
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/user-agents"

        # Get response
        response = requests.get(api_url, headers=self.headers)

        if response.status_code==200:
            return user_agents_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())

    def async_create_scan(self, url,
                          device="DESKTOP",
                          user_agent=None,
                          width=None,
                          height=None,
                          waiting_time=5,
                          scanned_from="DEFAULT",
                          private_scan=False,
                          http_referer=None,
                          submitter_tags=[]):
        """
        Create async new scan, it returns an empty scan object with PENDING/RUNNING status, you have to check a few moments later if status is DONE to get full access to all scan attributes
        :param url: url to scan
        :param device: DESKTOP/MOBILE
        :param user_agent: User agents
        :param width: viewport width
        :param height: viewport height
        :param waiting_time: waiting time
        :param scanned_from: Scan country source, only for PREMIUM users
        :param private_scan: Private scan
        :param http_referer: HTTP Referer URL
        :param submitter_tags: List of user tags, only for PREMIUM users
        :return: Scan object
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/scan"

        # payload
        payload = {}
        payload["submitted_url"] = url
        if scanned_from:
            payload["scanned_from"] = scanned_from
        if device:
            payload["device"] = device
        if user_agent:
            payload["user_agent"] = user_agent
        if http_referer:
            payload["http_referer"] = http_referer
        if width:
            payload["width"] = int(width)
        if height:
            payload["height"] = int(height)
        if waiting_time:
            payload["waiting_time"] = int(waiting_time)
        if private_scan:
            payload["private_scan"] = bool(private_scan)
        if submitter_tags:
            payload["submitter_tags"] = submitter_tags

        # Get response
        response = requests.post(api_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return scan_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())

    def create_scan(self, url,
                          device="DESKTOP",
                          user_agent=None,
                          width=None,
                          height=None,
                          waiting_time=5,
                          scanned_from="DEFAULT",
                          private_scan=False,
                          http_referer=None,
                          submitter_tags=[]):
        """
        Create new scan, it could be take few minutes
        :param url: url to scan
        :param device: DESKTOP/MOBILE
        :param user_agent: User agents
        :param width: viewport width
        :param height: viewport height
        :param waiting_time: waiting time
        :param scanned_from: Scan country source
        :param private_scan: Private scan
        :param http_referer: HTTP Referer URL
        :param submitter_tags: List of user tags, only for PREMIUM users
        :return: Scan object
        """
        try:
            # Create async scan
            scan = self.async_create_scan(
                url, 
                device=device, 
                user_agent=user_agent, 
                width=width, 
                height=height, 
                waiting_time=waiting_time, 
                scanned_from=scanned_from,
                private_scan=private_scan,
                http_referer=http_referer,
                submitter_tags=submitter_tags)
            status = scan.status
            scan_result = None
            while status not in ["DONE", "ERROR"]:
                # wait 2 seconds
                time.sleep(2)
                # Get Scan
                scan_result = self.get_scan(scan.id)
                status = scan_result.scan.status
            return scan_result
        except Exception as e:
            raise ApiException(str(e))
        
    def fast_check(self, url):
        """
        Check if URL is CLEAN, MALICIOUS or UNRATED
        :param url: Submitted URL
        :return: FastCheck
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/fast-check"

        # payload
        payload = {
            "url": url
        }

        # Get response
        response = requests.post(api_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return fast_check_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())
        
    def scan_feedback(self, 
                          scan_id,
                          feedback):
        """
        Toggle scan feedback
        :param url: url to scan
        :param feedback: MALICIOUS or SAFE
        :return: Scan Feedback object
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/scan/"+str(scan_id)+"/feedback"

        # payload
        payload = {
            "feedback": feedback
        }

        # Get response
        response = requests.post(api_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return scan_feedback_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())