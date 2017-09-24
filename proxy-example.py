# Python 2 proxy example
# https://www.geosurf.com/resources/residential-ips-integration-guide

import urllib2

# Our gateway’s hosthname + port, check your dashboard for full gateways list
gs_proxy_addr = ‘gw1.geosurf.io:8081’

proxy = urllib2.ProxyHandler({‘http’: gs_proxy_addr,
                              ‘https’: gs_proxy_addr})

opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

urllib2.urlopen(‘http://www.example.com’)
urllib2.urlopen(‘http://www.example.com’)
