#!/bin/bash

# write current crontab
crontab -l > gitcheater

# add new cron job to cron file
echo "58 23 * * * /bin/bash ~/git-cheater/runjob.sh  > ~/git-cheater/listener.log 2>&1" >> gitcheater

# install new cron file
crontab gitcheater

rm gitcheater
