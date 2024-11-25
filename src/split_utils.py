from src.parse_utils import get_currency_symbol


def get_keyshop_label() -> str:
    return "#keyshops"


def get_ask_price_for_single_product(product_metadata: dict[str, float]) -> float:
    keyshop_label = get_keyshop_label()
    return product_metadata.get(keyshop_label, 0)


def get_ask_prices_for_whole_bundle(
    price_metadata: dict[str, dict[str, float]],
) -> dict[str, float]:
    return {
        slug: get_ask_price_for_single_product(product_metadata)
        for slug, product_metadata in price_metadata.items()
    }


def round_price_to_the_closest_cent(price: float) -> float:
    num_decimal_digits = 2
    return round(price, num_decimal_digits)


def round_price_to_multiple_of_delta(price: float, delta: float = 0.05) -> float:
    return delta * round(price / delta)


def get_bundle_value(ask_prices: dict[str, float]) -> float:
    total = sum(ask_prices.values())
    return round_price_to_the_closest_cent(total)


def split_bundle_cost(
    ask_prices: dict[str, float],
    target_cost: float,
    *,
    verbose: bool = True,
) -> dict[str, float]:
    bundle_value = get_bundle_value(ask_prices)
    cost_value_ratio = target_cost / bundle_value

    if verbose:
        total = get_bundle_value(ask_prices)
        print(f"Bundle value: {total:.2f} {get_currency_symbol()}")

    split_prices: dict[str, float] = {
        slug: round_price_to_multiple_of_delta(ask * cost_value_ratio)
        for slug, ask in ask_prices.items()
    }

    if verbose:
        total = get_bundle_value(split_prices)
        print(f"Bundle cost: {total:.2f} {get_currency_symbol()}")

    return split_prices
