# TODO: choose a better name for this module
from . import utils
from .enums import HttpMethod


class RequestOptions(object):
    def __init__(self, path, params, method, data=None):
        assert len(path) > 0
        assert len(params) > 0
        assert isinstance(method, int)
        assert method is HttpMethod.GET or method is HttpMethod.POST

        self.path = path
        self.params = params
        self._method = method
        # TODO: rename to 'body'
        self.data = data

    @property
    def method_string(self):
        return HttpMethod.string(self._method)

    def is_post(self):
        return self._method is HttpMethod.POST

    @property
    def query_string(self, do_not_encode=None):
        # TODO: add option to sort params alphabetically(for PAM requests)
        if do_not_encode is None:
            do_not_encode = []

        s = []
        e = utils.url_encode

        for k, v in self.params.items():
            if k in do_not_encode:
                continue
            s.append(e(k) + "=" + e(v))

        return str('&'.join(s))
