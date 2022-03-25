from src.parse_utils import get_currency_symbol


def get_keyshop_label():
    return "#keyshops"


def get_ask_price_for_single_product(product_metadata):
    keyshop_label = get_keyshop_label()

    try:
        ask_price = product_metadata[keyshop_label]
    except KeyError:
        ask_price = 0

    return ask_price


def get_ask_prices_for_whole_bundle(price_metadata):
    ask_prices = {}

    for (slug, product_metadata) in price_metadata.items():
        ask_prices[slug] = get_ask_price_for_single_product(product_metadata)

    return ask_prices


def round_price(price):
    num_decimal_digits = 2
    return round(price, num_decimal_digits)


def get_bundle_value(ask_prices):
    total = sum(ask_prices.values())
    return round_price(total)


def split_bundle_cost(ask_prices, target_cost, verbose=True):
    bundle_value = get_bundle_value(ask_prices)
    cost_value_ratio = target_cost / bundle_value

    if verbose:
        total = get_bundle_value(ask_prices)
        print(f"Bundle value: {total:.2f} {get_currency_symbol()}")

    split_prices = {}

    for (slug, ask) in ask_prices.items():
        split_price = ask * cost_value_ratio
        split_prices[slug] = round_price(split_price)

    if verbose:
        total = get_bundle_value(split_prices)
        print(f"Bundle cost: {total:.2f} {get_currency_symbol()}")

    return split_prices
