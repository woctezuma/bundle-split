from src.filter_utils import get_class, get_content


def extract_soup_items(soup, target_div, verbose=False):
    all_divs = soup.findAll("div")

    items = []

    for div_element in all_divs:
        div_classes = get_class(div_element)

        if target_div in div_classes:
            new_items = get_content(div_element)

            items += new_items

            if verbose:
                print(f"div: {div_classes} -> {len(new_items)} items")

    return items


def extract_game_items(page_soup):
    target_div = "game-item-wrapper"
    game_items = extract_soup_items(page_soup, target_div=target_div, verbose=True)

    return game_items


def extract_metadata_for_given_game(game_soup):
    target_div = "game-info-title-wrapper"
    info_items = extract_soup_items(game_soup, target_div=target_div, verbose=False)

    title = info_items[0]["title"]
    href = info_items[0]["href"]
    slug = info_items[1]["data-game-slug"]

    game_metadata = {slug: {"title": title, "href": href}}

    return game_metadata


def extract_metadata_for_all_games(game_items):
    metadata = {}

    for game_soup in game_items:
        game_metadata = extract_metadata_for_given_game(game_soup=game_soup)
        metadata.update(game_metadata)

    return metadata
