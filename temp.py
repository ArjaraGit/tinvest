import json
from typing import Union, cast

myJsonStr = '{"payload": {"positions": [{"name": "\u0418\u0421\u041a\u0427", "average_position_price": {"currency": "RUB", "value": 122.75}, "average_position_price_no_nkd": null, "balance": 40.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": -85.9}, "figi": "BBG000N16BP3", "instrument_type": "Stock", "isin": "RU000A0JNAB6", "lots": 4, "ticker": "ISKJ"}, {"name": "\u0420\u0443\u0441\u0410\u0433\u0440\u043e", "average_position_price": {"currency": "RUB", "value": 1154}, "average_position_price_no_nkd": null, "balance": 6, "blocked": null, "expected_yield": {"currency": "RUB", "value": 10.0}, "figi": "BBG007N0Z367", "instrument_type": "Stock", "isin": "US7496552057", "lots": 6, "ticker": "AGRO"}, {"name": "\u0424\u0430\u0440\u043c\u0441\u0438\u043d\u0442\u0435\u0437", "average_position_price": {"currency": "RUB", "value": 5.89}, "average_position_price_no_nkd": null, "balance": 1200.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": -277}, "figi": "BBG0019K04R5", "instrument_type": "Stock", "isin": "RU000A0JR514", "lots": 12, "ticker": "LIFE"}, {"name": "\u0413\u0430\u0437\u043f\u0440\u043e\u043c", "average_position_price": {"currency": "RUB", "value": 335.13}, "average_position_price_no_nkd": null, "balance": 50.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": 183}, "figi": "BBG004730RP0", "instrument_type": "Stock", "isin": "RU0007661625", "lots": 5, "ticker": "GAZP"}, {"name": "\u0414\u0412\u041c\u041f", "average_position_price": {"currency": "RUB", "value": 26.73}, "average_position_price_no_nkd": null, "balance": 400.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": -28}, "figi": "BBG000QF1Q17", "instrument_type": "Stock", "isin": "RU0008992318", "lots": 4, "ticker": "FESH"}, {"name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u0427\u0435\u0440\u043a\u0438\u0437\u043e\u0432\u043e", "average_position_price": {"currency": "RUB", "value": 2853.5}, "average_position_price_no_nkd": null, "balance": 2, "blocked": null, "expected_yield": {"currency": "RUB", "value": 16}, "figi": "BBG000RTHVK7", "instrument_type": "Stock", "isin": "RU000A0JL4R1", "lots": 2, "ticker": "GCHE"}, {"name": "\u0420\u043e\u0441\u043d\u0435\u0444\u0442\u044c", "average_position_price": {"currency": "RUB", "value": 576.95}, "average_position_price_no_nkd": null, "balance": 30.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": -147.6}, "figi": "BBG004731354", "instrument_type": "Stock", "isin": "RU000A0J2Q06", "lots": 30, "ticker": "ROSN"}, {"name": "TCS Group", "average_position_price": {"currency": "RUB", "value": 6993.6}, "average_position_price_no_nkd": null, "balance": 6, "blocked": null, "expected_yield": {"currency": "RUB", "value": -6010.8}, "figi": "BBG00QPYJ5H0", "instrument_type": "Stock", "isin": "TCS7238U2033", "lots": 6, "ticker": "TCSG"}, {"name": "Polymetal", "average_position_price": {"currency": "RUB", "value": 1435.5}, "average_position_price_no_nkd": null, "balance": 26, "blocked": null, "expected_yield": {"currency": "RUB", "value": -4339.3}, "figi": "BBG004PYF2N3", "instrument_type": "Stock", "isin": "JE00B6T5S470", "lots": 26, "ticker": "POLY"}, {"name": "\u041c\u0435\u0447\u0435\u043b - \u041f\u0440\u0438\u0432\u0438\u043b\u0435\u0433\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0430\u043a\u0446\u0438\u0438", "average_position_price": {"currency": "RUB", "value": 297.8}, "average_position_price_no_nkd": null, "balance": 10.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": 29.5}, "figi": "BBG004S68FR6", "instrument_type": "Stock", "isin": "RU000A0JPV70", "lots": 1, "ticker": "MTLRP"}, {"name": "\u0422\u0430\u0442\u043d\u0435\u0444\u0442\u044c", "average_position_price": {"currency": "RUB", "value": 489.9}, "average_position_price_no_nkd": null, "balance": 14, "blocked": null, "expected_yield": {"currency": "RUB", "value": -110.6}, "figi": "BBG004RVFFC0", "instrument_type": "Stock", "isin": "RU0009033591", "lots": 14, "ticker": "TATN"}, {"name": "Viatris Inc", "average_position_price": {"currency": "USD", "value": 13.07}, "average_position_price_no_nkd": null, "balance": 3, "blocked": null, "expected_yield": {"currency": "USD", "value": 1.59}, "figi": "BBG00Y4RQNH4", "instrument_type": "Stock", "isin": "US92556V1061", "lots": 3, "ticker": "VTRS"}, {"name": "American Airlines Group", "average_position_price": {"currency": "USD", "value": 17.67}, "average_position_price_no_nkd": null, "balance": 11, "blocked": null, "expected_yield": {"currency": "USD", "value": 6.24}, "figi": "BBG005P7Q881", "instrument_type": "Stock", "isin": "US02376R1023", "lots": 11, "ticker": "AAL"}, {"name": "\u041f\u043e\u043b\u044e\u0441 \u0417\u043e\u043b\u043e\u0442\u043e", "average_position_price": {"currency": "RUB", "value": 15644}, "average_position_price_no_nkd": null, "balance": 5, "blocked": null, "expected_yield": {"currency": "RUB", "value": -13170.0}, "figi": "BBG000R607Y3", "instrument_type": "Stock", "isin": "RU000A0JNAA8", "lots": 5, "ticker": "PLZL"}, {"name": "\u041f\u0418\u041a", "average_position_price": {"currency": "RUB", "value": 1103.7}, "average_position_price_no_nkd": null, "balance": 70.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": -7076.2}, "figi": "BBG004S68BH6", "instrument_type": "Stock", "isin": "RU000A0JP7J7", "lots": 70, "ticker": "PIKK"}, {"name": "\u0410\u0448\u0438\u043d\u0441\u043a\u0438\u0439 \u043c\u0435\u0442\u0437\u0430\u0432\u043e\u0434", "average_position_price": {"currency": "RUB", "value": 18.775}, "average_position_price_no_nkd": null, "balance": 900.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": -318.5}, "figi": "BBG000RJWGC4", "instrument_type": "Stock", "isin": "RU000A0B88G6", "lots": 9, "ticker": "AMEZ"}, {"name": "\u0412\u0422\u0411 \u041b\u0438\u043a\u0432\u0438\u0434\u043d\u043e\u0441\u0442\u044c", "average_position_price": {"currency": "RUB", "value": 1.0886}, "average_position_price_no_nkd": null, "balance": 38000.0, "blocked": null, "expected_yield": {"currency": "RUB", "value": 269.8}, "figi": "BBG00RPRPX12", "instrument_type": "Etf", "isin": "RU000A1014L8", "lots": 38000, "ticker": "VTBM"}, {"name": "\u0414\u043e\u043b\u043b\u0430\u0440 \u0421\u0428\u0410", "average_position_price": {"currency": "RUB", "value": 73.97}, "average_position_price_no_nkd": null, "balance": 0.33, "blocked": null, "expected_yield": {"currency": "RUB", "value": -0.11}, "figi": "BBG0013HGFT4", "instrument_type": "Currency", "isin": null, "lots": 0, "ticker": "USD000UTSTOM"}]}, "status": "Ok", "tracking_id": "865bd2e2e85a830f"}'

ticker_list = {}
json_string = json.loads(myJsonStr)

for item in json_string["payload"]["positions"]:
    if (item["instrument_type"] != "Currency"):
        ticker_list[item["ticker"]] = item["balance"]

print(ticker_list)




"""

{"payload": {
    "positions": [
        {
            "name": "\u0418\u0421\u041a\u0427",
            "average_position_price": {"currency": "RUB", 
                                       "value": 122.75}, 
            "average_position_price_no_nkd": null, 
            "balance": 40.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -85.9}, 
            "figi": "BBG000N16BP3", 
            "instrument_type": "Stock", 
            "isin": "RU000A0JNAB6", 
            "lots": 4, 
            "ticker": "ISKJ"
        }, 
        {
            "name": "\u0420\u0443\u0441\u0410\u0433\u0440\u043e", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 1154}, 
            "average_position_price_no_nkd": null, 
            "balance": 6, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": 10.0}, 
            "figi": "BBG007N0Z367", 
            "instrument_type": "Stock", 
            "isin": "US7496552057", 
            "lots": 6, 
            "ticker": "AGRO"
        }, 
        {
            "name": "\u0424\u0430\u0440\u043c\u0441\u0438\u043d\u0442\u0435\u0437", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 5.89}, 
            "average_position_price_no_nkd": null, 
            "balance": 1200.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -277}, 
            "figi": "BBG0019K04R5", 
            "instrument_type": "Stock", 
            "isin": "RU000A0JR514", 
            "lots": 12, 
            "ticker": "LIFE"
        }, 
        {
            "name": "\u0413\u0430\u0437\u043f\u0440\u043e\u043c", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 335.13}, 
            "average_position_price_no_nkd": null, 
            "balance": 50.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": 183}, 
            "figi": "BBG004730RP0", 
            "instrument_type": "Stock", 
            "isin": "RU0007661625", 
            "lots": 5, 
            "ticker": "GAZP"
        }, 
        {
            "name": "\u0414\u0412\u041c\u041f", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 26.73}, 
            "average_position_price_no_nkd": null, 
            "balance": 400.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -28}, 
            "figi": "BBG000QF1Q17", 
            "instrument_type": "Stock", 
            "isin": "RU0008992318", 
            "lots": 4, 
            "ticker": "FESH"
        }, 
        {
            "name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u0427\u0435\u0440\u043a\u0438\u0437\u043e\u0432\u043e", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 2853.5}, 
            "average_position_price_no_nkd": null, 
            "balance": 2, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": 16}, 
            "figi": "BBG000RTHVK7", 
            "instrument_type": "Stock", 
            "isin": "RU000A0JL4R1", 
            "lots": 2, 
            "ticker": "GCHE"
        }, 
        {
            "name": "\u0420\u043e\u0441\u043d\u0435\u0444\u0442\u044c", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 576.95}, 
            "average_position_price_no_nkd": null, 
            "balance": 30.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -147.6}, 
            "figi": "BBG004731354", 
            "instrument_type": "Stock", 
            "isin": "RU000A0J2Q06", 
            "lots": 30, 
            "ticker": "ROSN"
        }, 
        {
            "name": "TCS Group", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 6993.6}, 
            "average_position_price_no_nkd": null, 
            "balance": 6, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -6010.8}, 
            "figi": "BBG00QPYJ5H0", 
            "instrument_type": "Stock", 
            "isin": "TCS7238U2033", 
            "lots": 6, 
            "ticker": "TCSG"
        }, 
        {
            "name": "Polymetal", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 1435.5}, 
            "average_position_price_no_nkd": null, 
            "balance": 26, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -4339.3}, 
            "figi": "BBG004PYF2N3", 
            "instrument_type": "Stock", 
            "isin": "JE00B6T5S470", 
            "lots": 26, 
            "ticker": "POLY"
        }, 
        {
            "name": "\u041c\u0435\u0447\u0435\u043b - \u041f\u0440\u0438\u0432\u0438\u043b\u0435\u0433\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0430\u043a\u0446\u0438\u0438", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 297.8}, 
            "average_position_price_no_nkd": null, 
            "balance": 10.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": 29.5}, 
            "figi": "BBG004S68FR6", 
            "instrument_type": "Stock", 
            "isin": "RU000A0JPV70", 
            "lots": 1, 
            "ticker": "MTLRP"
        }, 
        {
            "name": "\u0422\u0430\u0442\u043d\u0435\u0444\u0442\u044c", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 489.9}, 
            "average_position_price_no_nkd": null, 
            "balance": 14, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -110.6}, 
            "figi": "BBG004RVFFC0", 
            "instrument_type": "Stock", 
            "isin": "RU0009033591", 
            "lots": 14, 
            "ticker": "TATN"
        }, 
        {
            "name": "Viatris Inc", 
            "average_position_price": {"currency": "USD", 
                                       "value": 13.07}, 
            "average_position_price_no_nkd": null, 
            "balance": 3, 
            "blocked": null, 
            "expected_yield": {"currency": "USD", 
                               "value": 1.59}, 
            "figi": "BBG00Y4RQNH4", 
            "instrument_type": "Stock", 
            "isin": "US92556V1061", 
            "lots": 3, 
            "ticker": "VTRS"
        }, 
        {
            "name": "American Airlines Group", 
            "average_position_price": {"currency": "USD", 
                                       "value": 17.67}, 
            "average_position_price_no_nkd": null, 
            "balance": 11, 
            "blocked": null, 
            "expected_yield": {"currency": "USD", 
                               "value": 6.24}, 
            "figi": "BBG005P7Q881", 
            "instrument_type": "Stock", 
            "isin": "US02376R1023", 
            "lots": 11, 
            "ticker": "AAL"
        }, 
        {
            "name": "\u041f\u043e\u043b\u044e\u0441 \u0417\u043e\u043b\u043e\u0442\u043e", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 15644}, 
            "average_position_price_no_nkd": null, 
            "balance": 5, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -13170.0}, 
            "figi": "BBG000R607Y3", 
            "instrument_type": "Stock", 
            "isin": "RU000A0JNAA8", 
            "lots": 5, 
            "ticker": "PLZL"
        }, 
        {
            "name": "\u041f\u0418\u041a", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 1103.7}, 
            "average_position_price_no_nkd": null, 
            "balance": 70.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -7076.2}, 
            "figi": "BBG004S68BH6", 
            "instrument_type": "Stock", 
            "isin": "RU000A0JP7J7", 
            "lots": 70, 
            "ticker": "PIKK"
        }, 
        {
            "name": "\u0410\u0448\u0438\u043d\u0441\u043a\u0438\u0439 \u043c\u0435\u0442\u0437\u0430\u0432\u043e\u0434", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 18.775}, 
            "average_position_price_no_nkd": null, 
            "balance": 900.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -318.5}, 
            "figi": "BBG000RJWGC4", 
            "instrument_type": "Stock", 
            "isin": "RU000A0B88G6", 
            "lots": 9, 
            "ticker": "AMEZ"
        }, 
        {
            "name": "\u0412\u0422\u0411 \u041b\u0438\u043a\u0432\u0438\u0434\u043d\u043e\u0441\u0442\u044c", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 1.0886}, 
            "average_position_price_no_nkd": null, 
            "balance": 38000.0, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": 269.8}, 
            "figi": "BBG00RPRPX12", 
            "instrument_type": "Etf", 
            "isin": "RU000A1014L8", 
            "lots": 38000, 
            "ticker": "VTBM"
        }, 
        {
            "name": "\u0414\u043e\u043b\u043b\u0430\u0440 \u0421\u0428\u0410", 
            "average_position_price": {"currency": "RUB", 
                                       "value": 73.97}, 
            "average_position_price_no_nkd": null, 
            "balance": 0.33, 
            "blocked": null, 
            "expected_yield": {"currency": "RUB", 
                               "value": -0.11}, 
            "figi": "BBG0013HGFT4", 
            "instrument_type": "Currency", 
            "isin": null, 
            "lots": 0, 
            "ticker": "USD000UTSTOM"
        }]
}, "status": "Ok", "tracking_id": "865bd2e2e85a830f"}

"""

