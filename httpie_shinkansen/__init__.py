__version__ = "0.1.0"

from httpie.plugins import AuthPlugin
from .signer import ShinkansenSigner


class ShinkansenAuthPlugin(AuthPlugin):
    name = "Shinkansen Network Auth"
    auth_type = "shinkansen"
    auth_require = False
    description = ""

    def get_auth(self):
        return ShinkansenSigner()
