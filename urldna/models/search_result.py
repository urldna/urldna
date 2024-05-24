class SearchResult(object):

    def __init__(self, 
                search_id=None, 
                query=None, 
                elapsed_time=None, 
                fetched_result=None, 
                search_date=None,
                scan_results=[]):
        """
        Init Search result
        :param search_id: Search ID
        :param query: Query
        :param elapsed_time: Elapsed Time
        :param fetched_result: Fetched Result
        :param search_date: Search Date
        :param user_id: User ID
        :param scan_results: list of ScanResult
        """
        self.search_id = search_id
        self.query = query
        self.elapsed_time = elapsed_time
        self.fetched_result = fetched_result
        self.search_date = search_date
        self.scan_results = scan_results

    def __repr__(self):
        return "<SearchResult query: %r fetched_result: %r>" % (str(self.query), str(self.fetched_result))
