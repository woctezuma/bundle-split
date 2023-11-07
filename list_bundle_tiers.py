from src.tier_utils import fetch_tiers


def main():
    for bundle_slug in (
        "humble-survival-instinct-bundle",  # 1 tier
        "humble-fighting-farmers-bundle",  # 2 tiers
        "humble-game-bundle-in-case-you-missed-it-gems-of-2022",  # 3 tiers
    ):
        tier_prices = fetch_tiers(bundle_slug)

    return True


if __name__ == "__main__":
    main()
