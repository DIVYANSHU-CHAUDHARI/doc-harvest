from extract import extract_text


def test_extracts_only_main_text():
    html = "<body><nav>Home</nav><main>Hello, Python!</main></body>"
    assert extract_text(html) == "Hello, Python!"

test_extracts_only_main_text()