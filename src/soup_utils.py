from src.filter_utils import get_class, get_content, get_id, filter_price_items
from src.parse_utils import get_value_from_soups, parse_price


def extract_soup_items(soup, target_div, verbose=False):
    all_divs = soup.findAll("div")

    items = []

    for div_element in all_divs:
        div_classes = get_class(div_element)

        div_id = get_id(div_element)
        div_classes.append(div_id)

        if target_div in div_classes:
            new_items = get_content(div_element)

            items += new_items

            if verbose:
                print(f"div: {div_classes} -> {len(new_items)} items")

    return items


def extract_game_items(page_soup, verbose=True):
    target_div = "game-item-wrapper"
    game_items = extract_soup_items(page_soup, target_div=target_div, verbose=True)

    if verbose:
        num_games = len(game_items)
        print(f"Bundle content: {num_games} games.")

    return game_items


def extract_metadata_for_given_game(game_soup):
    target_div = "game-info-title-wrapper"
    info_items = extract_soup_items(game_soup, target_div=target_div, verbose=False)

    title = get_value_from_soups(info_items, "title")
    href = get_value_from_soups(info_items, "href")
    slug = get_value_from_soups(info_items, "data-game-slug")

    game_metadata = {slug: {"title": title, "href": href}}

    return game_metadata


def extract_metadata_for_all_games(game_items):
    metadata = {}

    for game_soup in game_items:
        game_metadata = extract_metadata_for_given_game(game_soup=game_soup)
        metadata.update(game_metadata)

    return metadata


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
