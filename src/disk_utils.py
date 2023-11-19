import json
from pathlib import Path

from src.data_utils import get_bundle_fname, get_price_fname, get_tier_fname


def save_json(data: dict | list, fname: str) -> None:
    with Path(fname).open("w", encoding="utf-8") as f:
        json.dump(data, f)


def load_json_as_dict(fname: str) -> dict:
    try:
        with Path(fname).open(encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    return data


def load_json_as_list(fname: str) -> list:
    try:
        with Path(fname).open(encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    return data


def load_bundle_from_disk(bundle_slug: str) -> dict[str, dict[str, str]]:
    fname = get_bundle_fname(bundle_slug)
    return load_json_as_dict(fname)


def save_bundle_to_disk(
    data: dict[str | None, dict[str, str | None]],
    bundle_slug: str,
) -> None:
    fname = get_bundle_fname(bundle_slug)

    # Overwrite previous data
    save_json(data, fname)


def load_prices_from_disk(bundle_slug: str) -> dict[str, dict[str, float]]:
    fname = get_price_fname(bundle_slug)
    return load_json_as_dict(fname)


def save_prices_to_disk(data: dict[str, dict[str, float]], bundle_slug: str) -> None:
    fname = get_price_fname(bundle_slug)

    # Update previous data
    # Reference: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    updated_data = load_prices_from_disk(bundle_slug)
    updated_data |= data

    save_json(updated_data, fname)


def load_tiers_from_disk(bundle_slug: str) -> list[float]:
    fname = get_tier_fname(bundle_slug)
    return load_json_as_list(fname)


def save_tiers_to_disk(data: list[float], bundle_slug: str) -> None:
    fname = get_tier_fname(bundle_slug)

    # Overwrite previous data
    save_json(data, fname)
