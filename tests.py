from unittest import TestCase

from src.fetch_utils import fetch_product_page_with_given_href
from src.soup_prices import extract_metadata_for_all_prices, extract_price_items


class TestSoupUtilsMethods(TestCase):
    @staticmethod
    def test_price_of_unreleased_product() -> None:
        # This tests what happens when prices are marked as "Unavailable".
        # Reference: https://gg.deals/game/in-the-valley-of-gods/
        href = "/game/in-the-valley-of-gods/"
        page_soup = fetch_product_page_with_given_href(product_href=href)

        price_items = extract_price_items(page_soup=page_soup)
        metadata = extract_metadata_for_all_prices(price_items=price_items)

        assert not metadata
