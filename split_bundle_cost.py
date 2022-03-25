from src.disk_utils import load_prices_from_disk, load_bundle_from_disk
from src.print_utils import print_prices
from src.split_utils import get_ask_prices_for_whole_bundle, split_bundle_cost


def main():
    bundle_slug = "humble-stand-with-ukraine-bundle"
    target_cost_in_euros = 36.39

    price_metadata = load_prices_from_disk(bundle_slug)

    ask_prices = get_ask_prices_for_whole_bundle(price_metadata)
    split_prices = split_bundle_cost(ask_prices, target_cost_in_euros)

    bundle_metadata = load_bundle_from_disk(bundle_slug)
    print_prices(bundle_metadata, split_prices)

    return True


if __name__ == "__main__":
    main()
