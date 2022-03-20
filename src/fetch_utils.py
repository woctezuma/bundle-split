import requests
from bs4 import BeautifulSoup


def get_domain_url():
    return "https://gg.deals"


def get_news_endpoint(news_category, news_item_slug):
    return f"/{news_category}/{news_item_slug}"


def get_bundle_endpoint(bundle_slug):
    return get_news_endpoint(news_category="bundle", news_item_slug=bundle_slug)


def get_bundle_url(bundle_slug):
    return get_domain_url() + get_bundle_endpoint(bundle_slug)


def fetch_bundle_page(bundle_url):
    r = requests.get(bundle_url)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, features="html.parser")
    return soup


def fetch_bundle_page_with_given_slug(bundle_slug):
    return fetch_bundle_page(bundle_url=get_bundle_url(bundle_slug))


def main():
    bundle_slug = "humble-stand-with-ukraine-bundle"
    page_soup = fetch_bundle_page_with_given_slug(bundle_slug)
    return True


if __name__ == "__main__":
    main()
