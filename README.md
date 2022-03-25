# Bundle Split

This repository contains Python code to:
- fetch bundle content from [GG.deals][ggdeals-landing-page],
- then price bundle split based on prices at keyshop resellers.

## Requirements

- Install the latest version of [Python 3.X][python-download].
- Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1) To fetch bundle content, run:

```bash
python list_bundle_content.py 
```

2) To fetch product prices, run:

```bash
python list_product_prices.py 
```

3) To split bundle cost, run:

```bash
python split_bundle_cost.py 
```

## References

- Group Buys: [a Steam group][grbu-steam-group] for splitting bundle content,
- GG.deals: [the web page][ggdeals-bundle-page] for "Humble Stand with Ukraine Bundle".

<!-- Definitions -->

[ggdeals-landing-page]: <https://gg.deals/>
[python-download]: <https://www.python.org/downloads/>
[grbu-steam-group]: <https://steamcommunity.com/groups/groupbuys/discussions/14/>
[ggdeals-bundle-page]: <https://gg.deals/bundle/humble-stand-with-ukraine-bundle/>
