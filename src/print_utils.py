from src.parse_utils import get_currency_symbol
from src.split_utils import get_bundle_value


def print_line_separator() -> None:
    sep = "="
    num_sep = 11

    print(sep * num_sep)


def print_prices(
    bundle_metadata: dict[str, dict[str, str]],
    prices: dict[str, float],
) -> None:
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


def convert_price_for_spreadsheet(price: float) -> str:
    price_str = f"{price:.2f}"
    return price_str.replace(".", ",")


def export_ask_prices_for_spreadsheet(
    bundle_metadata: dict[str, dict[str, str]],
    prices: dict[str, float],
) -> None:
    cell_separator = "\t"
    currency = get_currency_symbol()

    print(f"\nGame name{cell_separator}Reseller price")
    print_line_separator()

    for slug in sorted(prices, key=lambda x: prices[x], reverse=True):
        title = bundle_metadata[slug]["title"]
        price = prices[slug]

        price_str = convert_price_for_spreadsheet(price)
        print(f"{title}{cell_separator}{price_str}")

    print_line_separator()
    total = get_bundle_value(prices)
    print(f"Total: {total:.2f} {currency}")
