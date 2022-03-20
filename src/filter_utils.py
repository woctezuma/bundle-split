def get_class(elem):
    try:
        cl = elem["class"]
    except KeyError:
        cl = []

    return cl


def get_content(elem):
    content = elem.contents
    filtered_content = filter_content(content)

    return filtered_content


def filter_content(data):
    filtered_data = []

    for elem in data:

        try:
            stripped_elem = elem.strip()
        except TypeError:
            stripped_elem = elem

        if len(stripped_elem) > 0:
            filtered_data.append(stripped_elem)

    return filtered_data
