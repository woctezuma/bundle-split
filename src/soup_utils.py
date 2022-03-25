from src.filter_utils import get_class, get_content, get_id


def extract_soup_items(soup, target_div, verbose=False):
    all_divs = soup.findAll("div")

    items = []

    for div_element in all_divs:
        div_classes = get_class(div_element)

        div_id = get_id(div_element)
        div_classes.append(div_id)

        if target_div in div_classes:
            new_items = get_content(div_element)

            items += new_items

            if verbose:
                print(f"div: {div_classes} -> {len(new_items)} items")

    return items
