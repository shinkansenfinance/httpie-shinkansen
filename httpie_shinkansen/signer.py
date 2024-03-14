import os
import requests.auth
from shinkansen import jws


class ShinkansenSigner(requests.auth.AuthBase):
    def __init__(self):
        self.shinkansen_certificate = os.environ.get("SHINKANSEN_CERTIFICATE")
        self.shinkansen_key = os.environ.get("SHINKANSEN_KEY")
        self.shinkansen_certificate_path = os.environ.get("SHINKANSEN_CERTIFICATE_PATH")
        self.shinkansen_key_path = os.environ.get("SHINKANSEN_KEY_PATH")
        if not (self.has_plain_certificates() or self.has_path_certificates()):
            raise ValueError(
                """
                Enviroment variablesmust be set to use Auth Shinkansen plugin.
                Either SHINKANSEN_CERTIFICATE and SHINKANSEN_KEY, plain
                certificate and key strings, or SHINKANSEN_CERTIFICATE_PATH and
                SHINKANSEN_KEY_PATH, paths to the certificate and key files. 
                They have to be PEM encoded strings.
                """
            )

    def has_plain_certificates(self):
        return (
            self.shinkansen_certificate is not None and self.shinkansen_key is not None
        )

    def has_path_certificates(self):
        return (
            self.shinkansen_certificate_path is not None
            and self.shinkansen_key_path is not None
        )

    def sign(self, r) -> str:
        cert = None
        pk = None
        if self.has_plain_certificates():
            cert = jws.certificate_from_pem_bytes(self.shinkansen_certificate.encode())
            pk = jws.private_key_from_pem_bytes(self.shinkansen_key.encode())
        else:
            cert = jws.certificate_from_pem_file(self.shinkansen_certificate_path)
            pk = jws.private_key_from_pem_file(self.shinkansen_key_path)
        return jws.sign(r.body.decode("utf-8"), pk, cert)

    def __call__(self, r):
        if r.body is None:
            return r
        signature = self.sign(r)
        r.headers["shinkansen-jws-signature"] = signature
        return r
