import ssl
import urllib.request
from bs4 import BeautifulSoup
import re

# Ignore SSL cert errors (PY4E style)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ").strip()

# Fetch and parse
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

nums = [int(tag.text) for tag in soup.find_all("span") if tag.text.isdigit()]

print("Count", len(nums))
print("Sum", sum(nums))