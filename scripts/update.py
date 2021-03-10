from usp.tree import sitemap_tree_for_homepage
import robin_stocks as r
import sys

if __name__ == '__main__':
    with open('../account_info.txt', 'r') as f:
        acc_info = f.readlines()
    acc_info = acc_info[0].split(" ")
    args = sys.argv
    two_factor = ("--two_factor" in args)

    print("Logging in")
    if two_factor:
        print("Two Factor authentication required")
        print("Not Implemented")
        exit()

    login_info = r.login(acc_info[0], acc_info[1])
    print("Successfully Logged in")

    root = 'https://robinhood.com/'
    collections = []
    stock_hs = set()

    tree = sitemap_tree_for_homepage('https://robinhood.com/sitemap.xml')
    pages = tree.all_pages()
    urls = [p.url.replace(root, "") for p in pages]

    for url in urls:
        if 'collections' in url:
            collections.append(url.replace('collections/', ''))
        elif 'stocks' in url:
            stock_hs.add(url.replace('stocks/', ''))

    print(len(collections))
    print(len(stock_hs))
    print("Updating list of stocks from collections set")
    print(stock_hs)
    for col in collections:
        print(col)
        for s in r.markets.get_all_stocks_from_market_tag(col):
            stock_hs.add(s['symbol'])

    print(len(stock_hs))
