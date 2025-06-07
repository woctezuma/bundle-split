from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bs4 import Tag


def get_class(elem: dict) -> list[str]:
    return elem.get("class", [])


def get_id(elem: dict[str, str]) -> str:
    return elem.get("id", "")


def get_content(elem: Tag) -> list[str]:
    content = elem.contents
    return filter_content(content)


def safe_strip(elem: str) -> str:
    try:
        stripped_elem = elem.strip()
    except TypeError:
        stripped_elem = elem

    return stripped_elem


def filter_content(data: list[str]) -> list[str]:
    return [stripped for elem in data if (stripped := safe_strip(elem))]


def filter_price_items(price_items: list) -> list:
    target_class = "game-price-anchor-link"
    return [elem for elem in price_items if target_class in get_class(elem)]
