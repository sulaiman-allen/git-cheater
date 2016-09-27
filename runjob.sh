#! /bin/bash

# A script for updating git once a day if no commit has been added that day.
# Created in reaction to a company's idea that hiring practice dictates choosing
# a candidate should be based upon the number of commits that person has on github.

# Cron runs tasks from the users home directory. To reference path locations in the future
# of this script and the python one, the directory needs to be changed.
cd git-cheater

# Main functionality happens here
python ./git-cheater.py
