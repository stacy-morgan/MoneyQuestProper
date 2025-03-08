label wcd_chef_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcd_chef_game_loop

label wcd_janitor_job:
    mc "I got the job."
    $ yrs_until_promotion = 2
    jump wcd_janitor_game_loop

label wcd_chef_game_loop:
    mc "I am a chef now. I am making $16.50 an hour."
    mc "Yippee!"

label wcd_janitor_game_loop:
    mc "Yay, I'm a WcDonalads janitor now *dies inside*"
