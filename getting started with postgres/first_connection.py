import psycopg2

# Verbinding maken
# Database connection parameters
conn = psycopg2.connect(
    dbname="postgres",  # of jouw database naam
    user="admin",  # standaard postgres gebruiker
    password="myPassWord",  # wachtwoord dat je hebt ingesteld in de compose file
    host="mypostgres",  # de containernaam in het netwerk is de host
    port="5432"  # standaard PostgreSQL-poort
)

# Cursor aanmaken
cur = conn.cursor()

# Een eenvoudige query uitvoeren
cur.execute("SELECT version();")

# Het resultaat ophalen
version = cur.fetchone()
print("Database versie:", version)