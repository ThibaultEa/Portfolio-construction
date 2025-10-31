import pandas as pd
import numpy as np
import datetime


class FinData():
    def __init__(self, raw_data: pd.DataFrame):
        self.donnees = raw_data.copy()
        self.start_date = min(raw_data.index)
        self.end_date = max(raw_data.index)
        self.volume = self.get_volume()
        self.prices = self.get_prices()
        self.log_returns = self.get_log_returns()
    
    # Calculs à l'initialisation
    def get_log_returns(self):
        return np.log(self.prices/self.prices.shift(1))
    
    def get_volume(self):
        return self.donnees.xs('volume', level=1, axis=1)
    
    def get_prices(self):
        return self.donnees.drop('volume', level=1, axis=1).ffill()

    # Calculs des linear returns et des stds
    def perfs_histo(self, start_date: datetime.date = None, end_date: datetime.date = None):
        if not start_date:
            start_date=self.start_date
        if not end_date:
            end_date=self.end_date
        linear_returns = (np.exp(self.log_returns.loc[start_date: end_date].sum(axis=0))-1) * 100

        return pd.Series(linear_returns, name='perf')
    
    def vol_histo(self, start_date: datetime.date = None, end_date: datetime.date = None):
        if not start_date:
            start_date=self.start_date
        if not end_date:
            end_date=self.end_date
        vols = self.prices.loc[start_date: end_date].std()
        return pd.Series(vols, name='vol')