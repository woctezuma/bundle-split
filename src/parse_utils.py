from contextlib import suppress
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bs4 import Tag


def get_currency_symbol() -> str:
    return "€"


def strip_price_text(price_text: str) -> str:
    noisy_symbol = "~"
    currency_symbol = get_currency_symbol()

    price_text = price_text.strip(noisy_symbol)
    return price_text.split(currency_symbol)[0]


def fix_decimal_convention(price_text: str) -> str:
    return price_text.replace(",", ".")


def convert_to_float(price_text: str) -> float:
    try:
        price = float(price_text)
    except ValueError:
        price = 0

    return price


def parse_price(price_text: str) -> float:
    price_text = strip_price_text(price_text)
    price_text = fix_decimal_convention(price_text)
    return convert_to_float(price_text)


def parse_price_from_soup(price_soup: Tag) -> float:
    price_text = price_soup.text
    return parse_price(price_text)


def get_value_from_soups(soup_list: list, key: str) -> str | None:
    value = None

    for soup in soup_list:
        # NB: A soup is not a dictionary: you cannot check `if key in soup`. A possible solution would involve:
        # - either checking `if soup.has_attr(key)`
        # - or duck-typing via try/except.

        with suppress(KeyError):
            value = soup[key]
            break

    return value
