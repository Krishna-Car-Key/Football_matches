import requests

API_KEY = "5wF6ms2LYgiBqMG99iJvQYfA9oEonhBQtSu6pUFmcgHlDQtSNPag6haiTTCF"
URL = f"https://api.sportmonks.com/v3/football/fixtures?api_token={API_KEY}"


def get_data():

    """this function gets the data from the API_KEY & URL given above
    and filters the data and returns the list of matches, result of those
    matches and date of the matches"""

    response = requests.get(URL)
    df = response.json()
    filtered_data = df["data"]

    vs_content = []
    result_content = []
    date_content = []

    for data in filtered_data:

        vs_content.append(data['name'])
        result_content.append(data['result_info'])
        date_content.append(data["starting_at"])

    return vs_content, result_content, date_content


if __name__ == "__main__":
    match, result, date = get_data()
    print(match, result, date)
