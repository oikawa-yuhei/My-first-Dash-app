from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


def get_url_info():
    url = "https://scraping-for-beginner.herokuapp.com/udemy"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    name = soup.select('.card-title')[0].string

    n_subscribers = soup.select('.subscribers')[0].string
    n_subscribers= int(n_subscribers.split("：")[1])

    n_reviews = soup.select('.reviews')[0].string
    n_reviews = int(n_reviews.split("：")[1])

    results = {
        "name" : name,
        "n_subscribers" : n_subscribers,
        "n_reviews" : n_reviews
    }
    return results



def write_data():
    df = pd.read_csv('assets/data.csv')
    _results = get_url_info()
    date = datetime.datetime.today().strftime('%Y/%-m/%-d')

    subscribers = _results['n_subscribers']
    reviews = _results['n_reviews']
    name = _results['name']
    results = pd.DataFrame([[date, subscribers, reviews]],columns=['date','subscribers','reviews'])


    df= pd.concat([df, results])
    df = df.to_csv('assets/data.csv', index = False)


if __name__=="__main__":
    write_data()
