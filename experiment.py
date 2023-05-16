
# %%
import argparse
import os
from time import time

#import ray
import pandas as pd
from statsforecast.utils import generate_series
from statsforecast.models import ETS
from statsforecast.core import StatsForecast


for length in [1_00_000, 2_00_000]:
    print(f'length: {length}')
    series = generate_series(n_series=length, seed=1, equal_ends=True)
    print(series)
        # add constant to avoid numerical errors
        # in production settings we simply remove this constant
        # from the forecasts
    series['y'] += 10
    model = [
        ETS(season_length=7)
    ]
    sf = StatsForecast(
        df=series,
        models=model,
        freq='D', 
        n_jobs=-1
    )
    init = time()
    forecasts = sf.forecast(7)
    total_time = (time() - init) / 60
    print(f'n_series: {length} total time: {total_time}')


# %%
