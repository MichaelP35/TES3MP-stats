#!/usr/bin/python3
import requests
import datetime

master_servers = [
    "https://master.tes3mp.com/api/servers/info",
    "http://master.tes3mp.com:8080/api/servers/info",
    "http://master.tes3mp.com:8081/api/servers/info"
]


# Fetches states.
def getstats(entrypoint):
    try:
        stats = requests.get(entrypoint, verify=False, timeout=15).json()
    except requests.exceptions.RequestException:
        stats = {'servers': 0, 'players': 0}
    return stats


# Appends data.
def registercount(stats, array, prop):
    array.append(stats[prop])


# Main script. Fetches the data using "getstats", Appends the data using "registercount",
# then writes the data into "stats.csv".
def main():
    player_counts = []
    server_counts = []
    date_raw = datetime.datetime.utcnow()
    date = '{d.year}-{d.month:02}-{d.day:02} {d.hour:02}:{d.minute:02}'.format(d=date_raw)

    for entrypoint in master_servers:
        stats = getstats(entrypoint)
        registercount(stats, player_counts, 'players')
        registercount(stats, server_counts, 'servers')
    line = "%s,%s,%s\n" % (date, sum(server_counts), sum(player_counts))
    csv_file = open('stats.csv', 'a')
    csv_file.write(line)
    csv_file.close()


if __name__ == "__main__":
    main()
