import requests
import subprocess
from datetime import *
from bs4 import BeautifulSoup

def main():

    with open('enter_git_username_here.txt') as inputfile:
        git_username = inputfile.readlines()[0]
        print("git username =", git_username)
    current_date = datetime.now().strftime("%Y-%m-%d")
    base_url = "https://github.com/" + git_username + "?tab=overview&from=" + current_date
    #base_url = "https://github.com/sulaiman-allen?tab=overview&from=2016-03-01"

    html = requests.get(base_url)
    soup = BeautifulSoup(html.content, "lxml")
    results = soup.find_all('span', class_='text-gray m-0')

    # if a commit wasn't made for today...
    if results:
        for result in results:
            if "had no activity during this period" in str(result.string.encode("utf-8")):
                print("no commits made for today")
                with open('scumbag.txt', "a") as outfile:
                    outfile.write("Another unsuccesful day\n")
                subprocess.call(['git', 'add', 'scumbag.txt'])
                subprocess.call(['git', 'commit', '-m', 'testing if this stupid thing works'])
                subprocess.call(['git', 'push', 'origin', 'master'])

    else:
        print("commits were made for this day")
        subprocess.call(['rm', 'scumbag.txt'])



if __name__ == '__main__':
    main()
