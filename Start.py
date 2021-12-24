import asyncio
import tinvest
import yaml
from typing import Union, cast
import pathlib
import logging
import json

_root = pathlib.Path(__file__).parents[1]

def _load_config() -> dict[str, Union[int, float, str]]:
    cfg = {}
    path = _root / "tinvest" / "config" / "config.yaml"

    if path.exists():
        with path.open() as file:
            cfg = yaml.safe_load(file)
    logging.getLogger("Config").info(f"{cfg}")
    return cfg


def write_yaml(portfolio_tickers, portfolio_currencies):
    ticker_list = {}
    portfolio_tickers_string = json.loads(portfolio_tickers)
    portfolio_currencies_string = json.loads(portfolio_currencies)

    for item in portfolio_tickers_string["payload"]["positions"]:
        if (item["instrument_type"] != "Currency"):
            ticker_list[item["ticker"]] = item["balance"]

    for item in portfolio_currencies_string["payload"]["currencies"]:
        ticker_list[item["currency"]] = item["balance"]

    return ticker_list

async def main():
    portfolio_list = {}

    _cfg = _load_config()
    TOKEN = cast(str, _cfg.get("TOKEN", "none"))
    PORTFOLIO_TYPE = cast(str, _cfg.get("PORTFOLIO_TYPE", "none"))

    client = tinvest.AsyncClient(TOKEN)
    brokerAcc = await client.get_accounts()

    json_string = json.loads(brokerAcc.json())
    for item in json_string["payload"]["accounts"]:
        portfolio_list[item["broker_account_type"]] = item["broker_account_id"]

    tinkoff_IIS = int(portfolio_list[PORTFOLIO_TYPE])
    portfolio_tickers = await client.get_portfolio(broker_account_id=tinkoff_IIS)
    portfolio_currencies = await client.get_portfolio_currencies(broker_account_id=tinkoff_IIS)

    await client.close()

    ticker_list = write_yaml(portfolio_tickers.json(), portfolio_currencies.json())

    return ticker_list

ticker_list = asyncio.run(main())

print(ticker_list)


