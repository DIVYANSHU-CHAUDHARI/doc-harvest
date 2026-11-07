import httpx
from bs4 import BeautifulSoup

# url = "https://wiki.python.org/python/getting-started/doc-harvest-missing-page.html"
url = "https://wiki.python.org/python/getting-started/BeginnersGuide.html"


response = httpx.get(url, timeout=10.0)
content_type = response.headers.get("content-type", "")
media_type = content_type.split(";", 1)[0].strip().lower()

if not response.is_success:
    print(f"Skipping HTTP {response.status_code}")
elif media_type != "text/html":
    print("Skipping non-HTML content type:", content_type)
else:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title")
    print("Page title:", title.get_text(strip=True) if title else "(no title)")