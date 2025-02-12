from AmplifyQuantTrading import Data, Exchange, MarketMaker, HedgeFund as hf
from matplotlib import pyplot as plt

mm = MarketMaker.mm()

def calculate_spread(quote):
    volume = mm.current_positions[quote[0][0]].position_volume
    ref_price = quote[1]

    if volume > 0:
        bid_price = ref_price * 0.99
        offer_price = ref_price * 1.07
    elif volume < 0:
        bid_price = ref_price * 0.93
        offer_price = ref_price * 1.01
    else:
        bid_price = ref_price * 0.98
        offer_price = ref_price * 1.02

    trade = QuotedTrade(quote[0][0], quote[0][2], ref_price, bid_price, offer_price, quote[0][1])
    mm.add_quoted_trade(trade)
    return trade

def handle_response(trade):
    response = hf.show(trade)

    if response.hf_action == "buy":
        mm_action = "sell"
        trade_price = trade.offer_price
    elif response.hf_action == "sell":
        mm_action = "buy"
        trade_price = trade.bid_price
    else:
        mm_action = "refuse"
        trade_price = None

    completed_trade = CompletedTrade(trade.ticker, trade.trade_volume, trade_price, mm_action, trade.ref_price, trade.bid_price, trade.offer_price, trade.date)
    mm.add_trade(completed_trade)
    return completed_trade

ticker_data = {}
for trade in mm.completed_trades:
    if trade.ticker not in ticker_data:
        ticker_data[trade.ticker] = {"dates": [], "bid_prices": [], "offer_prices": [], "ref_prices": []}

    ticker_data[trade.ticker]["dates"].append(trade.date)
    ticker_data[trade.ticker]["bid_prices"].append(trade.bid_price)
    ticker_data[trade.ticker]["offer_prices"].append(trade.offer_price)
    ticker_data[trade.ticker]["ref_prices"].append(trade.ref_price)

for ticker, data in ticker_data.items():
    plt.figure(figsize=(10, 6))
    plt.plot(data["dates"], data["bid_prices"], label="Bid Prices", linestyle="--")
    plt.plot(data["dates"], data["offer_prices"], label="Offer Prices", linestyle="--")
    plt.plot(data["dates"], data["ref_prices"], label="Reference Prices", linestyle="-")
    plt.title(f"Price Data for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
