import requests

URL = 'https://api.tvmaze.com/search/shows?q=boys'
response = requests.get(URL).json()



class TVshow:
    def __init__(self, name, language, rating):
        self.data = {
            "name": name,
            "language": language,
            "rating": rating
        }
    def rating_rate(self):
        try:    
            if self.data["rating"] >= 8.0:
                return "High"
            else:
                return "Low"
        except TypeError:
            return "None"
    
for Show in response:
    temp_show = TVshow(name=Show['show']['name'], language=Show['show']['language'], rating=Show['show']['rating']['average'])
    print(f'Show name: {temp_show.data["name"]} | Language: {temp_show.data["language"]} | Rating: {temp_show.data["rating"]} considered {temp_show.rating_rate()}')
