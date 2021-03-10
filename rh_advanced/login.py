import robin_stocks as r

def robinhood_login(account_path, args):
    """

    :param account_path: path to the account info
    :param args: --two-factor enabled
    :return:
    """
    with open(account_path, 'r') as f:
        acc_info = f.readlines()
    acc_info = acc_info[0].split(" ")
    args = args
    two_factor = ("--two_factor" in args)

    print("Logging in")
    if two_factor:
        print("Two Factor authentication required")
        print("Not Implemented")
        exit()

    login_info = r.login(acc_info[0], acc_info[1])
    print("Successfully Logged in")
    return login_info