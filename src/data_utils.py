import pathlib


def get_data_folder():
    data_folder = "data/"
    pathlib.Path(data_folder).mkdir(exist_ok=True)
    return data_folder


def get_json_file_extension():
    return ".json"


def get_file_path(base_fname):
    return get_data_folder() + base_fname + get_json_file_extension()


def get_bundle_fname(bundle_slug):
    return get_file_path(base_fname=bundle_slug)


def get_price_fname(bundle_slug):
    return get_file_path(base_fname=f"prices_{bundle_slug}")


def get_tier_fname(bundle_slug):
    return get_file_path(base_fname=f"tiers_{bundle_slug}")
