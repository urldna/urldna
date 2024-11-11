class ScanWhois(object):

    def __init__(self,
                domain_name=None,
                registrar=None,
                creation_date=None,
                expiration_date=None,
                updated_date=None,
                name=None,
                org=None,
                address=None,
                registrant_postal_code=None,
                country=None,
                state=None,) -> None:
        # Fields
        self.domain_name = domain_name
        self.registrar = registrar
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.updated_date = updated_date
        self.name = name
        self.org = org
        self.address = address
        self.registrant_postal_code = registrant_postal_code
        self.country = country
        self.state = state

    def __repr__(self):
        return "<ScanWhois domain_name: %r, registrar: %r>" % (self.domain_name, self.registrar)
