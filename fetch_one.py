import httpx
from bs4 import BeautifulSoup
from extract import extract_text

# url = "https://wiki.python.org/python/getting-started/doc-harvest-missing-page.html"
url = "https://wiki.python.org/python/getting-started/BeginnersGuide.html"

response = httpx.get(url, timeout=10.0)
# print("Response:", response.text)
content_type = response.headers.get("content-type", "")
media_type = content_type.split(";", 1)[0].strip().lower()

if not response.is_success:
    print(f"Skipping HTTP {response.status_code}")
elif media_type != "text/html":
    print("Skipping non-HTML content type:", content_type)
else:
    extract_text = extract_text(response.text)
    print("Text preview:", extract_text)
