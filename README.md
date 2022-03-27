![Supported Python Versions](https://img.shields.io/static/v1?label=python&message=>=3.7&color=green)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vintasoftware/marilyn-api/master/LICENSE)
[![Downloads](https://pepy.tech/badge/marilyn-api)](https://pepy.tech/project/marilyn-api)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>


# Async client for Marilyn API


## Installation
    
    pip install marilyn-api

## Examples

```python
from marilyn_api import AsyncClient

api_root = "https://app.mymarilyn.ru"
headers = {
    "X-API-Account": 100500,
    "X-API-Token": "{auth token}",
}
aclient = AsyncClient(api_root, headers=headers)

body = {
    "channel_id": [],
    "start_date": "2022-02-01",
    "end_date": "2022-02-18",
    "date_grouping": "day",
    "grouping": "placement",
    "filtering": [
        {
            "entity": "no",
            "entities": []
        },
        {
            "entity": "project",
            "entities": [
                4551
            ]
        }
    ],
    "custom_metrics": [],
    "profiles": [],
    "goals": [],
    "with_vat": False,
    "per_page": 200,
    "sorting": "date",
    "columns": [
        "date",
        "placement_id",
        "placement_name",
        "campaign_xid",
        "channel_id",
        "impressions",
        "clicks",
        "cpm_fact",
        "reach_total_sum",
        "viral_reach_total_sum",
        "ctr",
        "cost_fact",
        "cpc_fact",
        "orders",
        "model_orders",
        "revenue",
        "revenue_model_orders"
    ]
}

async for page in aclient.iter_statistics_detailed(body):
    for item in page["items"]:
        print("RECORD:", item)

```

## Script examples

```bash
python Examples/statistics_detailed.py --help
python Examples/statistics_detailed.py -r https://app.mymarilyn.ru -a 100500 -t MytoKeN12345 -c Examples/detailed-stats-config.json
```

```bash
python Examples/project_placements.py.py --help
python Examples/project_placements.py.py -r https://app.mymarilyn.ru -a 100500 -p 12345 -t MytoKeN12345
```

## Dependencies
- aiohttp

## Author
Pavel Maksimov

You can contact me at
[Telegram](https://teleg.run/pavel_maksimow)

Удачи тебе, друг! Поставь звездочку ;)