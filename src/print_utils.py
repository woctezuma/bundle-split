from src.parse_utils import get_currency_symbol
from src.split_utils import get_bundle_value


def print_line_separator():
    sep = "="
    num_sep = 11

    print(sep * num_sep)

    return


def print_prices(bundle_metadata, prices):
    currency = get_currency_symbol()

    print("\nAvailable:")
    print_line_separator()

    for slug in sorted(prices, key=lambda x: prices[x], reverse=True):
        title = bundle_metadata[slug]["title"]
        price = prices[slug]

        print(f"☐ {title} - {price:.2f} {currency}")

    print_line_separator()
    total = get_bundle_value(prices)
    print(f"Total: {total:.2f} {currency}")

    return
