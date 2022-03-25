from src.filter_utils import filter_price_items
from src.parse_utils import parse_price
from src.soup_utils import extract_soup_items


def extract_price_header(page_soup):
    target_div = "game-header-current-prices"
    price_header = extract_soup_items(page_soup, target_div=target_div, verbose=False)

    return price_header


def extract_price_items_from_header(price_header):
    target_div = "game-info-price-col"
    price_items = []

    for soup in price_header:
        price_items += extract_soup_items(soup, target_div=target_div, verbose=False)

    return price_items


def extract_price_items(page_soup, verbose=False):
    price_header = extract_price_header(page_soup)
    price_items = extract_price_items_from_header(price_header)
    price_items = filter_price_items(price_items)

    if verbose:
        num_prices = len(price_items)
        print(f"#prices = {num_prices}")

    return price_items


def extract_metadata_for_given_price(price_soup):
    price_text = price_soup.text
    price = parse_price(price_text)

    if price is not None:
        href = price_soup["href"]
        price_metadata = {href: price}
    else:
        price_metadata = {}

    return price_metadata


def extract_metadata_for_all_prices(price_items):
    metadata = {}

    for price_soup in price_items:
        price_metadata = extract_metadata_for_given_price(price_soup=price_soup)
        metadata.update(price_metadata)

    return metadata
