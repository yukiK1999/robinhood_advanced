import robin_stocks as r
import sys
import rh_advanced.earning as earning
import rh_advanced.login as login
import rh_advanced.option as option
import rh_advanced.stocks as stocks
import pandas as pd
from tqdm import tqdm
from time import time


if __name__ == "__main__":
    print("Initiating reminder")
    login.robinhood_login('account_info.txt', sys.argv)
    input_tickers_file = sys.argv[1]
    with open(input_tickers_file, 'r') as f:
        input_tickers = f.readlines()

    data = []
    for ticker in input_tickers:
        ticker = ticker.strip()
        start = time()
        opt = option.custom(ticker, '', '', 0.2, 0.7)
        share_price = float(r.stocks.get_latest_price(ticker)[0])
        opt = {**opt, 'Share Price': share_price, 'SC To Break Even': (float(opt['SC break_even_price']) / share_price)*100 - 100,
               'LC To Break Even': (float(opt['LC break_even_price']) / share_price) * 100 - 100}
        data.append(opt)
        print(opt)
        end = time()
        print(end - start)
    df = pd.DataFrame(data=data)
    df.to_excel('options.xlsx')


