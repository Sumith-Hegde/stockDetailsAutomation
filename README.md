# stockDetailsAutomation
a shellScript project that creates watchlist of stocks and updates the details of stocks from watchlist

What it does?

-> collects realtime details of top 30 stocks from nifty50 website and updates them in user's machine

-> stores watchlist and stocksBought list of the user

-> notifies user if there is drastic changes in the prices though email

How to use :-

-> copy all the files into a directory

-> run the main.sh file

-> top 30 stocks from nifty50 websites will be shown

-> from the options available in main.sh update watchlist and stocks bought and quit

-> change the sender and reciever email details in mail.py file

-> in linux terminal enter the command 'crontab -e' (if crontab not installed, first install it using 'sudo apt-get install cron')

-> once the crontab opens scroll down and add the following at the end - # */10 10-16 * * 1-5 cd 'path of directory' && /bin/bash update.sh

-> above command updates the details of stocks every 10 minutes from monday to friday from 10am to 4pm and sends email if the percent changes in stock prices of stocks in stocksBought.csv is +/- 2.5%.

-> you can change the percentage from 2.5 to your required number in update.sh file(comments present)

-> to change the timings check the crontab syntax at - https://en.wikipedia.org/wiki/Cron

-> if you want to edit your watchlist or stocks bought you can run main.sh again and do the same
