label year_over:
    scene bg winter_room
    with Dissolve(2.0)

    if year < 2030:
        $ year += 1
        $ money += salary
    elif year == 2030 or year == 2035:
        $ year += 5
        $ money += salary*5
    elif year > 2035:
        $ year += 10
        $ money += salary*10

    mc "Happy new year! It is now [year]."
    if money > 0:
        $ savings_add = round((money*0.017))
        bank "Thank you for keeping a savings account with Baldman Sacks. Interest is 1.7\% APY for your savings account."
        bank "You have been credited $[savings_add]."
        $ money = round(money+savings_add)

    if year == 2026:
        news_reporter "Happy New Year!"
        news_reporter "In finance news, the S&P 500 has gone up by 11\% since last year. Great returns!"
        news_reporter "At the beginning of the year, it was at $[spy_price]."
        $ spy_price = round(spy_price*1.11)
        news_reporter "It is currently trading at $[spy_price]."
        news_reporter "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 10\% increase in stock value this year."
        $ wcb_price = round(wcb_price*1.1)
        news_reporter "GGL is also up only 1.1\% this year."
        $ ggl_price = round(ggl_price*1.011)

    if year == 2027:
        news_reporter "In finance news, the S&P 500 has gone up by 9.2\% since last year. Great returns!"
        news_reporter "Although slightly below last year, we really can't complain."
        news_reporter "At the beginning of the year, it was at $[spy_price]."
        $ spy_price = round( spy_price*1.092)
        news_reporter "It is currently trading at $[spy_price]."
        news_reporter "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 9\% increase in stock value this year."
        $ wcb_price = round(wcb_price*1.09)
        news_reporter "GGL has fallen this year, down 3\% to date."
        $ ggl_price = round(ggl_price*0.97)

    if year == 2028:
        news_reporter "In finance news, the S&P 500 has gone up by 9.5\% since last year. Great returns!"
        news_reporter "This growth outpaced last year very slightly, but only by about 0.3\%."
        news_reporter "At the beginning of the year, it was at $[spy_price]."
        $ spy_price = round(spy_price*1.095)
        news_reporter "It is currently trading at $[spy_price]."
        news_reporter "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 4\% increase in stock value this year."
        $ wcb_price = round(wcb_price*1.04)
        news_reporter "GGL has fallen even further this year, down 3.3\% to date."
        $ ggl_price = round(ggl_price*0.967)

    if year == 2029:
        news_reporter "In finance news, the S&P 500 has gone up by 8.1\% since last year. Not as great, but it's still outpacing inflation."
        news_reporter "This growth is lower than the previous two years, below 2028 by 1.4\%."
        news_reporter "At the beginning of the year, it was at $[spy_price]."
        $ spy_price = round( spy_price*1.081)
        news_reporter "It is currently trading at $[spy_price]."
        news_reporter "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 1\% increase in stock value this year."
        $ wcb_price = round(wcb_price*1.01)
        news_reporter "GGL has fallen more this year, to nobody's surprise."
        news_reporter " The company reported losses of  3.1\% to date."
        $ ggl_price = round(ggl_price*0.969)

    if year == 2030:
        news_reporter "In finance news, the S&P 500 has had a terrible year."
        news_reporter "Losses have been reported to be up to 28\% since last year."
        news_reporter "Fears about global trade and technology uncertainty have led to a steep decline in trust and profitability. "
        news_reporter "At the beginning of the year, it was at $[spy_price]."
        $ spy_price = round( spy_price*0.72)
        news_reporter "It is currently trading at $[spy_price]."
        news_reporter "We will recover!"
        news_reporter "Experts may consider this a buying opportunity, ready to pounce later for higher profits."
        news_reporter "In other news, WcBonalds reports a 1.3\% decrease in stock value this year."
        $ wcb_price = round(wcb_price*0.987)
        news_reporter "GGL has been hit the hardest by this recession."
        news_reporter "They report stock losses of 25.11\% to date."
        $ ggl_price = round(ggl_price*0.7489)

    if year == 2035:
        news_reporter "In finance news, the S&P 500 has gone up by 9.3\% since last year. The market is recovering."
        news_reporter "Since the recession, it has gone back up by approximately 89\%."
        news_reporter "From the recession, it was at $[spy_price]."
        $ spy_price = round(spy_price*1.89)
        news_reporter "It is currently trading at $[spy_price]."
        news_reporter "It's been a solid 5 years for the market's recovery, and I, for one, couldn't be happier."

        news_reporter "In other news, WcBonalds reports a 37\% increase in stock value in the last 5 years."
        $ wcb_price = round(wcb_price*1.37)
        news_reporter "GGL appears to be losing more, reporting a loss of 13\% in the last 5 years."
        $ ggl_price = round(ggl_price*0.87)

    if year == 2040:
        news_reporter "In finance news, the S&P 500 has gone up by 10.3\% since last year. The market is really climbing back up."
        news_reporter "In the last 5 years, it's up about 76\%."
        news_reporter "From the recession, it was at $[spy_price]."
        $ spy_price = round(spy_price*1.76)
        news_reporter "It is currently trading at $[spy_price]."
        news_reporter "Not the highest growth, but it's still a way to double your money."

        news_reporter "In other news, WcBonalds reports a 62\% increase in stock value in the last 5 years."
        $ wcb_price = round(wcb_price*1.51)
        news_reporter "Bad news for GGL holders, again..."
        news_reporter "They're reporting a loss of 16.8\% in the last 5 years."
        $ ggl_price = round(ggl_price*0.832)
    
    if year == 2050:
        news_reporter "In finance news, the S&P 500 has gone up by 11\% since last year. The market is doing great!"
        news_reporter "In the last 10 years, it's doubled."
        news_reporter "10 years ago, it was at $[spy_price]."
        $ spy_price = round(spy_price*2)
        news_reporter "It is currently trading at $[spy_price]."

        news_reporter "In other news, WcBonalds reports a 33\% increase in stock value in the last 10 years."
        $ wcb_price = round(wcb_price*1.33)
        news_reporter "GGL has tanked dramatically, reporting a loss of 40\% in the last 10 years."
        $ ggl_price = round(ggl_price*0.6)

    if year == 2060:
        news_reporter "In finance news, the S&P 500 has gone up by 10\% since last year. The market continues to amaze!"
        news_reporter "In the last 10 years, it's almost doubled again."
        news_reporter "So close to doubling! It's up 96\%."
        news_reporter "10 years ago, it was at $[spy_price]."
        $ spy_price = round(spy_price*1.96)
        news_reporter "It is currently trading at $[spy_price]."

        news_reporter "In other news, WcBonalds reports a 19\% decrease in stock value in the last 10 years."
        $ wcb_price = round(wcb_price*0.081)

        news_reporter "GGL has absolutely tanked in recent years, reports a 33\% loss in stock value in the last 10 years."
        $ ggl_price = round(ggl_price*0.66)

    if year == 2070:
        news_reporter "In finance news, the S&P 500 has gone up by 12\% since last year. It's certianly better than average year!"
        news_reporter "In the last 10 years, it's more than doubled."
        news_reporter "So close to doubling! It's up 103\%."
        news_reporter "10 years ago, it was at $[spy_price]."
        $ spy_price = round(spy_price*2.03)
        news_reporter "It is currently trading at $[spy_price]."

        news_reporter "In other news, WcBonalds reports a 5.9\% increase in stock value in the last 10 years."
        $ wcb_price = round(wcb_price*1.059)
        news_reporter "GGL has gone bankrupt,their stocks are useless."
        $ ggl_price = 0
    
    if "WCB" in held_stocks:
        $ dividend_amt =  round(((wcb_price*10) *0.022))

        robintrade "You have been credited $[dividend_amt] for your 10 shares in $WCB @ [wcb_price]."
        $ money += dividend_amt

    if year <= 2030:
        $ money -= 24000
    elif year == 2035 or year == 2040:
        $ money -= (24000*5)
    else:
        $ money -= (24000*10)

    mc "My rent is also due now. The cost of living is around $24,000 per year."

    if money < 0:
        scene bg atm
        mc "I have no more money!"
        mc "I guess I have to move back in with my parents."
        mc "I should have been financially smarter, I guess."
        return


    return

label collegeTimePass:
    $ spy_price = round(spy_price*1.11) #2026
    $ spy_price = round(spy_price*1.092) #2027
    $ spy_price = round(spy_price*1.095) #2028

    $ wcb_price = round(wcb_price*1.1) #2026
    $ wcb_price = round(wcb_price*1.09) #2027
    $ wcb_price = round(wcb_price*1.04) #2028

    $ ggl_price = round(ggl_price*1.011) #2026
    $ ggl_price = round(ggl_price*0.97) #2027
    $ ggl_price = round(ggl_price*0.967) #2028

    #You graduate in the middle of 2029.
    #Instant intrest on savings account
    $ savings_add = round((money*0.045))
    $ money += savings_add

    $ savings_add = round((money*0.045))
    $ money += savings_add

    $ savings_add = round((money*0.045))
    $ money += savings_add

        
