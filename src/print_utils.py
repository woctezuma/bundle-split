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


def convert_price_for_spreadsheet(price):
    price_str = f"{price:.2f}"
    return price_str.replace(".", ",")


def export_ask_prices_for_spreadsheet(bundle_metadata, ask_prices):
    cell_separator = "\t"
    currency = get_currency_symbol()

    print(f"\nGame name{cell_separator}Reseller price")
    print_line_separator()

    for slug in sorted(ask_prices, key=lambda x: ask_prices[x], reverse=True):
        title = bundle_metadata[slug]["title"]
        price = ask_prices[slug]

        price_str = convert_price_for_spreadsheet(price)
        print(f"{title}{cell_separator}{price_str}")

    print_line_separator()
    total = get_bundle_value(ask_prices)
    print(f"Total: {total:.2f} {currency}")

    return
