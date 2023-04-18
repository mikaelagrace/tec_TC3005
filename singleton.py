import urllib.parse
import urllib.request

### SINGLETON PATTERN: USING GLOBAL VARIABLE ###
_URL_FETCHER_SINGLETON_INSTANCE = None


class URLFetcher:
    """Note: this class should ONLY be used via get_url_fetcher method!"""

    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                self.urls.append(url)


def get_url_fetcher():
    global _URL_FETCHER_SINGLETON_INSTANCE
    if not _URL_FETCHER_SINGLETON_INSTANCE:
        _URL_FETCHER_SINGLETON_INSTANCE = URLFetcher()
    return _URL_FETCHER_SINGLETON_INSTANCE


if __name__ == "__main__":
    print(URLFetcher() is URLFetcher())


################## SINGLETON PATTERN: USING METACLASS #####################


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class URLFetcherSingleton(metaclass=SingletonType):
    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                urls = self.urls
                urls.append(url)
                self.urls = urls

    def dump_url_registry(self):
        return ", ".join(self.urls)
