# git cheater
 A script for updating git once a day if no commit has been added that day.
 Created in reaction to a company's idea that hiring practice dictates choosing
 a candidate should be based upon the number of commits that person has on github.
 
### Install
 The "git-cheater" folder must be placed in the /home/username directory in order to function
 properly.
 ```
 cd ~ && git clone https://github.com/sulaiman-allen/git-cheater.git && cd git-cheater
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
 ./init.sh.
 ```
 init.sh will create a cronjob which will be run once a day at 11:58 pm that executes the main script
 to check for if a commit has been made that day. After init.sh has been run, there is no longer any 
 need for user interaction as the script will run in the background daily.
