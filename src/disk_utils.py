import json
from pathlib import Path
from typing import TypeVar

from src.data_utils import get_bundle_fname, get_price_fname, get_tier_fname

T = TypeVar("T", dict, list)


def save_json(data: T, fname: str) -> None:
    with Path(fname).open("w", encoding="utf-8") as f:
        json.dump(data, f)


def load_json(fname: str, default_factory: type[T]) -> T:
    try:
        with Path(fname).open(encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = default_factory()

    return data


def load_bundle_from_disk(bundle_slug: str) -> dict[str, dict[str, str | None]]:
    fname = get_bundle_fname(bundle_slug)
    return load_json(fname, dict)


def save_bundle_to_disk(
    data: dict[str | None, dict[str, str | None]],
    bundle_slug: str,
) -> None:
    fname = get_bundle_fname(bundle_slug)

    # Overwrite previous data
    save_json(data, fname)


def load_prices_from_disk(bundle_slug: str) -> dict[str, dict[str, float]]:
    fname = get_price_fname(bundle_slug)
    return load_json(fname, dict)


def save_prices_to_disk(data: dict[str, dict[str, float]], bundle_slug: str) -> None:
    fname = get_price_fname(bundle_slug)

    # Update previous data
    # Reference: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    updated_data = load_prices_from_disk(bundle_slug)
    updated_data |= data

    save_json(updated_data, fname)


def load_tiers_from_disk(bundle_slug: str) -> list[float]:
    fname = get_tier_fname(bundle_slug)
    return load_json(fname, list)


def save_tiers_to_disk(data: list[float], bundle_slug: str) -> None:
    fname = get_tier_fname(bundle_slug)

    # Overwrite previous data
    save_json(data, fname)
