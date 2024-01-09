import csv
import sqlite3
import pathlib


# Opening up all the data files
with open("saber_karuta_collection.csv", "r", encoding='utf-8') as infile:
    saber_headers, *saber_data = csv.reader(infile)

with open("matt_karuta_collection.csv", "r", encoding='utf-8') as infile:
    matt_headers, *matt_data = csv.reader(infile)

with open("gerald_karuta_collection.csv", "r", encoding='utf-8') as infile:
    gerald_headers, *gerald_data = csv.reader(infile)

with open("forming_karuta_collection.csv", "r", encoding='utf-8') as infile:
    forming_headers, *forming_data = csv.reader(infile)

with open("cher_karuta_collection.csv", "r", encoding='utf-8') as infile:
    cher_headers, *cher_data = csv.reader(infile)

with open("boof_karuta_collection.csv", "r", encoding='utf-8') as infile:
    boof_headers, *boof_data = csv.reader(infile)

with open("black_karuta_collection.csv", "r", encoding='utf-8') as infile:
    black_headers, *black_data = csv.reader(infile)

# Adding a owner column to every data array we read in
saber_headers.append("owner")

for row in saber_data:
    row.append("saber")

matt_headers.append("owner")

for row in matt_data:
    row.append("matt")

gerald_headers.append("owner")

for row in gerald_data:
    row.append("gerald")

forming_headers.append("owner")

for row in forming_data:
    row.append("forming")

cher_headers.append("owner")

for row in cher_data:
    row.append("cher")

boof_headers.append("owner")

for row in boof_data:
    row.append("boof")

black_headers.append("owner")

for row in black_data:
    row.append("black")

# Checking the owner header was properly added and populated
print(saber_headers)

print(saber_data[0])

print(matt_headers)

print(matt_data[0])

print(gerald_headers)

print(gerald_data[0])

print(forming_headers)

print(forming_data[0])

print(cher_headers)

print(cher_data[0])

print(boof_headers)

print(boof_data[0])

print(black_headers)

print(black_data[0])

# Getting the index value for each column for ease of classifying which column index we will be extracting
for index, col_name in enumerate(saber_headers):
    print(col_name, index)

# The column index values we want for the final csv
index_values = [0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 15, 16, 18, 22, 23, 32]

# Making the new headers for the final csv and populating them
new_headers = []

for i in index_values:
    new_headers.append(saber_headers[i])

print(new_headers)

# Grabbing the data that we want from each csv for our final csv
new_data = []

for index, row in enumerate(saber_data):
    new_row = []
    for i in index_values:
        new_row.append(row[i])
    new_data.append(new_row)

for index, row in enumerate(matt_data):
    new_row = []
    for i in index_values:
        new_row.append(row[i])
    new_data.append(new_row)

for index, row in enumerate(gerald_data):
    new_row = []
    for i in index_values:
        new_row.append(row[i])
    new_data.append(new_row)

for index, row in enumerate(forming_data):
    new_row = []
    for i in index_values:
        new_row.append(row[i])
    new_data.append(new_row)

for index, row in enumerate(cher_data):
    new_row = []
    for i in index_values:
        new_row.append(row[i])
    new_data.append(new_row)

for index, row in enumerate(boof_data):
    new_row = []
    for i in index_values:
        new_row.append(row[i])
    new_data.append(new_row)

for index, row in enumerate(black_data):
    new_row = []
    for i in index_values:
        new_row.append(row[i])
    new_data.append(new_row)

# Checking the data was properly extracted from each csv
print(len(new_data))

print(new_data[0])

print(new_data[5000])

print(new_data[6000])

print(new_data[8000])

print(new_data[11000])

print(new_data[15000])

print(new_data[18750])

# Making blank data None so the new csv will have blank spots
for row in new_data:
    if row[6] == '':
        row[6] = None

    if row[7] == '':
        row[7] = None

    if row[8] == '':
        row[8] = None

    if row[11] == '':
        row[11] = None

print(new_data[0])

# Writing out the master csv for the next part of the problem
with open("master_karuta_collection.csv", "w", encoding="utf-8", newline="") as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(new_headers)
    csvout.writerows(new_data)

# Opening up the master csv for use
with open("master_karuta_collection.csv", "r", encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# Setting up the new database file and SQLite3
db_master = pathlib.Path('master.db')

if db_master.exists():
    db_master.unlink()

conn = sqlite3.connect(db_master)

c = conn.cursor()

print(headers)

# Creating the master table
c.execute("DROP TABLE IF EXISTS master")

c.execute("CREATE TABLE IF NOT EXISTS master (code text, print_number integer, edition integer, character_name text, series text, quality integer, dye_code text, dye_name text, frame text, morphed text, trimmed text, nickname text, wishlist_count integer, dropQuality integer, workEffort integer, workerStyle text, owner text);")

c.executemany("INSERT INTO master VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", data)

conn.commit()

c.execute("SELECT * FROM master")

master_table = c.fetchall()

# print(master_table)

# Making all the empty values NULL for ease of comparison and usage for queries later on
c.execute("UPDATE master SET dye_code = NULL WHERE dye_code = '';")

c.execute("UPDATE master SET dye_name = NULL WHERE dye_name = '';")

c.execute("UPDATE master SET frame = NULL WHERE frame = '';")

c.execute("UPDATE master SET nickname = NULL WHERE nickname = '';")

conn.commit()

c.execute("SELECT * FROM master;")

master_table = c.fetchall()

# print(master_table)

# Creating smaller tables from the master table that is organized by each player
# instead of using the individual csv files
c.execute("DROP TABLE IF EXISTS saber")

c.execute("CREATE TABLE saber AS SELECT * FROM master WHERE owner = 'saber';")

conn.commit()

c.execute("SELECT * FROM saber;")

saber_table = c.fetchall()

# print(saber_table)

c.execute("DROP TABLE IF EXISTS matt")
c.execute("CREATE TABLE matt AS SELECT * FROM master WHERE owner = 'matt';")

c.execute("DROP TABLE IF EXISTS gerald")
c.execute("CREATE TABLE gerald AS SELECT * FROM master WHERE owner = 'gerald';")

c.execute("DROP TABLE IF EXISTS forming")
c.execute("CREATE TABLE forming AS SELECT * FROM master WHERE owner = 'forming';")

c.execute("DROP TABLE IF EXISTS cher")
c.execute("CREATE TABLE cher AS SELECT * FROM master WHERE owner = 'cher';")

c.execute("DROP TABLE IF EXISTS boof")
c.execute("CREATE TABLE boof AS SELECT * FROM master WHERE owner = 'boof';")

c.execute("DROP TABLE IF EXISTS black")
c.execute("CREATE TABLE black AS SELECT * FROM master WHERE owner = 'black';")

conn.commit()

# Starting the queries

# Query to compare collection sizes
players = ['saber', 'matt', 'gerald', 'forming', 'cher', 'boof', 'black']
players_collection_sizes = []

c.execute("SELECT COUNT(*) from saber;")

saber_collection_size = c.fetchone()

players_collection_sizes.append(saber_collection_size[0])

c.execute("SELECT COUNT(*) from matt;")

matt_collection_size = c.fetchone()

players_collection_sizes.append(matt_collection_size[0])

c.execute("SELECT COUNT(*) from gerald;")

gerald_collection_size = c.fetchone()

players_collection_sizes.append(gerald_collection_size[0])

c.execute("SELECT COUNT(*) from forming;")

forming_collection_size = c.fetchone()

players_collection_sizes.append(forming_collection_size[0])

c.execute("SELECT COUNT(*) from cher;")

cher_collection_size = c.fetchone()

players_collection_sizes.append(cher_collection_size[0])

c.execute("SELECT COUNT(*) from boof;")

boof_collection_size = c.fetchone()

players_collection_sizes.append(boof_collection_size[0])

c.execute("SELECT COUNT(*) from black;")

black_collection_size = c.fetchone()

players_collection_sizes.append(black_collection_size[0])

for i in range(len(players)):
    print(players[i], "has a collection size of", players_collection_sizes[i])

# Query to compare the wishlist total of each player
player_wishlists = []

c.execute("SELECT SUM(wishlist_count) from saber;")

saber_wishlist = c.fetchone()

player_wishlists.append(saber_wishlist[0])

c.execute("SELECT SUM(wishlist_count) from matt;")

matt_wishlist = c.fetchone()

player_wishlists.append(matt_wishlist[0])

c.execute("SELECT SUM(wishlist_count) from gerald;")

gerald_wishlist = c.fetchone()

player_wishlists.append(gerald_wishlist[0])

c.execute("SELECT SUM(wishlist_count) from forming;")

forming_wishlist = c.fetchone()

player_wishlists.append(forming_wishlist[0])

c.execute("SELECT SUM(wishlist_count) from cher;")

cher_wishlist = c.fetchone()

player_wishlists.append(cher_wishlist[0])

c.execute("SELECT SUM(wishlist_count) from boof;")

boof_wishlist = c.fetchone()

player_wishlists.append(boof_wishlist[0])

c.execute("SELECT SUM(wishlist_count) from black;")

black_wishlist = c.fetchone()

player_wishlists.append(black_wishlist[0])

for i in range(len(players)):
    print(players[i], "has a collection wishlist total of", player_wishlists[i])

# Using the previous data from the queries to find the
# average wishlist value per card of each player's collection
for i in range(len(players)):
    print(players[i], "has an average wishlist value per card of", (players_collection_sizes[i]/player_wishlists[i]))

# Query to find how many cards are maxed out in customization
c.execute("SELECT * from master where quality = 4 AND dye_code is not NULL and dye_name is not NULL and frame is not NULL and morphed = 'Yes' and trimmed = 'Yes' AND nickname is not NULL;")
maxed_cards = c.fetchall()
print(maxed_cards)

# Query to find how many cards are decently customized
c.execute("SELECT * from master where quality = 4 AND dye_code is not NULL and dye_name is not NULL and frame is not NULL;")
decent_cards = c.fetchall()
print(decent_cards)

# Query to find the breakdown of how many decently customized cards
# there are and sorting it in descending order by the amount owned per player
c.execute("SELECT COUNT(*) from master where quality = 4 AND dye_code is not NULL and dye_name is not NULL and frame is not NULL;")
total_decent_cards = c.fetchall()
print(total_decent_cards[0][0])

c.execute("SELECT owner, COUNT(*) as total from master where quality = 4 AND dye_code is not NULL and dye_name is not NULL and frame is not NULL GROUP by owner order by total DESC;")
player_decent_cards = c.fetchall()
print(player_decent_cards)

# Finished :D
conn.commit()
conn.close()