"""
ProxyParser Library
~~~~~~~~~~~~~~~~~~~

ProxyParser is a library for checking/parsing proxies.

Example how to use:
    >>> from ProxyParser import ProxyParser
    >>> 
    >>> working_proxies = []
    >>> proxies = ProxyParser.parseProxy()
    >>> 
    >>> for proxy in proxies:
    >>>    if ProxyParser.checkProxy(proxy):
    >>>       working_proxies.append(proxy)
    >>> print("Working proxies:")
    >>> print(working_proxies)
    Working proxies:
    ['101.132.25.152:5678', '120.196.188.21:9091']

(C) 2023 by TurboKoT1.
"""

import requests, socket

class ProxyParser:
    def __init__(self):
        pass

    def parseProxy(proxy_sites=["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"]):
        """
        This function parses proxies.

        Args:
            proxy_sites (list): List of sites from which proxies'll be parsed.

        Returns:
            List: List of parsed proxies.
        """

        proxies = []

        try:
            for site in proxy_sites:
                site_text = requests.get(site).text

                for proxy in site_text.split("\n"):
                    proxies.append(proxy)
        except TypeError:
            raise TypeError("Invalid proxy sites data-type")
        except requests.RequestException:
            raise RuntimeError(f"An error has been occured with attempt to parse proxy from site: {site}")

        return proxies
    
    def checkProxy(proxy, timeout=2):
        """
        This function checks proxy.

        Args:
            proxy (string): Proxy.
            timeout (integer): Max proxy response time.

        Returns:
            Boolean: Is proxy working?
        """

        try:
            splitted_proxy = proxy.split(":")

            ip = splitted_proxy[0]
            port = int(splitted_proxy[1])
        except IndexError:
            raise IndexError("Invalid proxy format")
        except AttributeError:
            raise AttributeError("Invalid proxy data-type")

        new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        new_socket.settimeout(timeout)

        try:
            new_socket.connect((ip, port))
        except:
            return False
        else:
            new_socket.close()

            return True

if __name__ == "__main__":
    print("It's library, lol")
