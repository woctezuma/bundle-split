import cloudscraper
from bs4 import BeautifulSoup


def get_domain_url() -> str:
    return "https://gg.deals"


def get_news_endpoint(news_category: str, news_item_slug: str) -> str:
    return f"/{news_category}/{news_item_slug}"


def get_bundle_endpoint(bundle_slug: str) -> str:
    return get_news_endpoint(news_category="bundle", news_item_slug=bundle_slug)


def get_bundle_url(bundle_slug: str) -> str:
    return get_domain_url() + get_bundle_endpoint(bundle_slug)


def get_product_url(product_href: str) -> str:
    return get_domain_url() + product_href


def fetch_html_page(
    url: str,
    scraper: cloudscraper.CloudScraper | None = None,
) -> BeautifulSoup:
    if scraper is None:
        scraper = cloudscraper.create_scraper()
    return BeautifulSoup(scraper.get(url).text, features="html.parser")


def fetch_bundle_page_with_given_slug(
    bundle_slug: str,
    scraper: cloudscraper.CloudScraper | None = None,
) -> BeautifulSoup:
    return fetch_html_page(url=get_bundle_url(bundle_slug), scraper=scraper)


def fetch_product_page_with_given_href(
    product_href: str,
    scraper: cloudscraper.CloudScraper | None = None,
) -> BeautifulSoup:
    return fetch_html_page(url=get_product_url(product_href), scraper=scraper)


def main() -> bool:
    bundle_slug = "humble-stand-with-ukraine-bundle"
    fetch_bundle_page_with_given_slug(bundle_slug)
    return True


if __name__ == "__main__":
    main()
