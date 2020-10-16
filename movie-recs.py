#movie-recs.py

import requests
import re
from bs4 import BeautifulSoup




def recommend_movies(emotion):
    if emotion.lower() in ['sad', 'depressed']:
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif emotion.lower() in ['whimsical', 'creative', 'happy']:
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    elif emotion.lower() == 'excited':
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif emotion.lower() in ['adventurous', 'joyous', 'powerful', 'motivated']:
        url = 'https://www.imdb.com/search/title/?genres=adventure&title_type=feature&sort=moviemeter, asc'
    elif emotion.lower() == 'brooding':
        url = 'https://www.imdb.com/search/title/?genres=mystery&title_type=feature&sort=moviemeter, asc'

    response = requests.get(url)
    data = response.text
    incrementor = 0
    movie_dict = {}
    soup = BeautifulSoup(data, 'html.parser')
    titles = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})

    return titles



if __name__ == '__main__':
    bot_name = 'Botty'
    print(f'Hello there! Welcome to the Movie Recommendation System! {bot_name} will be recommending some movies for you today!')
    emotion = input('Enter an emotion (a single word): ')
    driver = recommend_movies(emotion)
    count = 0
    incrementor = 1

    if(emotion.lower() == "disgust" or emotion.lower() == "anger"
                           or emotion.lower() =="surprise"):

        for i in driver:
            # Splitting each line of the
            # IMDb data to scrape movies
            temp = str(i).split('>;')

            if(len(temp) == 3):
                print(str(incrementor) +'). ' + temp[1][:-1])
                incrementor += 1

            if(count > 150):
                break
            count += 1
    else:
        for i in driver:
            temp = str(i).split('>')

            if(len(temp) == 3):
                print(str(incrementor) +'). ' +temp[1][:-3])
                incrementor += 1

            if(count > 150):
                break
            count+=1
