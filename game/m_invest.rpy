label invest:
    mc "Lets buy some juicy stocks and ETFs."
    scene bg stocks_pc_green
    with Wipeleft(2)
    mc "I don't know much about stocks..."
    mc "I've heard from my grandpa's ramblings that some \"Baldman Socks\" EFT or whatever is good to invest in."
    mc "Or was it ETF?"
    mc "He said it's a good idea to invest in the S&P 500, but there doesn't seem to be a way to do that."
    mc "It says it costs 5,000 dollars to invest? Wow, it must really only be for rich people."
    scene bg stocks_pc_green
    with Wipeleft(2)
    mc "Ok, it seems like my account setup went through ok."
    mc "All my friends are using Robintrade, so I think I'll set it up with this. "
    mc "Setup went good..."
    mc "It's asking if I'm a beginner invester? Yes, I certainly am."
    mc "It's so helpful that they have a little tour here on how to navigate the stock market."
    mc "..."
    mc "So you {i}can't{/i} invest into the S&P 500 and Nasdaq-100 directly? That makes sense."
    mc "With a price of $5,000, it makes sense that you can't buy a lot of these."
    mc "Instead, it seems like we have to use an \"exchange-traded fund\", or ETF."
    mc "These {i}}track{/i} the price of the market indexes."
    mc "I guess I'll buy some, but I heard investment advisors say that you should diversify a little bit."
    mc "Maybe I'll buy some bonds, but I don't want to put too much money into it right now in case it goes down."
    mc "Because then it would be more of a buying opportunity."
    mc "You don't want to put too much in at once, because then you can't capitalize on a lower price if it falls a bit tomorrow."
    mc "So, the ETF costs $500."
    mc "With the $50,000 I have, in theory I could buy 100 of these ETFs and grow my money by so much!"
    mc "But I still need money for food and stuff..."
    mc "So I'll probably just buy about 10."
    mc "My living expenses run me about $24,000 a year."
    mc "So I {i}could{/i} invest also into some other stuff..."
    menu:
        "Should I buy S&P ETF?"
        "Yes":
            jump yes_buy
        "No":
            jump no_buy
    
    label yes_buy:
        $ held_stocks.update({'SPY', 10})
    label no_buy:
        mc "I won't buy any. It's risky and we haven't had a recession in a while."

    mc "I've heard about dividends and how they're basically free money for holding a stock..."
    mc "Seems like the fast food giant $WCB pays a dividend about about 2.2%."

    mc "So for the amount of stock you're holding, you can get paid 2.2% of that every year."
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
        "Yeah, I'll put a bit into it."
        "If WcBonald's stock is about $200, I'll buy about 100 shares."
        "That way, the value will be enough to give me about $400 in dividends every year."
        "So, a little more than a dollar a day."
    
    jump end
