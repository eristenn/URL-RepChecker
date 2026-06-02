from core.url_utils import extract_domain, is_https


def analyze_url(url: str) -> dict:
    return {
        "url": url,
        "domain": extract_domain(url),
        "https": is_https(url)
    }