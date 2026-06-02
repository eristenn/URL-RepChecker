from urllib.parse import urlparse


def extract_domain(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc


def is_https(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme.lower() == "https"