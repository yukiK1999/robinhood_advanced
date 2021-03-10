import robin_stocks as r
import datetime

date_time_pattern = "%Y-%m-%d %p"


def get_next_eps_date(stock_earning):
    for earning in stock_earning:
        if earning['eps']['actual'] is not None:
            continue
        else:
            return earning['report']['date'] + " " + earning['report']['timing'].upper()
    return "3000-01-10 AM"


def get_holding_earnings():
    print("From the holdings:")
    my_stocks = r.build_holdings()
    stocks_earning = [(symbol, r.stocks.get_earnings(symbol)) for symbol in my_stocks.keys()]
    stocks_earning.sort(key=lambda x: datetime.datetime.strptime(get_next_eps_date(x[1]), date_time_pattern))
    print_stocks_earning(stocks_earning)


def print_stocks_earning(stocks_earning):
    for symbol, earning in stocks_earning:
        eps_date = get_next_eps_date(earning)
        if eps_date[-2:] == 'AM':
            eps_date = eps_date[:-2] + 'Pre-Market'
        else:
            eps_date = eps_date[:-2] + 'After-Hours'
        if eps_date == "3000-01-10 Pre-Market":
            eps_date = "Unavailable"
        print(symbol + " next EPS date: " + eps_date)


def get_watchlist_earnings():
    lists_stocks = r.account.get_all_watchlists()
    for l in lists_stocks['results']:
        watch_list_name = l['display_name']
        print("\n\n")
        print("From the watchlist " + watch_list_name)
        watch_list = r.account.get_watchlist_by_name(watch_list_name)
        stocks_earning = [(stock['symbol'], r.stocks.get_earnings(stock['symbol'])) for stock in watch_list['results']]
        stocks_earning.sort(key=lambda x: datetime.datetime.strptime(get_next_eps_date(x[1]), date_time_pattern))
        print_stocks_earning(stocks_earning)
