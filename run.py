from src.stages.extract import ExtractMovies

api_key = "a773e9c7af7861e875f8f9d6ada80d36"
ex = ExtractMovies(api_key)
r = ex.extract(qtd_movies=2)
print(r)
