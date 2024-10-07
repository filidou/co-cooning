# This files contains your custom actions which can be used to run
# custom Python code.
#

import requests
from rasa_sdk import Action

OMDB_API_KEY = "b238afd6"  # Your provided OMDb API key

class ActionRecommendMovie(Action):
    def name(self):
        return "action_recommend_movie"

    def run(self, dispatcher, tracker, domain):
        movie_genre = tracker.get_slot('movie_genre')
        release_year = tracker.get_slot('release_year')

        movie = self.get_movie_recommendation(movie_genre, release_year)

        if movie:
            dispatcher.utter_message(
                text=f"I recommend you watch {movie['Title']}. "
                     f"It's a {movie_genre} movie from {movie['Year']}, rated {movie['imdbRating']} on IMDb!"
            )
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find a movie recommendation at the moment.")

        return []

    def get_movie_recommendation(self, genre, release_year):
        base_url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&type=movie"
        
        if genre:
            # OMDb doesn't directly filter by genre, so we search based on keywords or provide a fallback
            base_url += f"&s={genre}"
        if release_year:
            base_url += f"&y={release_year}"
        
        response = requests.get(base_url)
        data = response.json()

        # Check if the API returns a valid response with a movie
        if data.get('Response') == 'True' and data.get('Search'):
            # Return the first movie from the search results
            movie_id = data['Search'][0]['imdbID']
            # Get detailed information about the movie using the IMDb ID
            movie_detail_url = f"http://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}"
            movie_details = requests.get(movie_detail_url).json()
            return movie_details
        return None


class ActionRecommendSeries(Action):
    def name(self):
        return "action_recommend_series"

    def run(self, dispatcher, tracker, domain):
        series_genre = tracker.get_slot('series_genre')
        release_year = tracker.get_slot('release_year')

        series = self.get_series_recommendation(series_genre, release_year)

        if series:
            dispatcher.utter_message(
                text=f"I recommend you watch {series['Title']}. "
                     f"It's a {series_genre} series from {series['Year']}, rated {series['imdbRating']} on IMDb!"
            )
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find a TV series recommendation at the moment.")

        return []

    def get_series_recommendation(self, genre, release_year):
        base_url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&type=series"
        
        if genre:
            base_url += f"&s={genre}"
        if release_year:
            base_url += f"&y={release_year}"

        response = requests.get(base_url)
        data = response.json()

        if data.get('Response') == 'True' and data.get('Search'):
            # Return the first series from the search results
            series_id = data['Search'][0]['imdbID']
            # Get detailed information about the series using the IMDb ID
            series_detail_url = f"http://www.omdbapi.com/?i={series_id}&apikey={OMDB_API_KEY}"
            series_details = requests.get(series_detail_url).json()
            return series_details
        return None




# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
