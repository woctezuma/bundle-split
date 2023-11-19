NOISY_CHARACTER: str = "/"
URL_SEPARATOR: str = "/"


def strip_noisy_character(base_fname: str) -> str:
    return base_fname.removesuffix(NOISY_CHARACTER)


def get_non_empty_tokens(tokens: list[str]) -> list[str]:
    return [t for t in tokens if len(t) > 0]


def standardize_bundle_slug(slug_or_url: str) -> str:
    tokens = slug_or_url.split(URL_SEPARATOR)
    return get_non_empty_tokens(tokens)[-1]
