# NBA_Players_Recent_Stats

This repository contains a Python script that webscrapes the latest 5 games played for any NBA team and displays the information via Streamlit.
This tool is designed to help expedite research when deciding on lineups for DraftKings.

## Prerequisites

- Python 3.6 or higher
- Streamlit
- Requests
- BeautifulSoup
- Pandas

## Installation

1. Clone this repository:

```
git clone https://github.com/username/NBA-player-Webscraper.git
```

2. Install the necessary packages:

```
pip install -r requirements.txt
```

3. Run the script:

```
python nba_webscraper.py
```

4. Visit the Streamlit URL which should be printed to the console.

## Usage

1. Choose the NBA team you would like to view from the dropdown menu
2. The most recent 5 games played by each player on the team will be displayed.
3. Option to generate a .CSV file
