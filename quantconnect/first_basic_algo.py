# region imports
from AlgorithmImports import *
# endregion

class FirstBasicAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 9, 23)  # Set Start Date
        self.SetEndDate(2021, 1, 1)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash

        spy = self.AddEquity("SPY", Resolution.Daily)
        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)

        self.spy = spy.Symbol

        self.SetBenchmark("SPY")
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)

        self.entryPrice = 0
        self.period = timedelta(2)
        self.nextEntryTime = self.Time

    def OnData(self, data: Slice):
        if not self.spy in data:
            return
        
        # Different ways of obtaining Close price
        # price = data.Bars[self.spy].Close
        price = data[self.spy].Close
        # price = self.Securities[self.spy].Close

        if not self.Portfolio.Invested:
            if self.nextEntryTime <= self.Time:
                self.SetHoldings(self.spy, 1)
                # self.MarketOrder(self.spy, int(self.Portfolio.Cash / price))
                self.Log("BUY SPY @" + str(price))
                self.entryPrice = price
        elif self.entryPrice * 1.1 < price or self.entryPrice * 0.9 > price:
            self.Liquidate()
            self.Log("SELL SPY @" + str(price))
            self.nextEntryTime = self.Time + self.period
