from src.disk_utils import load_tiers_from_disk, save_tiers_to_disk
from src.fetch_utils import fetch_bundle_page_with_given_slug
from src.soup_tiers import extract_prices_for_all_tiers, extract_tier_items


def fetch_tiers(bundle_slug, page_soup=None):
    if page_soup is None:
        page_soup = fetch_bundle_page_with_given_slug(bundle_slug)

    tier_items = extract_tier_items(page_soup=page_soup)
    tier_prices = extract_prices_for_all_tiers(tier_items=tier_items)

    save_tiers_to_disk(tier_prices, bundle_slug=bundle_slug)

    return tier_prices


def compute_target_cost(tier_prices):
    return max(tier_prices)


def fetch_target_cost(bundle_slug, page_soup=None):
    tier_prices = fetch_tiers(bundle_slug, page_soup=page_soup)

    return compute_target_cost(tier_prices)


def load_target_cost(bundle_slug, page_soup=None):
    try:
        tier_prices = load_tiers_from_disk(bundle_slug)
    except FileNotFoundError:
        tier_prices = fetch_tiers(bundle_slug, page_soup=page_soup)

    return compute_target_cost(tier_prices)
