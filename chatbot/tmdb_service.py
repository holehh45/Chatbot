import streamlit as st
import requests


class TMDBService:

    def __init__(self):

        self.api_key = st.secrets.get(
            "TMDB_API_KEY",
            None
        )

    def search_movie(
        self,
        title
    ):

        if not self.api_key:
            return None

        url = (
            "https://api.themoviedb.org/3/search/movie"
        )

        params = {
            "api_key": self.api_key,
            "query": title
        }

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        if data["results"]:
            return data["results"][0]

        return None
