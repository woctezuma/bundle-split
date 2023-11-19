def get_class(elem: dict[str, list]) -> list:
    try:
        cl = elem["class"]
    except KeyError:
        cl = []

    return cl


def get_id(elem: dict[str, str]) -> str:
    try:
        elem_id = elem["id"]
    except KeyError:
        elem_id = ""

    return elem_id


def get_content(elem) -> list[str]:
    content = elem.contents
    return filter_content(content)


def safe_strip(elem: str) -> str:
    try:
        stripped_elem = elem.strip()
    except TypeError:
        stripped_elem = elem

    return stripped_elem


def filter_content(data: list[str]) -> list[str]:
    filtered_data = []

    for elem in data:
        stripped_elem = safe_strip(elem)

        if len(stripped_elem) > 0:
            filtered_data.append(stripped_elem)

    return filtered_data


def filter_price_items(price_items: list[dict[str, list]]) -> list[dict[str, list]]:
    target_class = "game-price-anchor-link"
    return [elem for elem in price_items if target_class in get_class(elem)]
