import pyodbc, psycopg2, sys, sqlanydb
#sys.path.insert(0, 'C:/Users/Christian/Desktop/GitHub/')
#sys.path.insert(0, 'C:/Users/Reaper/Desktop/GitHub/')
import Connect as ct

#class DatabaseSync:
#	def __init__(noquery=None): #Initialze method
#		if sql is None:
#			noquery = "SELECT 'No Query'"
#		else:
#			noquery = sql
noquery = "SELECT 'No Query'"
		
def ESGrab(host,query=None):
	query = query or noquery #Use class query if no alternative
	try:
		esconn = sqlanydb.connect( #Establish Connection
			UID=ct.SAUID,
			PWD=ct.SAPWD,
			HOST=host,
			DBN=ct.SADatabase,
			ENG=ct.SAServer)
		escurs = esconn.cursor() #Create Cursor
		escurs.execute(query) #Execute query argument
		esresults = escurs.fetchall() #Fetch results of query
		escurs.close() #Close Cursor
		esconn.close() #Close Connection
		return esresults #Return stored results
	except:
		print("Could not connect to HOST: %s" % host)
		#If connect fails, return host IP

def PGSelect(query=None):
	query = query or noquery
	pgconn = psycopg2.connect( #Establish Connection to DB
		"dbname=%s user=%s host=%s password=%s" % 
		(ct.PGDatabase,ct.PGUID,ct.PGHost,ct.PGPWD))
	pgcurs = pgconn.cursor() #Create Cursor
	pgcurs.execute(query) #Execute query argument
	pgresults = pgcurs.fetchall() #Fetch query results
	pgcurs.close() #Close Cursor
	pgconn.close() #Close Connection
	return pgresults #Return stored results

def PGInsert(query):
	query = query or noquery #Use class query if no alternative
	pgconn = psycopg2.connect( #Establish Connection to DB
		"dbname=%s user=%s host=%s password=%s" %
		(ct.PGDatabase,ct.PGUID,ct.PGHost,ct.PGPWD))
	pgcurs = pgconn.cursor() #Create Cursor
	try: #Try INSERT Query
		pgcurs.execute(query) #Execute query argument
		pgconn.commit() #Commit INSERT
		#return print('INSERT Commited to Database')
	except:
		return print('Unable to execute INSERT query: %s' % query)
	pgcurs.close() #Close Cursor
	pgconn.close() #Close Connection

def PGInsertMany(query,list):
	query = query or noquery #Use class query if no alternative
	pgconn = psycopg2.connect( #Establish Connection to DB
		"dbname=%s user=%s host=%s password=%s" %
		(ct.PGDatabase,ct.PGUID,ct.PGHost,ct.PGPWD))
	pgcurs = pgconn.cursor() #Create Cursor
	try: #Try INSERT Query
		pgcurs.executemany(query,) #Execute query argument
		pgconn.commit() #Commit INSERT
		#return print('INSERT Commited to Database')
	except:
		return print('Unable to execute INSERT query: %s' % query)
	pgcurs.close() #Close Cursor
	pgconn.close() #Close Connection

def MSSelect(query=None):
	query = query or noquery #Use class query if no alternative
	msconn = pyodbc.connect( #Establish Connection with MS Database
		"Driver={%s};Server=%s;Database=%s;UID=%s;PWD=%s;" % 
		(ct.MSDriver,ct.MSServer,ct.MSDatabase,ct.MSUID,ct.MSPWD))
	mscurs = msconn.cursor() #Create Cursor
	mscurse.execute(query) #Execute Query
	msresults = mscurs.fetchall() #Fetch query results
	mscurs.close() #Close Cursor
	msconn.close() #Close Connection

def MSInsert(query=None):
	query = query or noquery #Use class query if no alternative
	msconn = pyodbc.connect( #Establish Connection with MS Database
		"Driver={%s};Server=%s;Database=%s;UID=%s;PWD=%s;" % 
		(ct.MSDriver,ct.MSServer,ct.MSDatabase,ct.MSUID,ct.MSPWD))
	mscurs = msconn.cursor() #Create Cursor
	try:
		mscurse.execute(query) #Execute INSERT Query
	except:
		print('Unable to execute INSERT query')
	mscurs.close() #Close Cursor
	msconn.close() #Close Connection