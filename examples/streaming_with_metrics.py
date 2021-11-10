"""Streaming.

    python -m examples.streaming_with_metrics
"""
import asyncio

from pydantic import BaseSettings

import tinvest as ti
from tinvest.metrics import (
    collect_client_metrics,
    collect_streaming_metrics,
    run_metrics_server,
)


class Config(BaseSettings):
    TOKEN: str
    SANDBOX_TOKEN: str

    class Config:
        env_prefix = 'TINVEST_'


config = Config()


async def main() -> None:
    await run_metrics_server()
    client = ti.AsyncClient(config.TOKEN)
    collect_client_metrics(client)
    try:
        async with ti.Streaming(config.TOKEN) as streaming:
            collect_streaming_metrics(streaming)
            await streaming.candle.subscribe('BBG0013HGFT4', ti.CandleResolution.min1)
            await streaming.orderbook.subscribe('BBG0013HGFT4', 5)
            await streaming.instrument_info.subscribe('BBG0013HGFT4')
            async for event in streaming:
                if event.event == 'instrument_info':
                    r = await client.get_market_search_by_figi(event.payload.figi)
                    print(r)  # noqa:T001
                print(event)  # noqa:T001
    finally:
        await client.close()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
