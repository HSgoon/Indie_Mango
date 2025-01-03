from requests import post
from dotenv import load_dotenv
import os

load_dotenv()

response = post(
    'https://api.igdb.com/v4/games',
    headers={
        'Client-ID': os.getenv('CLIENT_ID_IGDB'),
        'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN_IGDB")}'
    },
    data='fields age_ratings,aggregated_rating,aggregated_rating_count,alternative_names,artworks,bundles,category,checksum,collection,collections,cover,created_at,dlcs,expanded_games,expansions,external_games,first_release_date,follows,forks,franchise,franchises,game_engines,game_localizations,game_modes,genres,hypes,involved_companies,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;'
)

# 응답 출력
print("response:", response.json())