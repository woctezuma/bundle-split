# Bundle Split

[![Build status with Github Action][build-image-action]][build-action]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

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

Alternatively, to execute the complete workflow, run:

```bash
python run_workflow.py 
```

## References

- Group Buys: [a Steam group][grbu-steam-group] for splitting bundle content,
- GG.deals: [the web page][ggdeals-bundle-page] for "Humble Stand with Ukraine Bundle".

<!-- Definitions -->

[build-action]: <https://github.com/woctezuma/bundle-split/actions>
[build-image-action]: <https://github.com/woctezuma/bundle-split/workflows/Python application/badge.svg?branch=main>

[codecov]: <https://codecov.io/gh/woctezuma/bundle-split>
[codecov-image]: <https://codecov.io/gh/woctezuma/bundle-split/branch/main/graph/badge.svg>

[codacy]: <https://www.codacy.com/gh/woctezuma/bundle-split>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/6f681c0f05e94799a83c68105fce8558>

[ggdeals-landing-page]: <https://gg.deals/>
[python-download]: <https://www.python.org/downloads/>
[grbu-steam-group]: <https://steamcommunity.com/groups/groupbuys/discussions/14/>
[ggdeals-bundle-page]: <https://gg.deals/bundle/humble-stand-with-ukraine-bundle/>
