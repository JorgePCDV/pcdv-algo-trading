# region imports
from AlgorithmImports import *
# endregion

class BacktestingAndPerformanceAnalysis(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2018, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.bnd = self.AddEquity("BND", Resolution.Daily).Symbol
        
        length = self.GetParameter("sma_length")
        length = 30 if length is None else int(length)

        self.sma = self.SMA(self.spy, length, Resolution.Daily)
        self.rebalanceTime = datetime.min
        self.uptrend = True
        
    def OnData(self, data: Slice):
        if not self.sma.IsReady or self.spy not in data or self.bnd not in data:
            return
        
        # uncomment to compare with SPY buy and hold strategy
        # self.SetHoldings(self.spy, 1)
        # return
        
        if data[self.spy].Price >= self.sma.Current.Value:
            if self.Time >= self.rebalanceTime or not self.uptrend:
                self.SetHoldings(self.spy, 0.8)
                self.SetHoldings(self.bnd, 0.2)
                self.uptrend = True
                self.rebalanceTime = self.Time + timedelta(30)
        elif self.Time >= self.rebalanceTime or self.uptrend:
            self.SetHoldings(self.spy, 0.2)
            self.SetHoldings(self.bnd, 0.8)
            self.uptrend = False
            self.rebalanceTime = self.Time + timedelta(30)

        self.Plot("Benchmark", "SMA", self.sma.Current.Value)
