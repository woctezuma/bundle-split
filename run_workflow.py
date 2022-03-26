import list_bundle_content
import list_product_prices
import split_bundle_cost


def main(bundle_slug, target_cost_in_euros):
    list_bundle_content.main(bundle_slug)
    list_product_prices.main(bundle_slug)
    split_bundle_cost.main(bundle_slug, target_cost_in_euros)

    return True


if __name__ == "__main__":
    bundle_slug = "humble-choice-march-2022"
    target_cost_in_euros = 9.99
    main(bundle_slug, target_cost_in_euros)
