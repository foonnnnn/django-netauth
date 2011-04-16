from __future__ import absolute_import

from openid.extensions.ax import FetchResponse

from netauth.backends.openid import OpenIDBackend
from netauth import settings


class GoogleBackend(OpenIDBackend):

    def get_extra_data(self, resp):
        print(resp)
        return FetchResponse.fromSuccessResponse(resp)

    def extract_data(self, extra, backend_field):
        return extra.getSingle(settings.AX_URIS[backend_field], '')
