import time
import requests

# Exception
from urldna.exceptions.api_exception import ApiException

# Schemas
from urldna.schemas.scan_schema import scan_schema, scans_schema
from urldna.schemas.viewport_schema import viewports_schema
from urldna.schemas.scan_result_schema import scan_result_schema
from urldna.schemas.user_agent_schema import user_agents_schema


class UrlDNA:

    # URL
    ENDPOINT_URL = "https://api.urldna.io"

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

    def search(self, query):
        """
        Search by query text
        :param query: Domain or CQL syntax
        :return: Search results
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/search"
        # payload
        payload = {"query": query}

        # Get response
        response = requests.post(api_url, headers=self.headers, json=payload)

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
                          user_agent="Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
                          width=1920,
                          height=1080,
                          waiting_time=5,
                          private_scan=False):
        """
        Create async new scan, it returns an empty scan object with PENDING/RUNNING status, you have to check a few moments later if status is DONE to get full access to all scan attributes
        :param url: url to scan
        :param device: DESKTOP/MOBILE
        :param user_agent: User agents
        :param width: viewport width
        :param height: viewport height
        :param waiting_time: waiting time
        :param private_scan: Private scan
        :return: Scan object
        """
        # URL
        api_url = UrlDNA.ENDPOINT_URL + "/scan"

        # payload
        payload = {
            "submitted_url": url,
            "device": device,
            "user_agent": user_agent,
            "width": int(width),
            "height": int(height),
            "waiting_time": int(waiting_time),
            "private_scan": bool(private_scan)
        }

        # Get response
        response = requests.post(api_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return scan_schema.load(response.json())
        else:
            raise ApiException(response.content.decode())

    def create_scan(self, url,
                          device="DESKTOP",
                          user_agent="Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
                          width=1920,
                          height=1080,
                          waiting_time=5,
                          private_scan=False):
        """
        Create new scan, it could be take few minutes
        :param url: url to scan
        :param device: DESKTOP/MOBILE
        :param user_agent: User agents
        :param width: viewport width
        :param height: viewport height
        :param waiting_time: waiting time
        :param private_scan: Private scan
        :return: Scan object
        """
        try:
            # Create async scan
            scan = self.async_create_scan(url, device, user_agent, width, height, waiting_time, private_scan)
            status = scan.status
            
            while status not in ["DONE", "ERROR"]:
                # wait 2 seconds
                time.sleep(2)
                # Get Scan
                scan_result = self.get_scan(scan.id)
                status = scan_result.scan.status
            return scan_result
        except Exception as e:
            raise ApiException(str(e))