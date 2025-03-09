label invest:
    default dividend_amt = 0
    define fast_dissolve = Dissolve(0.5)
    define normal_dissolve = Dissolve(1.0)
    define slow_dissolve = Dissolve(2.0)

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
    mc "So, the ETF costs $500."
    mc "With the $50,000 I have, in theory I could buy 100 of these ETFs and grow my money by so much!"
    mc "But I still need money for food and stuff..."
    mc "So I'll probably just buy about 75. I don't want to put too much in, otherwise I won't have enouhg to live."
    mc "My living expenses run me about $24,000 a year. So I'll need to get a job."
    menu:
        "Should I buy the S&P ETF?"

        "Yes":
            jump yes_buy
        "No":
            jump no_buy
    
    label yes_buy:
        $ held_stocks["SPY"] = 75
        $ money -= 35000
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

    mc "It would probably be safest to only get a little bit of dividend stock, or not at all."
    menu:
        "Should I buy some WcBonald's dividend stock?"

        "Yes! I love free money.":
            jump wcb_div
        "No, I'll play it a bit safer.":
            jump no_wcb_div
    
    label wcb_div:
        $ held_stocks["WCB"] = 50
        $ money -= (wcb_price)*50
        "Yeah, I'll put a bit into it."
        "If WcBonald's stock is about $200, I'll buy about 50 shares."
        "That way, the value will be enough to give me about $300 in dividends every year."
        "So, a little less than a dollar a day."
        "And I can sell this later for more profit."
        jump after_wcb_div

    label no_wcb_div:
        "Eh, I don't think it'll even give me that much. I'm better off putting it into a savings account."
        jump after_wcb_div

    label after_wcb_div:
        "So now, I guess I just have to wait?"
        "I'll have a bunch of money in like 20 years or so, I guess."
        "Hopefully this turns out well!"

        scene bg home
        with wipeleft
        "Now that my money is invested, I should probably get a job."
        "Or I could take out loans for a job..."
        "I've applied to some, but the cost has really been holding me back."
        "Financial aid could help and then I could take out loans for something better."
        menu:
            "What should I do?"
            
            "Get a job":
                jump get_job_with_intro
            
            "Go to college.":
                jump degree


