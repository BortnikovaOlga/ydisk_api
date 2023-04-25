import requests
from requests import Response


class Client:
    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        """
        Request method
        method: method for the new Request object: get, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        return requests.request(method, url,  **kwargs)

    @staticmethod
    def get(url,  **kwargs):
        return requests.get(url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return requests.post(url, **kwargs)

    @staticmethod
    def put(url, **kwargs):
        return requests.put(url, **kwargs)

    @staticmethod
    def patch(url, **kwargs):
        return requests.patch(url, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return requests.delete(url, **kwargs)


