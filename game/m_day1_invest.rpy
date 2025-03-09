
init python:
    def between(var, o1, o2):
        if var >= o1 and var <= o2:
            return True
        else:
            return False

    def calc_prices_and_amts():
        global investment_level
        global tutorial_buy_sp
        if investment_level == 1:
            tutorial_buy_sp = 1
        if investment_level == 2:
            tutorial_buy_sp = 5
        if investment_level == 3:
            tutorial_buy_sp = 15
            if sp_price == 500:
                tutorial_buy_sp += 20
        if investment_level == 4:
            tutorial_buy_sp = 30


label day1_invest:
    $ noob = False

    if money < spy_price:
        "You have broken the game, you should never see this message."
        return
    default dividend_amt = 0
    define fast_dissolve = Dissolve(0.5)
    define normal_dissolve = Dissolve(1.0)
    define slow_dissolve = Dissolve(2.0)

    $ investment_Level = 0

    if between(money, 3000, 10000):
        $ investment_level = 1

    if between(money, 10001, 30000):
        $ investment_level = 2

    if between(money, 31000, 60000):
        $ investment_level = 3

    if money > 60000:
        $ investment_level = 4

    $ calc_prices_and_amts()


    mc "Lets buy some juicy stocks and ETFs."
    scene bg stocks_up
    with normal_dissolve
    mc "I don't know much about stocks..."
    mc "I've heard from my grandpa's ramblings that some \"S&P 500\" ETF or whatever is good to invest in."
    mc "He said it's a good idea to invest in the S&P 500, but there doesn't seem to be a way to do that."
    mc "It says it costs 5,000 dollars to invest? Wow, it must really only be for rich people."
    scene bg stocks_up
    with normal_dissolve
    mc "Ok, it seems like my account setup went through ok."
    mc "All my friends are using Robintrade, so I think I'll set it up with this. "
    mc "This app is really helpful, it has a tour here on how to navigate the stock market."
    mc "..."
    mc "So you {i}can't{/i} invest into the S&P 500 and Nasdaq-100 directly..."
    mc "Instead, it seems like we have to use an \"exchange-traded fund\", or ETF."
    mc "These {i}track{/i} the price of the market indexes. The symbol of the S&P ETF is SPY."
    mc "I'll put some money into it."
    mc "So, the ETF costs [spy_price]."
    mc "With the money I have, in theory I could buy some of these ETFs and grow my money by so much!"
    mc "But I still need money for food and stuff..."

    mc "So I'll probably just buy about [tutorial_buy_sp]. I don't want to put too much in, otherwise I won't have enough to live."
    menu:
        "Should I buy the S&P ETF?"

        "Yes":
            jump yes_buy
        "No":
            jump no_buy
    
    label yes_buy:
        $ held_stocks["SPY"] = tutorial_buy_sp
        $ money -= (tutorial_buy_sp * spy_price)
        jump post_sp_buy

    label no_buy:
        mc "I won't buy any. It's risky and the price is kind of high."
        mc "It's gone up so much and it might come down a lot too."
        mc "If I buy now, I could end up losing a lot."
        jump post_sp_buy

label post_sp_buy:
    mc "I've heard about dividends and how they're basically free money for holding a stock..."
    mc "Seems like the fast food giant $WCB pays a dividend of about 2.2\%."

    mc "So for the amount of stock you're holding, you can get paid 2.2\% of that every year."
    mc "But based on these historical S&P graphs, the returns are a lot more per year."
    mc "And the dividends can be risky because they can change the dividend return or the stock could be more volatile than the market as a whole."
    mc "It's also good to just diversify a llittle bit."
    mc "Seems like WcBonald's stock costs [wcb_price]."
    mc "It would probably be safe to get a bit of another stock, and dividends aren't bad too."
    menu:
        "Should I buy some WcBonald's dividend stock?"

        "Yes! I love free money.":
            jump wcb_div
        "No, I'll play it a bit safer.":
            jump no_wcb_div
    
    label wcb_div:
        $ held_stocks["WCB"] = 2
        $ money -= (wcb_price)*2
        "Yeah, I'll put a bit into it."
        "Only 2 shares, though."
        "These dividends aren't that good, and I just want to invest in something that I've actually heard of to start."

    label no_wcb_div:
        "Eh, I don't think it'll even give me that much. I'm better off putting it into a savings account."

    label after_wcb_div:
        if calling_day1:
            $ calling_day1 = False
            return
        "So now, I guess I just have to wait?"
        "I'll have a bunch of money in like 20 years or so, I guess."
        "Hopefully this turns out well!"

        scene bg home
        with wipeleft
        "Now that my money is invested, I should probably get a job."
        "Or I could go to college, but i'd have to take out loans..."
        menu:
            mc "What should I do?"
            
            "Get a job":
                jump get_job_with_intro
            
            "Go to college":
                jump degree

    return
