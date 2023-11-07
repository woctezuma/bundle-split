import json
from pathlib import Path

from src.data_utils import get_bundle_fname, get_price_fname, get_tier_fname


def save_json(data, fname):
    with Path(fname).open("w", encoding="utf-8") as f:
        json.dump(data, f)
    return


def load_json(fname):
    try:
        with Path(fname).open(encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    return data


def load_bundle_from_disk(bundle_slug):
    fname = get_bundle_fname(bundle_slug)
    return load_json(fname)


def save_bundle_to_disk(data, bundle_slug):
    fname = get_bundle_fname(bundle_slug)

    # Overwrite previous data
    save_json(data, fname)

    return


def load_prices_from_disk(bundle_slug):
    fname = get_price_fname(bundle_slug)
    return load_json(fname)


def save_prices_to_disk(data, bundle_slug):
    fname = get_price_fname(bundle_slug)

    # Update previous data
    # Reference: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    updated_data = load_prices_from_disk(bundle_slug)
    updated_data |= data

    save_json(updated_data, fname)

    return


def load_tiers_from_disk(bundle_slug):
    fname = get_tier_fname(bundle_slug)
    return load_json(fname)


def save_tiers_to_disk(data, bundle_slug):
    fname = get_tier_fname(bundle_slug)

    # Overwrite previous data
    save_json(data, fname)

    return
