class IpAddress(object):

    def __init__(self,
                ip=None,
                asn=None,
                city=None, 
                country=None, 
                country_code=None, 
                isp=None, 
                latitude=None, 
                longitude=None, 
                org=None, 
                region=None, 
                timezone_gmt=None, 
                type=None) -> None:
        # Fields
        self.ip = ip
        self.asn = asn
        self.city = city
        self.country = country
        self.country_code = country_code
        self.isp = isp
        self.latitude = latitude
        self.longitude = longitude
        self.org = org
        self.region = region
        self.timezone_gmt = timezone_gmt
        self.type = type

    def __repr__(self):
        return "<IpAddress ip: %r, asn: %r, country: %r>" % (
            self.ip, self.asn, self.country)
