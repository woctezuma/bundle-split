import pathlib

from src.trim_utils import strip_noisy_character


def get_data_folder() -> str:
    data_folder = "data/"
    pathlib.Path(data_folder).mkdir(exist_ok=True)
    return data_folder


def get_json_file_extension() -> str:
    return ".json"


def get_file_path(base_fname: str) -> str:
    base_fname = strip_noisy_character(base_fname)
    return get_data_folder() + base_fname + get_json_file_extension()


def get_bundle_fname(bundle_slug: str) -> str:
    return get_file_path(base_fname=bundle_slug)


def get_price_fname(bundle_slug: str) -> str:
    return get_file_path(base_fname=f"prices_{bundle_slug}")


def get_tier_fname(bundle_slug: str) -> str:
    return get_file_path(base_fname=f"tiers_{bundle_slug}")
