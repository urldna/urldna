class Certificate(object):

    def __init__(self,
                authority_info_access=None,
                authority_key_identifier=None,
                basic_constraints=None,
                certificate_policies=None,
                ct_precert_scts=None,
                extended_key_usage=None,
                issuer=None,
                key_usage=None,
                not_after=None,
                not_before=None,
                serial_number=None,
                subject=None,
                subject_key_identifier=None,
                version=None) -> None:
            # Fields
            self.authority_info_access = authority_info_access
            self.authority_key_identifier = authority_key_identifier
            self.basic_constraints = basic_constraints
            self.certificate_policies = certificate_policies
            self.ct_precert_scts = ct_precert_scts
            self.extended_key_usage = extended_key_usage
            self.issuer = issuer
            self.key_usage = key_usage
            self.not_after = not_after
            self.not_before = not_before
            self.serial_number = serial_number
            self.subject = subject
            self.subject_key_identifier = subject_key_identifier
            self.version = version

    def __repr__(self):
        return "<Certificate issuer: %r, subject: %r, serial_number: %r>" % (
            self.issuer, self.subject, self.serial_number)
