from src.parse_utils import get_value_from_soups
from src.soup_utils import extract_soup_items


def extract_game_items(page_soup, verbose: bool = True) -> list[str]:
    target_div = "game-item-wrapper"
    game_items = extract_soup_items(page_soup, target_div=target_div, verbose=True)

    if verbose:
        num_games = len(game_items)
        print(f"Bundle content: {num_games} games.")

    return game_items


def extract_metadata_for_given_game(game_soup) -> dict[str, dict[str, str]]:
    target_div = "game-info-title-wrapper"
    info_items = extract_soup_items(game_soup, target_div=target_div, verbose=False)

    title = get_value_from_soups(info_items, "title")
    href = get_value_from_soups(info_items, "href")
    slug = get_value_from_soups(info_items, "data-game-slug")

    return {slug: {"title": title, "href": href}}


def extract_metadata_for_all_games(game_items: list) -> dict[str, dict[str, str]]:
    metadata = {}

    for game_soup in game_items:
        game_metadata = extract_metadata_for_given_game(game_soup=game_soup)
        metadata.update(game_metadata)

    return metadata
