from src.filter_utils import filter_price_items
from src.parse_utils import parse_price_from_soup
from src.soup_utils import extract_soup_items


def extract_price_header(page_soup) -> list[str]:
    target_div = "game-header-current-prices"
    return extract_soup_items(page_soup, target_div=target_div, verbose=False)


def extract_price_items_from_header(price_header: list) -> list[dict[str, list]]:
    target_div = "game-info-price-col"
    price_items = []

    for soup in price_header:
        price_items += extract_soup_items(soup, target_div=target_div, verbose=False)

    return price_items


def extract_price_items(page_soup, verbose: bool = False) -> list[dict[str, list]]:
    price_header = extract_price_header(page_soup)
    price_items = extract_price_items_from_header(price_header)
    price_items = filter_price_items(price_items)

    if verbose:
        num_prices = len(price_items)
        print(f"#prices = {num_prices}")

    return price_items


def extract_metadata_for_given_price(price_soup) -> dict[str, float | None]:
    price = parse_price_from_soup(price_soup)

    if price is not None:
        href = price_soup["href"]
        price_metadata = {href: price}
    else:
        price_metadata = {}

    return price_metadata


def extract_metadata_for_all_prices(price_items: list) -> dict[str, float | None]:
    metadata = {}

    for price_soup in price_items:
        price_metadata = extract_metadata_for_given_price(price_soup=price_soup)
        metadata.update(price_metadata)

    return metadata
