import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
def extract_name_from_url(url: str) -> str:
    m = re.search(r"known_by_([A-Za-z]+)\.html", url)
    return m.group(1) if m else ""

def get_link_at_position(url: str, position_1_based: int, ctx) -> str:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    if position_1_based < 1 or position_1_based > len(links):
        raise IndexError(f"Requested position {position_1_based} but page has {len(links)} links")
    return links[position_1_based - 1].get("href", "")

start_url = input("Enter URL: ").strip()
position = int(input("Enter position (1-based): ").strip())
count = int(input("Enter count (number of times to follow): ").strip())

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

sequence = []
current_url = start_url

sequence.append(extract_name_from_url(current_url))

for _ in range(count):
    next_url = get_link_at_position(current_url, position, ctx)
    name = extract_name_from_url(next_url)
    sequence.append(name)
    current_url = next_url

# --- Output ---
print("Sequence of names:", " ".join(n for n in sequence if n))
if sequence:
    print("Last name in sequence:", sequence[-1])