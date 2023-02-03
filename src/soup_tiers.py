from src.parse_utils import parse_price_from_soup
from src.soup_utils import extract_soup_items


def extract_tier_items(page_soup, verbose=True):
    target_div = "game-item-column-head"
    column_items = extract_soup_items(page_soup, target_div=target_div, verbose=True)

    if verbose:
        # NB: The first column is for game names ; subsequent columns are for bundle tiers.
        num_columns = len(column_items)
        print(f"#columns = {num_columns}")

    return column_items


def extract_prices_for_given_tier(tier_soup):
    target_div = "tier-price"
    info_items = extract_soup_items(tier_soup, target_div=target_div, verbose=False)
    tier_prices = [parse_price_from_soup(e) for e in info_items]

    return tier_prices


def extract_prices_for_all_tiers(tier_items, verbose=True):
    tier_prices = []

    for tier_soup in tier_items:
        tier_prices += extract_prices_for_given_tier(tier_soup=tier_soup)

    if verbose:
        print(f"Bundle tiers: {tier_prices}")

    return tier_prices
