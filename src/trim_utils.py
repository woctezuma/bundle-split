NOISY_CHARACTER = "/"


def strip_noisy_character(base_fname):
    return base_fname.removesuffix(NOISY_CHARACTER)
