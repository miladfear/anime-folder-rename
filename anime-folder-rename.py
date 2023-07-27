import os
import requests

# set the path to your anime folder
folder_path = "FullPath/To/The/Archive"

def get_season(month):
    if month in ["01", "02", "03"]:
        return "Winter"
    elif month in ["04", "05", "06"]:
        return "Spring"
    elif month in ["07", "08", "09"]:
        return "Summer"
    elif month in ["10", "11", "12"]:
        return "Fall"

# loop through the files in the folder
for filename in os.listdir(folder_path):
    # check if the file is a directory
    if os.path.isdir(os.path.join(folder_path, filename)):
        # check if the folder name already contains a year
        if "[" not in filename:
            # get the anime name from the folder name
            anime_name = filename.replace("_", " ")
            # make a request to the Kitsu API to search for the anime
            response = requests.get(f"https://kitsu.io/api/edge/anime?filter[text]={anime_name}")
            # check if the response was successful
            if response.status_code == 200:
                # get the release year from the response
                anime = response.json()["data"][0]
                fullDate = anime["attributes"]["startDate"][:7] if anime["attributes"]["startDate"] else ""
                year, month = fullDate.split('-')
                season = get_season(month)
                # create the new folder name with the year
                new_name = f"{filename} [ {year} {season} ]"
                # rename the folder
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
