#!/bin/bash

# This is a script for the initial setup of the cron job used to automate the process of running the
# other scripts.

# write current crontab
crontab -l > gitcheater

# add new cron job to cron file
echo "58 23 * * * /bin/bash ~/git-cheater/runjob.sh  > ~/git-cheater/listener.log 2>&1" >> gitcheater

# install new cron file
crontab gitcheater

rm gitcheater
