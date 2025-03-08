label wcd_chef_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcd_chef_game_loop

label wcd_janitor_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcd_janitor_game_loop

label wcd_chef_game_loop:
    mc "I am a chef now. I am making $20 an hour."
    mc "Yippee!"
    jump expenses_chef

label wcd_janitor_game_loop:
    mc "Yay, I'm a WcDonalads janitor now *dies inside*"
    mc "I am making $16.50 an hour."
    jump expenses_janitor

label expenses_janitor:
    "One year has passed..."
    "Yearly savings: $34,320"
    "Yearly expenses: $24,000" 
    "Remaining savings: $10,320"
    jump end

label expenses_chef:
    "One year has passed..." 
    "Yearly savings: $41,600" 
    "Yearly expenses: $24,000" 
    "Remaining savings: $17,600"
    jump end



