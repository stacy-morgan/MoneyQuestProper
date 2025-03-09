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

    $ market_stocks = [
        "SPY",
        "WCB"
    ]
    #Show prices
    $ market_order = input("Choose a symbol to view.")
    if market_order in market_stocks:
        pass

    else:
        "I don't think that symbol is a good investment."


