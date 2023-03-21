from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st
import os

st.title("NBA Players' Recent Stats")

list_of_teams = {"Atlanta Hawks": "https://www.espn.com/nba/team/roster/_/name/atl/atlanta-hawks",
                 "Boston Celtics": "https://www.espn.com/nba/team/roster/_/name/bos/boston-celtics",
                 "Brooklyn Nets": "https://www.espn.com/nba/team/roster/_/name/bkn/brooklyn-nets",
                 "Charlotte Hornets": "https://www.espn.com/nba/team/roster/_/name/cha/charlotte-hornets",
                 "Chicago Bulls": "https://www.espn.com/nba/team/roster/_/name/chi/chicago-bulls",
                 "Cleveland Cavaliers": "https://www.espn.com/nba/team/roster/_/name/cle/cleveland-cavaliers",
                 "Dallas Mavericks": "https://www.espn.com/nba/team/roster/_/name/dal/dallas-mavericks",
                 "Denver Nuggets": "https://www.espn.com/nba/team/roster/_/name/den/denver-nuggets",
                 "Detroit Pistons": "https://www.espn.com/nba/team/roster/_/name/det/detroit-pistons",
                 "Golden State Warriors": "https://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors",
                 "Houston Rockets": "https://www.espn.com/nba/team/roster/_/name/hou/houston-rockets",
                 "Indiana Pacers": "https://www.espn.com/nba/team/roster/_/name/ind/indiana-pacers",
                 "Los Angeles Clippers": "https://www.espn.com/nba/team/roster/_/name/lac/la-clippers",
                 "Los Angeles Lakers": "https://www.espn.com/nba/team/roster/_/name/lal/los-angeles-lakers",
                 "Memphis Grizzlies": "https://www.espn.com/nba/team/roster/_/name/mem/memphis-grizzlies",
                 "Miami Heat": "https://www.espn.com/nba/team/roster/_/name/mia/miami-heat",
                 "Milwaukee Bucks": "https://www.espn.com/nba/team/roster/_/name/mil/milwaukee-bucks",
                 "Minnesota Timberwolves": "https://www.espn.com/nba/team/roster/_/name/min/minnesota-timberwolves",
                 "New Orleans Pelicans": "https://www.espn.com/nba/team/roster/_/name/no/new-orleans-pelicans",
                 "New York Knicks": "https://www.espn.com/nba/team/roster/_/name/ny/new-york-knicks",
                 "Oklahoma City Thunder": "https://www.espn.com/nba/team/roster/_/name/okc/oklahoma-city-thunder",
                 "Orlando Magic": "https://www.espn.com/nba/team/roster/_/name/orl/orlando-magic",
                 "Philadelphia 76ers": "https://www.espn.com/nba/team/roster/_/name/phi/philadelphia-76ers",
                 "Phoenix Suns": "https://www.espn.com/nba/team/roster/_/name/phx/phoenix-suns",
                 "Portland Trail Blazers": "https://www.espn.com/nba/team/roster/_/name/por/portland-trail-blazers",
                 "Sacramento Kings": "https://www.espn.com/nba/team/roster/_/name/sac/sacramento-kings",
                 "San Antonio Spurs": "https://www.espn.com/nba/team/roster/_/name/sa/san-antonio-spurs",
                 "Toronto Raptors": "https://www.espn.com/nba/team/roster/_/name/tor/toronto-raptors",
                 "Utah Jazz": "https://www.espn.com/nba/team/roster/_/name/utah/utah-jazz",
                 "Washington Wizards": "https://www.espn.com/nba/team/roster/_/name/wsh/washington-wizards"}

tag = st.selectbox("Choose a Team:", list_of_teams)
generate = st.button("Generate CSV")

url = list_of_teams[tag]

doc = requests.get(url).content
web_content = BeautifulSoup(doc, "html.parser")

roster_list = web_content.find("tbody", class_="Table__TBODY")
player_links = roster_list.find_all("a", class_="AnchorLink")

player_links_list = []
iterator = 0
for link in player_links:                      #This for loop is to gather the player links in a team
    if iterator % 2 == 0:
        iterator += 1
        continue
    iterator += 1
    player_link = link.get("href")
    player_links_list.append(player_link)

df_list = []
df_list_with_blanks = []
row_header = []
for player_url in player_links_list:           #Once gathered we parse the information we need looping thru the urls
    doc1 = requests.get(player_url).content
    web_content1 = BeautifulSoup(doc1, "html.parser")

    recent_games_stats = web_content1.find("div", class_="ResponsiveTable is-color-controlled")
    if recent_games_stats is None:             #if the player has no info skip
        continue
    player_stats = recent_games_stats.find_all("td", class_="Table__TD")

    player_first_name = web_content1.find("span", class_="truncate min-w-0 fw-light").text
    player_last_name = web_content1.find("span", class_="truncate min-w-0").text
    print(player_first_name, player_last_name)
    st.text(player_first_name + " " + player_last_name)

    notes_row = []
    stats_row1 = []
    stats_row2 = []
    stats_row3 = []
    stats_row4 = []
    stats_row5 = []
    stats_row6 = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    for stat in player_stats:                   #this for loop grabs the recent game info and puts them into rows
        player_info = stat.text
        if len(player_info) > 12:
            notes_row.append(player_info)
        elif len(stats_row1) != 14:
            stats_row1.append(player_info)
        elif len(stats_row2) != 14:
            stats_row2.append(player_info)
        elif len(stats_row3) != 14:
            stats_row3.append(player_info)
        elif len(stats_row4) != 14:
            stats_row4.append(player_info)
        elif len(stats_row5) != 14:
            stats_row5.append(player_info)

    player_name_row = [player_first_name, player_last_name, "", "", "", "", "", "", "", "", "", "", "", ""]
    row_header = ["DATE", "OPP", "RESULT", "MIN", "FG%", "3P%", "FT%", "REB", "AST", "BLK", "STL", "PF", "TO", "PTS"]
    recent_games_table = [stats_row1, stats_row2, stats_row3, stats_row4, stats_row5]
    recent_games_table_with_blank = [player_name_row, stats_row1, stats_row2, stats_row3,
                                     stats_row4, stats_row5, stats_row6]

    df = pd.DataFrame(
        data=recent_games_table,
        columns=row_header
    )
    df_list.append(df)

    df_with_blanks = pd.DataFrame(
        data=recent_games_table_with_blank,
        columns=row_header
    )
    df_list_with_blanks.append(df_with_blanks)

    if notes_row:
        st.caption(notes_row)

    st.table(df)


# Concatenate all DataFrames into one
final_df = pd.concat(df_list_with_blanks, ignore_index=True)


# Export to CSV if button is clicked
if generate:
    downloads_folder = os.path.expanduser("~") + "/Downloads/"
    final_df.to_csv(downloads_folder + "nba_stats.csv", index=False)
    st.write("CSV file has been generated!")

# Display the DataFrame which mimics the CSV file the user will obtain if they choose to generate it
st.write(final_df)


