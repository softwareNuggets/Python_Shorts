
import csv
import sqlite3

def create_database(conn, cur):

	cur.execute("""
		create table if not exists florida
		(
			year 		int,
			month 		int,
			day 		int,
			rain 		float,
			max_temp 	float,
			min_temp	float,
			mean_temp	float
		)
	""")
	
	cur.execute("""
		create unique index if not exists
			temp_line_index on florida(year, month, day)
		""")
	conn.commit()

def process_file(conn,cur, filename):
		with open(filename, "rt") as f:
			reader = csv.reader(f)
			next(csv.reader(f),None)
			
			for entry in reader:
			
				try:
					#print(reader.line_num)
					record = (entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6])
					
					#build sql insert statement
					stmt = "insert into florida(year, month, day,rain, max_temp, min_temp,mean_temp)";
					stmt += " values(?,?,?,?,?,?,?);"
					
					#execute statement with tuple data
					cur.execute(stmt, record)
					
					if cur.lastrowid %100 == 0:
						conn.commit()
						
				except csv.Error as e:
					print(f'Line:{reader.line_num}, Record:{record}')
					

if __name__ == "__main__":
	conn = sqlite3.connect('FL_temps.db')
	cur = conn.cursor()
	create_database(conn, cur)
	process_file(conn, cur, "FL_temps.csv")
	conn.commit()
	conn.close()
	print("job complete")
