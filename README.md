# git cheater
 A script for updating git once a day if no commit has been added that day. Randomly
 picks a commit message from a list of prewritten messages and modifies a file, scumbag.txt
 by writing the message "Another unsuccesful day". These unsuccesful days will continue to pile
 up until a real commit is written.
 
 This project was created in reaction to a company's idea that hiring practice dictates choosing
 a candidate should be based upon the number of commits that person has on github. Although this 
 script only runs once a day, it could easily be modified to run any number of times without 
 checking to see if a commit even exists for that day. Just throw a few more commit messages in
 the rolodex and it may actually look like you are a productive member of society.
# ( ͡° ͜ʖ ͡°)
 
### Install
 Begin by forking this project to your own repo
 
 The "git-cheater" folder must be placed in the /home/username directory in order to function
 properly.
 ```
 cd ~ && git clone https://github.com/YOUROWNUSERNAMEAFTERFORKING/git-cheater.git && cd git-cheater
 ```
 git-cheater makes use of the python requests package. If the package isn't installed..
 ```
 pip install requests
```
 To use, make sure init.sh is executable: 
 ```
 chmod +x init.sh
 ```
 and run 
 ```
 ./init.sh
 ```
 init.sh will create a cronjob which will be run once a day at 11:58 pm that executes the main script
 to check for if a commit has been made that day. After init.sh has been run, there is no longer any 
 need for user interaction as the script will run in the background daily.
