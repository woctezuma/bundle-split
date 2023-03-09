import argparse

import list_bundle_content
import list_product_prices
import split_bundle_cost
from src.fetch_utils import fetch_bundle_page_with_given_slug
from src.tier_utils import fetch_target_cost
from src.trim_utils import standardize_bundle_slug


def main(bundle_slug, target_cost_in_euros=None):
    bundle_slug = standardize_bundle_slug(bundle_slug)

    page_soup = fetch_bundle_page_with_given_slug(bundle_slug)

    if target_cost_in_euros is None:
        target_cost_in_euros = fetch_target_cost(bundle_slug, page_soup=page_soup)

    list_bundle_content.main(bundle_slug, page_soup=page_soup)
    list_product_prices.main(bundle_slug)
    split_bundle_cost.main(bundle_slug, target_cost_in_euros)

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute fair prices for a bundle split, based on prices observed at gray-market key resellers.",
    )
    parser.add_argument(
        "--bundle",
        dest="bundle_slug",
        type=str,
        default="humble-choice-march-2022",
        help="Bundle slug at gg.deals",
    )
    parser.add_argument(
        "--cost",
        dest="target_cost_in_euros",
        type=float,
        default=None,
        help="Target cost of the bundle, e.g. the retail price of the bundle, or the cost of the highest tier.",
    )
    args = parser.parse_args()

    main(args.bundle_slug, args.target_cost_in_euros)
