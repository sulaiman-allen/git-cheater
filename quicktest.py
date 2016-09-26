import requests
from datetime import *
from bs4 import BeautifulSoup

def main():

    current_date = datetime.now().strftime("%Y-%m-%d")
    git_username = "sulaiman-allen"
    base_url = "https://github.com/" + git_username + "?tab=overview&from=" + current_date
    #base_url = "https://github.com/sulaiman-allen?tab=overview&from=2016-03-01"

    html = requests.get(base_url)
    soup = BeautifulSoup(html.content, "lxml")
    results = soup.find_all('span', class_='text-gray m-0')

    # if a commit wasn't made for today...
    if results:
        for result in results:
            #print("result = ", result.string)
            if "had no activity during this period" in str(result.string.encode("utf-8")):
                print("true")
    else:
        print("commits were made for this day")



if __name__ == '__main__':
    main()
