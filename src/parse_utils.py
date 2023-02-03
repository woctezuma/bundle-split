def get_currency_symbol():
    return "€"


def strip_price_text(price_text):
    noisy_symbol = "~"
    currency_symbol = get_currency_symbol()

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


def parse_price_from_soup(price_soup):
    price_text = price_soup.text
    return parse_price(price_text)


def get_value_from_soups(soup_list, key):
    value = None

    for soup in soup_list:
        # NB: A soup is not a dictionary: you cannot check `if key in soup`. A possible solution would involve:
        # - either checking `if soup.has_attr(key)`
        # - or duck-typing via try/except.

        try:
            value = soup[key]
            break
        except KeyError:
            pass

    return value
