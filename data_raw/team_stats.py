import pandas as pd

team_stats_header = ["name", "total_matches", "runs_scored", "batting_average", "num_centuries", "num_fifties",
                     "num_wickets_taken", "bowling_average", "five_wickets_haul"]

afghanistan_team_stats = [
    ["Hashmatullah Shahidi", 105, 3251, 31.77, 5, 17, 0, 0, 0],
    ["Rahmanullah Gurbaz", 26, 814, 31.00, 1, 6, 0, 0, 0],
    ["Ibrahim Zadran", 15, 327, 21.80, 0, 2, 0, 0, 0],
    ["Riaz Hassan", 8, 60, 7.50, 0, 0, 4, 21.50, 1],
    ["Rahmat Shah", 100, 3681, 37.30, 7, 18, 0, 0, 0],
    ["Najibullah Zadran", 76, 1964, 25.85, 1, 11, 0, 0, 0],
    ["Mohammad Nabi", 129, 4510, 34.96, 11, 22, 137, 29.80, 5],
    ["Ikram Alikhil", 10, 105, 10.50, 0, 0, 0, 0, 0],
    ["Azmatullah Omarzai", 7, 110, 15.71, 0, 0, 0, 0, 0],
    ["Rashid Khan", 76, 1801, 23.69, 0, 9, 163, 28.11, 5],
    ["Mujeeb ur Rahman", 30, 284, 9.46, 0, 1, 48, 29.17, 2],
    ["Noor Ahmad", 21, 212, 10.60, 0, 1, 35, 31.40, 1],
    ["Fazalhaq Farooqi", 28, 480, 17.14, 0, 2, 57, 29.75, 3],
    ["Abdul Rahman", 15, 126, 8.40, 0, 0, 27, 32.85, 1],
    ["Naveen-ul-Haq", 25, 361, 14.44, 0, 1, 50, 35.00, 2],
]

australia_team_stats = [
    ["Pat Cummins", 110, 1882, 20.91, 1, 10, 159, 30.28, 5],
    ["Steve Smith", 145, 4943, 35.05, 12, 26, 0, 0, 0],
    ["Alex Carey", 107, 2880, 27.27, 2, 19, 0, 0, 0],
    ["Josh Inglis", 15, 429, 28.60, 0, 2, 0, 0, 0],
    ["Sean Abbott", 24, 454, 18.16, 0, 2, 43, 34.35, 2],
    ["Cameron Green", 10, 282, 28.20, 0, 1, 15, 34.66, 1],
    ["Josh Hazlewood", 116, 2198, 19.87, 1, 11, 200, 27.75, 5],
    ["Travis Head", 113, 3509, 31.54, 4, 16, 0, 0, 0],
    ["Marnus Labuschagne", 92, 3668, 40.76, 12, 16, 0, 0, 0],
    ["Mitch Marsh", 79, 1937, 25.16, 1, 13, 55, 41.09, 3],
    ["Glenn Maxwell", 149, 3543, 32.05, 5, 25, 0, 0, 0],
    ["Marcus Stoinis", 76, 2032, 27.53, 2, 10, 74, 37.74, 3],
    ["David Warner", 141, 5734, 41.36, 19, 28, 0, 0, 0],
    ["Adam Zampa", 103, 121, 10.95, 0, 0, 121, 25.58, 5],
    ["Mitchell Starc", 104, 2634, 25.45, 2, 19, 190, 27.06, 5]
]

bangladesh_team_stats = [
    ["Shakib Al Hasan", 237, 6983, 31.25, 10, 48, 277, 30.71, 10],
    ["Litton Das", 97, 3140, 32.31, 6, 21, 0, 0, 0],
    ["Najmul Hossain Shanto", 42, 1719, 40.93, 4, 10, 0, 0, 0],
    ["Mahmudullah Riyad", 232, 7033, 32.23, 8, 51, 0, 0, 0],
    ["Mushfiqur Rahim", 247, 7130, 30.97, 8, 43, 0, 0, 0],
    ["Mehidy Hasan Miraz", 70, 1077, 15.40, 0, 5, 107, 31.20, 5],
    ["Mahedi Hasan", 47, 604, 12.65, 1, 2, 66, 33.63, 3],
    ["Taskin Ahmed", 82, 144, 16.95, 0, 0, 105, 28.91, 5],
    ["Mustafizur Rahman", 72, 107, 14.29, 0, 0, 111, 26.48, 5],
    ["Nasum Ahmed", 57, 86, 14.33, 0, 0, 95, 24.94, 5],
    ["Shoriful Islam", 22, 48, 24.00, 0, 0, 34, 32.11, 1],
    ["Tanzim Hasan Sakib", 10, 12, 12.00, 0, 0, 15, 30.00, 1]
]

england_team_stats = [
    ["Jos Buttler", 153, 5371, 36.72, 20, 26, 0, 0, 0],
    ["Jonny Bairstow", 115, 4527, 40.24, 11, 21, 0, 0, 0],
    ["Jason Roy", 102, 4432, 46.64, 17, 20, 0, 0, 0],
    ["Joe Root", 155, 6062, 45.77, 24, 34, 0, 0, 0],
    ["Ben Stokes", 102, 2919, 35.30, 19, 17, 0, 0, 0],
    ["Moeen Ali", 132, 3114, 25.26, 19, 21, 0, 0, 0],
    ["Liam Livingstone", 49, 1117, 22.34, 10, 18, 0, 0, 0],
    ["Sam Curran", 38, 713, 18.77, 0, 5, 59, 26.20, 2],
    ["Reece Topley", 23, 320, 13.65, 0, 1, 51, 26.50, 2],
    ["David Willey", 59, 995, 16.96, 0, 10, 87, 27.13, 3],
    ["Chris Woakes", 162, 3816, 24.04, 0, 1, 221, 28.42, 5],
    ["Adil Rashid", 131, 2021, 15.47, 0, 5, 202, 28.17, 5],
    ["Jofra Archer", 18, 175, 9.72, 0, 1, 24, 28.80, 1],
    ["Phil Salt", 12, 325, 27.08, 1, 3, 0, 0, 0],
    ["Matthew Parkinson", 9, 103, 11.44, 0, 1, 16, 26.00, 1],
]

india_team_stats = [
    ["Rohit Sharma", 246, 9782, 48.91, 29, 46, 22, 52.50, 0],
    ["Hardik Pandya", 79, 1753, 27.64, 0, 11, 74, 35.37, 2],
    ["Shubman Gill", 29, 1282, 49.28, 2, 8, 0, 0, 0],
    ["Virat Kohli", 262, 12311, 50.39, 43, 64, 0, 0, 0],
    ["Shreyas Iyer", 44, 1689, 40.22, 3, 12, 0, 0, 0],
    ["Ishan Kishan", 19, 607, 31.95, 1, 3, 0, 0, 0],
    ["KL Rahul", 54, 2002, 37.07, 4, 12, 0, 0, 0],
    ["Suryakumar Yadav", 26, 1034, 41.36, 1, 9, 0, 0, 0],
    ["Ravindra Jadeja", 179, 2534, 32.51, 1, 16, 247, 36.47, 10],
    ["Shardul Thakur", 40, 121, 12.10, 0, 0, 62, 42.20, 1],
    ["Jasprit Bumrah", 73, 113, 16.14, 0, 0, 128, 24.89, 5],
    ["Mohammed Shami", 91, 208, 19.76, 0, 0, 156, 25.90, 5],
    ["Mohammed Siraj", 26, 36, 12.00, 0, 0, 48, 32.27, 1],
    ["Kuldeep Yadav", 86, 132, 15.34, 0, 0, 113, 27.43, 6]
]

netherlands_team_stats = [
    ["Scott Edwards", 86, 2711, 31.75, 4, 18, 0, 0, 0],
    ["Max O'Dowd", 91, 2991, 32.86, 4, 19, 0, 0, 0],
    ["Bas de Leede", 39, 1154, 29.61, 2, 6, 0, 0, 0],
    ["Vikram Singh", 44, 1395, 31.68, 3, 8, 0, 0, 0],
    ["Teja Nidamanuru", 46, 1204, 26.14, 1, 6, 0, 0, 0],
    ["Paul van Meekeren", 57, 1013, 17.75, 0, 10, 68, 33.00, 3],
    ["Colin Ackermann", 43, 1094, 25.42, 2, 6, 47, 30.86, 2],
    ["Roelof van der Merwe", 92, 1710, 18.60, 1, 9, 107, 31.20, 5],
    ["Logan van Beek", 48, 831, 17.30, 0, 1, 58, 28.09, 2],
    ["Aryan Dutt", 15, 259, 17.27, 0, 1, 18, 29.00, 1],
    ["Ryan Klein", 43, 732, 17.05, 0, 3, 51, 31.50, 2],
    ["Wesley Barresi", 10, 146, 14.60, 0, 0, 0, 0, 0],
    ["Saqib Zulfiqar", 15, 192, 12.80, 0, 1, 21, 33.50, 1],
    ["Shariz Ahmad", 10, 105, 10.50, 0, 0, 12, 27.00, 1],
    ["Sybrand Engelbrecht", 12, 161, 13.41, 0, 0, 0, 0, 0],
]

new_zealand_team_stats = [
    ["Kane Williamson", 155, 7068, 45.77, 24, 34, 0, 0, 0],
    ["Tom Latham", 145, 4605, 33.28, 12, 28, 0, 0, 0],
    ["Devon Conway", 29, 1282, 49.28, 2, 8, 0, 0, 0],
    ["Glenn Phillips", 29, 1034, 41.36, 1, 9, 0, 0, 0],
    ["Trent Boult", 133, 3051, 22.34, 0, 1, 290, 27.35, 5],
    ["Tim Southee", 186, 3770, 20.32, 0, 1, 402, 26.22, 5],
    ["Mitchell Santner", 94, 1567, 21.48, 2, 8, 145, 32.99, 2],
    ["Jimmy Neesham", 80, 1753, 27.64, 0, 11, 154, 34.07, 3],
    ["Daryl Mitchell", 79, 2646, 37.87, 4, 16, 0, 0, 0],
    ["Will Young", 29, 1282, 49.28, 2, 8, 0, 0, 0],
    ["Mark Chapman", 38, 1065, 28.00, 2, 4, 0, 0, 0],
    ["Rachin Ravindra", 15, 301, 20.07, 0, 0, 18, 29.00, 1],
    ["Lockie Ferguson", 62, 1282, 20.68, 0, 0, 99, 25.44, 5],
    ["Ish Sodhi", 103, 1394, 13.50, 0, 0, 121, 27.43, 6],
    ["Matt Henry", 53, 1441, 27.19, 0, 0, 88, 32.29, 3]
]

pakistan_team_stats = [
    ["Babar Azam", 115, 6632, 59.89, 17, 35, 0, 0, 0],
    ["Fakhar Zaman", 76, 3365, 45.82, 10, 18, 0, 0, 0],
    ["Imam-ul-Haq", 71, 3301, 47.83, 8, 21, 0, 0, 0],
    ["Mohammad Rizwan", 80, 3145, 39.31, 5, 22, 0, 0, 0],
    ["Haris Rauf", 48, 1193, 24.85, 0, 0, 96, 25.83, 5],
    ["Shaheen Shah Afridi", 36, 821, 22.80, 0, 0, 73, 23.85, 5],
    ["Hasan Ali", 63, 1384, 22.00, 0, 0, 118, 24.06, 5],
    ["Mohammad Nawaz", 23, 476, 20.21, 0, 1, 31, 38.10, 1],
    ["Iftikhar Ahmed", 58, 1542, 26.70, 1, 10, 0, 0, 0],
    ["Asif Ali", 50, 1152, 23.04, 1, 6, 0, 0, 0],
    ["Shadab Khan", 65, 1187, 18.34, 0, 8, 110, 31.20, 5],
    ["Faheem Ashraf", 44, 620, 14.11, 0, 4, 68, 34.73, 3],
    ["Mohammad Wasim Jr.", 12, 229, 19.08, 0, 0, 21, 33.43, 1],
    ["Khushdil Shah", 15, 216, 14.40, 0, 1, 18, 34.00, 1],
    ["Sarfaraz Ahmed", 106, 3532, 36.25, 5, 20, 0, 0, 0],
]

south_africa_team_stats = [
    ["Temba Bavuma", 107, 4201, 40.00, 6, 28, 0, 0, 0],
    ["Quinton de Kock", 139, 5991, 46.18, 17, 28, 0, 0, 0],
    ["Reeza Hendricks", 98, 3446, 35.23, 6, 20, 0, 0, 0],
    ["Rassie van der Dussen", 71, 3216, 47.40, 6, 21, 0, 0, 0],
    ["Aiden Markram", 85, 3496, 41.25, 5, 22, 0, 0, 0],
    ["David Miller", 151, 4037, 32.51, 5, 23, 0, 0, 0],
    ["Marco Jansen", 39, 750, 19.23, 0, 3, 54, 31.85, 2],
    ["Kagiso Rabada", 97, 2395, 24.70, 1, 13, 174, 26.32, 5],
    ["Anrich Nortje", 40, 520, 13.00, 0, 2, 67, 24.18, 3],
    ["Lungi Ngidi", 65, 1169, 18.14, 0, 2, 110, 28.09, 5],
    ["Tabraiz Shamsi", 73, 1092, 15.57, 0, 5, 100, 28.17, 5],
    ["Keshav Maharaj", 58, 875, 15.08, 0, 3, 109, 29.63, 4],
    ["Gerald Coetzee", 7, 138, 19.71, 0, 0, 13, 31.54, 1],
    ["Heinrich Klaasen", 36, 1164, 33.29, 2, 6, 0, 0, 0],
    ["Andile Phehlukwayo", 113, 1492, 13.28, 0, 9, 118, 32.36, 3],
]

sri_lanka_team_stats = [
    ["Dasun Shanaka", 125, 3761, 30.09, 6, 19, 0, 0, 0],
    ["Kusal Mendis", 108, 3915, 36.09, 6, 20, 0, 0, 0],
    ["Pathum Nissanka", 89, 3021, 33.95, 5, 18, 0, 0, 0],
    ["Charith Asalanka", 81, 2707, 33.85, 3, 16, 0, 0, 0],
    ["Dhananjaya de Silva", 114, 3697, 32.77, 7, 18, 0, 0, 0],
    ["Wanindu Hasaranga", 95, 2917, 30.75, 4, 17, 0, 0, 0],
    ["Chamika Karunaratne", 57, 1154, 20.33, 0, 1, 68, 33.00, 3],
    ["Dushmantha Chameera", 76, 1523, 19.97, 0, 1, 119, 26.46, 5],
    ["Lahiru Kumara", 58, 1133, 19.58, 0, 1, 98, 26.97, 5],
    ["Maheesh Theekshana", 34, 537, 15.80, 0, 2, 60, 27.75, 3],
    ["Jeffrey Vandersay", 45, 701, 15.58, 0, 4, 71, 24.83, 3],
    ["Kasun Rajitha", 32, 532, 16.62, 0, 2, 54, 27.19, 3],
    ["Kusal Perera", 123, 4015, 32.68, 5, 22, 0, 0, 0],
    ["Ashen Bandara", 10, 159, 15.90, 0, 1, 15, 30.00, 1],
    ["Binura Fernando", 12, 161, 13.41, 0, 0, 0, 0, 0],
]

# CREATING PANDAS DATAFRAME FOR ABOVE STATS.
afghanistan_stats = pd.DataFrame(afghanistan_team_stats, columns=team_stats_header)
australia_stats = pd.DataFrame(australia_team_stats, columns=team_stats_header)
bangladesh_stats = pd.DataFrame(australia_team_stats, columns=team_stats_header)
england_stats = pd.DataFrame(england_team_stats, columns=team_stats_header)
india_stats = pd.DataFrame(india_team_stats, columns=team_stats_header)
netherlands_stats = pd.DataFrame(netherlands_team_stats, columns=team_stats_header)
new_zealand_stats = pd.DataFrame(new_zealand_team_stats, columns=team_stats_header)
pakistan_stats = pd.DataFrame(pakistan_team_stats, columns=team_stats_header)
south_africa_stats = pd.DataFrame(south_africa_team_stats, columns=team_stats_header)
sri_lanka_stats = pd.DataFrame(sri_lanka_team_stats, columns=team_stats_header)

# DICTIONARY OF TEAM NAME AS KEY AND STATS DATAFRAME AS VALUE
all_team_stats = {"afghanistan": afghanistan_stats, "australia": australia_stats, "bangladesh": bangladesh_stats,
                  "england": england_stats, "india": india_stats, "netherlands": netherlands_stats,
                  "new_zealand": new_zealand_stats, "pakistan": pakistan_stats, "south_africa": south_africa_stats,
                  "sri_lanka": sri_lanka_stats}

all_countries_stats = pd.concat([
    afghanistan_stats.insert(0, "country", "afghanistan"),
    australia_stats.insert(0, "country", "australia"),
    bangladesh_stats.insert(0, "country", "bangladesh"),
    england_stats.insert(0, "country", "england"),
    india_stats.insert(0, "country", "india"),
    netherlands_stats.insert(0, "country", "netherlands"),
    new_zealand_stats.insert(0, "country", "new_zealand"),
    pakistan_stats.insert(0, "country", "pakistan"),
    south_africa_stats.insert(0, "country", "south_africa"),
    sri_lanka_stats.insert(0, "country", "sri_lanka"),
])
