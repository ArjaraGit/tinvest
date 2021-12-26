import asyncio
import tinvest
import yaml
from typing import Union, cast
import pathlib
import logging
import json
import os

_root = pathlib.Path(__file__).parents[1]

def load_from_poptimazer_yaml():
    path = _root / "poptimizer" / "poptimizer" / "portfolio" / "base.yaml"
    with open(path) as file:
        base_ticker_list = yaml.load(file, Loader=yaml.FullLoader)
    return base_ticker_list

def _load_config() -> dict[str, Union[int, float, str]]:
    cfg = {}
    path = _root / "tinvest" / "config_tinvest" / "config.yaml"

    if path.exists():
        with path.open() as file:
            cfg = yaml.safe_load(file)
    logging.getLogger("Config").info(f"{cfg}")
    return cfg

def json_to_dict(portfolio_tickers, portfolio_currencies):
    ticker_list = {}
    portfolio_tickers_string = json.loads(portfolio_tickers)
    portfolio_currencies_string = json.loads(portfolio_currencies)

    for item in portfolio_tickers_string["positions"]:
        if (item["instrument_type"] != "Currency"):
            ticker_list[item["ticker"]] = item["balance"]

    for item in portfolio_currencies_string["currencies"]:
        ticker_list[item["currency"]] = item["balance"]

    return ticker_list

def write_to_yaml(allTickersByAcc):
    positions = {}
    positionsRM = {}
    my_tickers = {}
    my_tickers_list = {}

    main_path = _root / "poptimizer" / "poptimizer" / "portfolio"
    for file in os.listdir(main_path):
        if file != "base.yaml":
            os.remove(main_path / file)

    for acc_name in allTickersByAcc:
        base_ticker_list = load_from_poptimazer_yaml()
        positions_base = base_ticker_list["positions"]
        path = main_path

        for ticker, value in positions_base.items():
            if "-RM" in ticker:
                positionsRM[ticker.replace("-RM", "")] = value
            else:
                positions[ticker] = value

        for ticker, value in positionsRM.items():
            if ticker in allTickersByAcc[acc_name]:
                positionsRM[ticker] = allTickersByAcc[acc_name][ticker]
        for ticker, value in positions.items():
            if ticker in allTickersByAcc[acc_name]:
                positions[ticker] = allTickersByAcc[acc_name][ticker]

        for ticker, value in positionsRM.items():
            positions_base[ticker + "-RM"] = int(positionsRM[ticker])

        for ticker, value in positions.items():
            positions_base[ticker] = int(positions[ticker])

        base_ticker_list["RUR"] = int(allTickersByAcc[acc_name]["RUB"])
        base_ticker_list["USD"] = int(allTickersByAcc[acc_name]["USD"])

        for ticker, value in allTickersByAcc[acc_name].items():
            if (ticker not in positionsRM) and (ticker not in positions) and (ticker not in base_ticker_list):
                if (ticker == "RUB"):
                    if ("RUR" not in base_ticker_list):
                        my_tickers_list[ticker] = value
                else:
                    my_tickers_list[ticker] = value

        my_tickers[acc_name] = my_tickers_list.copy()

        positionsRM.clear()
        positions.clear()
        my_tickers_list.clear()

        acc_name = acc_name + ".yaml"
        path = path / acc_name

        with open(path, 'w') as file:
            documents = yaml.dump(base_ticker_list, file)

    print()
    print("=====================================================================================")
    print("Бумаги из портфеля {}, которых нет в base.yaml:".format(acc_name.replace(".yaml", "")))
    for acc_name, acc_ticker_list in my_tickers.items():
        for ticker, value in acc_ticker_list.items():
            if value != 0:
                print("\t{} - \t{}: \t{}".format(acc_name, ticker, int(value)))
    print("=====================================================================================")

async def main():
    portfolio_list = {}
    allTickersByAcc = {}

    _cfg = _load_config()
    TOKEN = cast(str, _cfg.get("TOKEN", "none"))
    PORTFOLIO_TYPE = cast(str, _cfg.get("PORTFOLIO_TYPE", "none"))

    if TOKEN == "none":
        print("В конфиге не прописан токен")
    else:
        client = tinvest.AsyncClient(TOKEN)
        brokerAcc = await client.get_accounts()

        json_string = json.loads(brokerAcc.json())
        for item in json_string["payload"]["accounts"]:
            portfolio_list[item["broker_account_type"]] = item["broker_account_id"]

        if PORTFOLIO_TYPE in portfolio_list:
            portfolio_list = {PORTFOLIO_TYPE: portfolio_list[PORTFOLIO_TYPE]}

        for name, acc in portfolio_list.items():
            portfolio_tickers = await client.get_portfolio(broker_account_id=int(acc))
            portfolio_currencies = await client.get_portfolio_currencies(broker_account_id=int(acc))

            if "positions" in portfolio_tickers.payload.json():
                portfolio_tickers = portfolio_tickers.payload.json()

            if "currencies" in portfolio_currencies.payload.json():
                portfolio_currencies = portfolio_currencies.payload.json()

            ticker_list = json_to_dict(portfolio_tickers, portfolio_currencies)
            allTickersByAcc[name] = ticker_list

        await client.close()
    return allTickersByAcc

write_to_yaml(asyncio.run(main()))


