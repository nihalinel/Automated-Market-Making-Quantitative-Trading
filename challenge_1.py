from AmplifyQuantTrading import Data, Exchange, MarketMaker, HedgeFund as hf
from matplotlib import pyplot as plt

# Retrieve market data
prices = Data.get_price_series("PricestoFeedserver")
price_requests = Data.get_price_requests("PriceRequeststoFeedserver")

test_requests = [price_requests[i] for i in range(10)]

# Match requests with prices
request_with_prices = [(req, price[2]) for price in prices for req in test_requests if req[0] == price[0] and req[1] == price[1]]

class QuotedTrade:
    def __init__(self, ticker, trade_volume, ref_price, bid_price, offer_price, date):
        self.ticker = ticker
        self.trade_volume = trade_volume
        self.ref_price = ref_price
        self.bid_price = bid_price
        self.offer_price = offer_price
        self.date = date

# Generate quoted trades
quoted_trades = []
for matched in request_with_prices:
    bid_price = matched[1] * 0.98
    offer_price = matched[1] * 1.02
    quote = QuotedTrade(matched[0][0], matched[0][2], matched[1], bid_price, offer_price, matched[0][1])
    quoted_trades.append(quote)

# Hedge Fund Responses
hf_responses = []
for trade in quoted_trades:
    response = hf.show(trade)
    hf_responses.append(response)

# Market Maker handling
mm = MarketMaker.mm()
for quote in quoted_trades:
    mm.add_quoted_trade(quote)

# Completed Trades
class CompletedTrade:
    def __init__(self, ticker, trade_volume, trade_price, mm_action, ref_price, bid_price, offer_price, date):
        self.ticker = ticker
        self.trade_volume = trade_volume
        self.trade_price = trade_price
        self.mm_action = mm_action
        self.ref_price = ref_price
        self.bid_price = bid_price
        self.offer_price = offer_price
        self.date = date

for response in hf_responses:
    if response.hf_action == "buy":
        mm_action = "sell"
    elif response.hf_action == "sell":
        mm_action = "buy"
    else:
        mm_action = "refuse"

    trade = CompletedTrade(response.ticker, response.trade_volume, response.trade_price, mm_action, response.ref_price, response.bid_price, response.offer_price, response.date)
    mm.add_trade(trade)

# Visualization
bid_data, offer_data, quote_dates = [], [], []
for trade in mm.completed_trades:
    if trade.ticker == "AAPL":
        bid_data.append(trade.bid_price)
        offer_data.append(trade.offer_price)
        quote_dates.append(trade.date)

ref_data, ref_dates = [], []
for price in prices:
    if price[0] == "AAPL" and price[1] <= quote_dates[-1]:
        ref_data.append(price[2])
        ref_dates.append(price[1])

plt.plot(quote_dates, bid_data, label="Bid Prices")
plt.plot(quote_dates, offer_data, label="Offer Prices")
plt.plot(ref_dates, ref_data, label="Reference Prices")
plt.legend()
plt.show()
