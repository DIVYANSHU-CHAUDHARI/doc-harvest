from bs4 import BeautifulSoup


def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    section = soup.find("main") or soup.body or soup
    return section.get_text(" ", strip=True)