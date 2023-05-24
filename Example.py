# Example of creating a program for parsing and checking proxies.

from ProxyParser import ProxyParser

proxies = ProxyParser.parseProxy() 
proxies_file = open("proxies.txt", "w+")

for proxy in proxies:
    if ProxyParser.checkProxy(proxy):
        print(f"[WORKING] - {proxy}")
        
        with open("proxies.txt", "a") as proxies_file:
            proxies_file.write("\n" + proxy)
    else:
        print(f"[DEAD] - {proxy}")
