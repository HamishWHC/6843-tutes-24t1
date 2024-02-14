import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Silences warnings about not verifying Burp's CA certificate.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s = requests.session() # This session object saves our settings for the lifetime of the script.
s.verify = False # Skip trying to verify TLS certs, due to Burp's CA.
s.proxies = {"https": "http://127.0.0.1:8080"} # Proxy requests through Burp.

r = s.get("https://whoami.quoccabank.com") # Send a GET request to whoami.
print(r.content) # b"Hi HamishWHC! Here's a flag: COMP6443{hi_im_HamishWHC_hwOk6dGApTnDudlmsKl-}"