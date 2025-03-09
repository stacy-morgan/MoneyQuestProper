label year_over_loop:
    if year < 2030:
        $ year += 1
    else:
        $ year += 5

    mc "Happy new year! It is now [year]."
    if money > 0:
        $ savings_add = (money*1.045)
        bank "Thank you for keeping a savings account with Baldman Sacks."
        bank "You have been credited $[savings_add]."
        $ money += savings_add

    if year == 2026:
        news_reporter "Happy New Year!"
        news_reporter "In finance news, the S&P 500 has gone up by 11\% since last year. Great returns!"
        news_reporter "At the beginning of the year, it was at $[spy_price]."
        $ spy_price *= 1.11
        news_reporter "It is currently trading at [spy_price]."
        news_reporter "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 10\% increase in stock value this year."
        $ wcb_price *= 1.1

    if year == 2027:
        news_reporter "In finance news, the S&P 500 has gone up by 9.2\% since last year. Great returns!"
        news_reporter "Although slightly below last year, we really can't complain."
        news_reporter "At the beginning of the year, it was at [spy_price]."
        $ spy_price *= 1.092
        news_reporter "It is currently trading at [spy_price]."
        news_reporters "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 9\% increase in stock value this year."
        $ wcb_price *= 1.09

    if year == 2028:
        news_reporter "In finance news, the S&P 500 has gone up by 9.5\% since last year. Great returns!"
        news_reporter "This growth outpaced last year very slightly, but only by about 0.3%."
        news_reporter "At the beginning of the year, it was at [spy_price]."
        $ spy_price *= 1.095
        news_reporter "It is currently trading at [spy_price]."
        news_reporters "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 4\% increase in stock value this year."
        $ wcb_price *= 1.04

    if year == 2029:
        news_reporter "In finance news, the S&P 500 has gone up by 8.1\% since last year. Not as great, but it's still outpacing inflation."
        news_reporter "This growth is lower than the previous two years, below 2028 by 1.4%."
        news_reporter "At the beginning of the year, it was at [spy_price]."
        $ spy_price *= 1.081
        news_reporter "It is currently trading at [spy_price]."
        news_reporters "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 6\% increase in stock value this year."
        $ wcb_price *= 1.06

    if year == 2030:
        news_reporter "In finance news, the S&P 500 has had a terrible year."
        news_reporter "Losses have been reported to be up to 18\% since last year."
        news_reporter "Fears about global trade and technology uncertainty have led to a steep decline in trust and profitability. "
        news_reporter "At the beginning of the year, it was at [spy_price]."
        $ spy_price *= 0.82
        news_reporter "It is currently trading at [spy_price]."
        news_reporter "We will recover!"
        news_reporter "Experts may consider this a buying opportunity, ready to pounce later for higher profits."
        news_reporter "In other news, WcBonalds reports a 1.3\% decrease in stock value this year."
        $ wcb_price *= 0.097

    if year == 2035:
        news_reporter "In finance news, the S&P 500 has gone up by 3.5\% since last year. The market is recovering."
        news_reporter "Since the recession, it has gone back up by approximately 40%."
        news_reporter "From the recession, it was at [spy_price]."
        $ spy_price *= 1.4
        news_reporter "It is currently trading at [spy_price]."
        news_reporters "Another great year for investors worldwide!"

        news_reporter "In other news, WcBonalds reports a 32\% increase in stock value this year."
        $ wcb_price *= 1.32
    
    if "WCB" in held_stocks:
        $ dividend_amt =  ((wcb_price*10) *0.022)

        $ savings_acct += dividend_amt
        robintrade "You have been credited [dividend_amt] for your 10 shares in $WCB @ [wcb_price]."

    jump year_over_loop