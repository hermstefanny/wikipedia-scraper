import requests
import json
import re
from bs4 import BeautifulSoup


def get_leaders():
    # Establishing the urls
    root_url = "https://country-leaders.onrender.com/"
    cookie_url = root_url + "cookie/"
    countries_url = root_url + "countries"
    leaders_url = root_url + "/leaders"

    # Inititalizing empty data structures
    leaders_per_country = dict()
    all_leaders = []

    # Getting the cookie
    cookie_resp = requests.get(cookie_url)
    user_cookie = cookie_resp.cookies["user_cookie"]

    # Getting the country information
    countries_resp = requests.get(countries_url, cookies={"user_cookie": user_cookie})
    countries = countries_resp.json()

    # Getting leaders for each country
    for country in countries:
        country_resp = requests.get(
            leaders_url,
            cookies={"user_cookie": user_cookie},
            params={"country": country},
        )
        leaders_per_country[country] = country_resp.text

    # Obtaining the Wikipedia url
    for country, leaders in leaders_per_country.items():
        leaders_dict = json.loads(leaders)

        # Modifying the dictionary to add the country information
        for leaders in leaders_dict:
            leaders["country"] = country
            all_leaders.append(leaders)

    # Creating a session to send the wikipedia URLs
    with requests.Session() as s:
        for leader in all_leaders:
            wiki_parragraph = get_first_paragraph(leader["wikipedia_url"], s)
            leader["wiki_parragraph"] = wiki_parragraph

    return all_leaders


def get_first_paragraph(wikipedia_url, session):

    leaders_wiki = session.get(wikipedia_url)
    soup_leaders = BeautifulSoup(leaders_wiki.content, "html")

    parragraphs = []
    for p in soup_leaders.find_all("p"):
        parragraphs.append(p)

    for p in parragraphs:
        # Find the first instance of bold. It should be the name
        if p.find("b"):
            raw_first_p = p.text
            # Only takes the first bold instance
            break

    # Clean the text with regex

    pattern = "\\n|\S*ⓘ\S*|/xa0|\[.{0,3}?\]|"
    clean_parragraph = re.sub(pattern, "", raw_first_p)

    return clean_parragraph


def save(leaders_per_country):
    json_leaders = json.dumps(leaders_per_country, ensure_ascii=False, indent=4)

    with open("leaders.json", "w", encoding="utf-8") as outfile:
        outfile.write(json_leaders)

    with open("leaders.json", "r", encoding="utf-8") as file:
        content = file.read()

    print("The following content has been saved to 'leaders.json' :")
    print(content)


def main():
    leaders = get_leaders()
    save(leaders)


if __name__ == "__main__":
    main()
