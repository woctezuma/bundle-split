def strip_price_text(price_text):
    noisy_symbol = "~"
    currency_symbol = "€"

    price_text = price_text.strip(noisy_symbol)
    price_text = price_text.split(currency_symbol)[0]

    return price_text


def fix_decimal_convention(price_text):
    return price_text.replace(",", ".")


def convert_to_float(price_text):
    try:
        price = float(price_text)
    except ValueError:
        price = None

    return price


def parse_price(price_text):
    price_text = strip_price_text(price_text)
    price_text = fix_decimal_convention(price_text)
    return convert_to_float(price_text)
