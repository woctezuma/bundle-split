from src.disk_utils import save_bundle_to_disk
from src.fetch_utils import fetch_bundle_page_with_given_slug
from src.soup_games import extract_game_items, extract_metadata_for_all_games


def main(bundle_slug, page_soup=None) -> bool:
    if page_soup is None:
        page_soup = fetch_bundle_page_with_given_slug(bundle_slug)

    game_items = extract_game_items(page_soup=page_soup)
    metadata = extract_metadata_for_all_games(game_items=game_items)

    print(metadata)
    save_bundle_to_disk(data=metadata, bundle_slug=bundle_slug)

    return True


if __name__ == "__main__":
    bundle_slug = "humble-stand-with-ukraine-bundle"
    main(bundle_slug)
