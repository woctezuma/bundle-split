from src.disk_utils import load_bundle_from_disk, save_prices_to_disk
from src.fetch_utils import fetch_product_page_with_given_href
from src.soup_utils import extract_price_items, extract_metadata_for_all_prices


def main():
    bundle_slug = "humble-stand-with-ukraine-bundle"
    bundle_metadata = load_bundle_from_disk(bundle_slug)

    price_metadata = {}

    for i, slug in enumerate(bundle_metadata, start=1):
        print(f"{i:02d}) {slug}")

        product = bundle_metadata[slug]
        page_soup = fetch_product_page_with_given_href(product_href=product["href"])

        price_items = extract_price_items(page_soup=page_soup)
        price_metadata[slug] = extract_metadata_for_all_prices(price_items=price_items)

    print(price_metadata)
    save_prices_to_disk(data=price_metadata)

    return True


if __name__ == "__main__":
    main()
