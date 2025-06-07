from typing import TYPE_CHECKING

from src.parse_utils import get_value_from_soups
from src.soup_utils import extract_soup_items

if TYPE_CHECKING:
    from bs4 import BeautifulSoup, Tag


def extract_game_items(
    page_soup: BeautifulSoup,
    *,
    verbose: bool = True,
) -> list[Tag]:
    target_div = "game-item-wrapper"
    game_items = extract_soup_items(page_soup, target_div=target_div, verbose=True)

    if verbose:
        num_games = len(game_items)
        print(f"Bundle content: {num_games} games.")

    return game_items


def extract_metadata_for_given_game(
    game_soup: Tag,
) -> dict[str | None, dict[str, str | None]]:
    target_div = "game-info-title-wrapper"
    info_items = extract_soup_items(game_soup, target_div=target_div, verbose=False)

    title = get_value_from_soups(info_items, "title")
    if title is None:
        title = get_value_from_soups(info_items, "data-title-auto-hide")
    href = get_value_from_soups(info_items, "href")
    slug = get_value_from_soups(info_items, "data-game-slug")

    return {slug: {"title": title, "href": href}}


def extract_metadata_for_all_games(
    game_items: list,
) -> dict[str | None, dict[str, str | None]]:
    metadata = {}

    for game_soup in game_items:
        game_metadata = extract_metadata_for_given_game(game_soup=game_soup)
        metadata.update(game_metadata)

    return metadata
