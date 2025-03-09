label other_invest:
    define fast_dissolve = Dissolve(0.5)
    define normal_dissolve = Dissolve(1.0)
    define slow_dissolve = Dissolve(2.0)
    $ recession = None
    if year != 2030:
        $ recession = False
    else:
        $ recession = True

    scene bg stocks_up


    "Time to buy some stocks!"
    "Let's check the market prices."
    $ show_stock_prices = True

    $ market_stocks = [
        "spy",
        "wcb",
        "ggl"
    ]
    #Show prices
    $ done = False
    $ max_shares = 0
    while not done:

        $ shares_before = 0
        $ market_order = (renpy.input("Choose a symbol to view, or \"quit\".")).lower()
        if market_order == "quit":
            $ done = True
        if market_order in market_stocks:
            if market_order == "spy":
                $ max_shares = int(money/spy_price)
                $ shares_to_buy = renpy.input("How many $SPY to buy @ $[spy_price]? (Max: [max_shares] shares)")
                $ shares_to_buy = int(shares_to_buy)
                $ total_price = shares_to_buy * spy_price
                "$[spy_price] x [shares_to_buy] shares: $[total_price]"
                if total_price > money:
                    "Robintrade alert: Insufficient funds in account."
                else:
                    "Your order has been placed..."
                    python:
                        try:
                            shares_before = held_stocks["SPY"]#Pre spy
                            held_stocks["SPY"] = shares_before + shares_to_buy
                        except KeyError:
                            held_stocks["SPY"] = shares_to_buy
                        money -= total_price
                    "Purchase successful."

            if market_order == "wcb":
                $ max_shares = int(money/wcb_price)
                $ shares_to_buy = renpy.input("How many $WCB to buy @ $[wcb_price]? (Max: [max_shares] shares)")
                $ shares_to_buy = int(shares_to_buy)
                $ total_price = shares_to_buy * wcb_price
                "$[wcb_price] x [shares_to_buy] shares: $[total_price]"
                if total_price > money:
                    "Robintrade alert: Insufficient funds in account."
                else:
                    "Your order has been placed..."
                    python:
                        try:
                            shares_before = held_stocks["WCB"]
                            held_stocks["WCB"] = shares_before + shares_to_buy
                        except KeyError:
                            held_stocks["WCB"] = shares_to_buy
                        money -= total_price
                    "Purchase successful."

            if market_order == "ggl":
                $ max_shares = int(money/ggl_price)
                $ shares_to_buy = renpy.input("How many $GGL to buy @ $[ggl_price]? (Max: [max_shares] shares)")
                $ shares_to_buy = int(shares_to_buy)
                $ total_price = shares_to_buy * ggl_price
                "$[ggl_price] x [shares_to_buy] shares: $[total_price]"
                if total_price > money:
                    "Robintrade alert: Insufficient funds in account."
                else:
                    "Your order has been placed..."
                    python:
                        try:
                            shares_before = held_stocks["GGL"]
                            held_stocks["GGL"] = shares_before + shares_to_buy
                        except KeyError:
                            held_stocks["GGL"] = shares_to_buy
                        money -= total_price
                    "Purchase successful."
        else:
            if not done:
                "I don't think that symbol is a good investment."
    "Well, that's enough investing for now."

    $ show_stock_prices = False
    return
