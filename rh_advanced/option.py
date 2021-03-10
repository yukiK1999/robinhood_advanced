import robin_stocks as r
import rh_advanced.utils as utils


def get_option(ticker, date, delta_threshold, option_type=None, info=None):
    options = r.find_options_by_expiration(ticker, date, optionType=option_type)
    closest_delta = -1.0 if option_type == 'call' else 1.0
    best_option = None
    for o in options:
        if o['delta'] is None:
            continue
        if abs(float(o['delta']) - delta_threshold) < abs(closest_delta - delta_threshold):
            closest_delta = float(o['delta'])
            best_option = o

    return best_option


def custom(ticker, short_date, long_date, short_delta=0.3, long_delta=0.7):
    short_best_option = get_option(ticker, "2021-03-12", short_delta, 'call')
    long_best_option = get_option(ticker, "2022-01-21", long_delta, 'call')
    # strike price, ask_price, delta, expiration date
    info = ['ask_price', 'strike_price', 'delta', 'expiration_date', 'break_even_price']
    # short call additional 'break_even_price'
    long_best_option = utils.filter(long_best_option, info, 'LC ')
    short_best_option = utils.filter(short_best_option, info, 'SC ')
    best_option = {'Ticker': ticker, **long_best_option, **short_best_option,
                   'Return Period': float(long_best_option['LC ask_price'])
                                    / float(short_best_option['SC ask_price'])}
    return best_option
