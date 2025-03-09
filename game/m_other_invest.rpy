label other_invest:
    define fast_dissolve = Dissolve(0.5)
    define normal_dissolve = Dissolve(1.0)
    define slow_dissolve = Dissolve(2.0)
    $ recession = None
    if year != 2030:
        $ recession = False
    else:
        $ recession = True

    if not recession:
        scene bg stocks_up
    else:
        scene bg stocks_down

    "Time to buy some stocks!"
    "Let's check the market prices."
    $ show_stock_prices = True

    $ market_stocks = [
        "spy",
        "wcb"
    ]
    #Show prices
    $ shares_before = 0
    $ market_order = (renpy.input("Choose a symbol to view.")).lower()
    if market_order in market_stocks:
        if market_order == "spy":
            $ temp = renpy.input("Buy SPY?")
            if temp == "yes":
                $ shares_to_buy = renpy.input("How many $SPY to buy @ $[spy_price]?")
                $ shares_to_buy = int(shares_to_buy)
                $ total_price = shares_to_buy * spy_price
                "$[spy_price] x [shares_to_buy] shares: [total_price]"
                if total_price > money:
                    "Robintrade alert: Insufficient funds in account."
                else:
                    python:
                        try:
                            shares_before = held_stocks["SPY"]
                            held_stocks["SPY"] = shares_before + shares_to_buy
                        except KeyError:
                            held_stocks["SPY"] = shares_to_buy
                            money -= total_price
                "Purchase successful."

        if market_order == "wcb":
            $ temp = renpy.input("Buy WCB?")
            if temp == "yes":
                $ shares_to_buy = renpy.input("How many $SPY to buy @ $[wcb_price]?")
                $ shares_to_buy = int(shares_to_buy)
                $ total_price = shares_to_buy * wcb_price
                "$[wcb_price] x [shares_to_buy] shares: [total_price]"
                if total_price > money:
                    "Robintrade alert: Insufficient funds in account."
                else:
                    python:
                        try:
                            shares_before = held_stocks["WCB"]
                            held_stocks["WCB"] = shares_before + shares_to_buy
                        except KeyError:
                            held_stocks["WCB"] = shares_to_buy
                            money -= total_price
                "Purchase successful."

    else:
        "I don't think that symbol is a good investment."
    return
