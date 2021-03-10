import robin_stocks as r


def get_nasdaq_tickers():
    tickers =[]
    with open('nasdaqlisted.txt', 'r') as f:
        ll = f.readlines()
        ll.pop(0)
        ll.pop()
        tickers = [l.split('|')[0] for l in ll]

    with open('nasdaqtraded.txt', 'r') as f:
        ll = f.readlines()
        ll.pop(0)
        ll.pop()
        tickers += [l.split('|')[1] for l in ll]
    return tickers


def clean_tickers(tickers):
    return [t for t in tickers if r.stocks.get_earnings(t) != []]


def write_clean_tickers(tickers):
    with open('tickers.txt', 'w') as f:
        for t in tickers:
            f.write('%s\n' % t)


def get_tickers():
    with open('tickers.txt', 'r') as f:
        return f.readlines()


if __name__ == '__main__':
    tickers = get_nasdaq_tickers()
    tickers = clean_tickers(tickers)
    print(tickers)
    write_clean_tickers(tickers)
