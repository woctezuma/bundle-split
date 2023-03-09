NOISY_CHARACTER = "/"
URL_SEPARATOR = "/"


def strip_noisy_character(base_fname):
    return base_fname.removesuffix(NOISY_CHARACTER)


def get_non_empty_tokens(tokens):
    return [t for t in tokens if len(t) > 0]


def standardize_bundle_slug(slug_or_url):
    tokens = slug_or_url.split(URL_SEPARATOR)
    bundle_slug = get_non_empty_tokens(tokens)[-1]
    return bundle_slug
