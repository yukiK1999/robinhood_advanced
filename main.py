import robin_stocks as r
import sys



if __name__ == "__main__":
    print("Initiating reminder")
    with open('account_info.txt', 'r') as f:
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

    print("From the holdings:")
    my_stocks = r.build_holdings()
    for key, value in my_stocks.items():
        print(key, value)
        stock_earning = r.stocks.get_earnings(key)
        for earning in stock_earning:
            if earning['report']['verified']:
                continue
            else:
                print(key + ": next EPS date", earning['report']['date'])
                break
    print("\n\n")
    print("From the watchlist:")
    lists_stocks = r.account.get_all_watchlists
    for l in lists_stocks:
        print(l)
        # stock_earning = r.stocks.get_earnings(key)
        # for earning in stock_earning:
        #     if earning['report']['verified']:
        #         continue
        #     else:
        #         print(key + ": next EPS date", earning['report']['date'])
        #         break

