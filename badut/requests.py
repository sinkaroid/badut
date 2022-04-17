from urllib.request import urlopen, Request
from urllib.parse import urlencode
from json import loads
from . import __version__


class Badut(object):
    """Badut client

    Methods
    -------

    get: function
        Makes a GET request to the target URL

    post: function
        Makes a POST request to the target URL

    """

    def __init__(self, json: bool = False, headers: dict = {}, timeout: int = None):
        """Initialize the Badut object

        Parameters
        ----------
        json : bool
            Whether to return the data as JSON

        headers : dict
            The headers to be sent with the request

        timeout : int
            The timeout in seconds
        """
        if json and headers != {}:
            self.json = True
            self.headers = headers
            self.timeout = timeout
        elif json and headers == {}:
            self.json = True
            self.headers = {"User-Agent": f"Badut/{__version__}"}
            self.timeout = timeout
        else:
            self.json = False
            self.headers = {"User-Agent": f"Badut/{__version__}"}
            self.timeout = timeout

    async def get(self, target: str):
        """Make a GET request to the target URL

        Parameters
        ----------
        target : str
            The target URL

        timeout : int
            The timeout in seconds

        headers : dict
            The headers to be sent with the request


        Returns
        -------
        dict
            The raw data
        """
        self.req = Request(target, headers=self.headers)
        with urlopen(self.req, timeout=self.timeout) as response:
            data = response.read()
            if self.json:
                return loads(data)
            return data

    async def post(self, target: str, data: dict):
        """Make a POST request to the target URL

        Parameters
        ----------
        target : str
            The target URL

        data : dict
            The data to be sent with the request

        Returns
        -------
        dict
            The response data
        """
        self.summary = urlencode(data).encode("utf-8")
        self.req = Request(target, self.summary)
        with urlopen(self.req) as response:
            return loads(response.read().decode("utf-8"))
