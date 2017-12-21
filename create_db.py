import sqlite3
from scraper import Scraper

sc = Scraper()

DATABASE = "diviapp.db"

with sqlite3.connect(DATABASE) as conn:
	# get cursor
	c = conn.cursor()

	# dropping all tables
	c.execute("DROP TABLE IF EXISTS line_stop")
	c.execute("DROP TABLE IF EXISTS line")
	c.execute("DROP TABLE IF EXISTS stop")

	# creating tables "arret", "ligne" and "arret_ligne"
	# table arret
	c.execute(
		""" 
		CREATE TABLE stop (
			stop_id INTEGER PRIMARY KEY AUTOINCREMENT,
			stop_totem TEXT NOT NULL,
			stop_name INTEGER NOT NULL
		)
		"""
	)

	# table ligne
	c.execute(
		""" 
		CREATE TABLE line (
			line_id INTEGER PRIMARY KEY,
			line_name TEXT NOT NULL,
			destination TEXT NOT NULL
		)
		"""
	)

	c.execute(
		"""
		CREATE TABLE line_stop(
			stop_totem INTEGER NOT NULL,
			line_id INTEGER NOT NULL,
			PRIMARY KEY(stop_totem, line_id),
			FOREIGN KEY(stop_totem) REFERENCES stop(stop_totem),
			FOREIGN KEY(line_id) REFERENCES line(line_id)
		)
		"""
	)

	c.executemany("INSERT INTO line VALUES (?, ?, ?)", sc.get_lines("tuples"))

	c.executemany("INSERT INTO stop(stop_totem, stop_name) VALUES (?, ?)", sc.get_stops("tuples"))

	c.executemany("INSERT INTO line_stop VALUES (?, ?)", sc.get_datas(["stop_totem", "line_id"], "tuples"))