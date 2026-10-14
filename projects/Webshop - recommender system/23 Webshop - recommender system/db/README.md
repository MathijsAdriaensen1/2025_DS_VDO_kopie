**Na uitvoeren init.sql**

De aangemaakte user webuser heeft nog geen rechten op de tabellen (deze stonden niet in het 
gegenereerde script).  Daarom moet je deze nog 'manueel' toevoegen.  Dit doe je als volgt:

*Uit te voeren in query console in pgAdmin*

-- Toegang tot de database
GRANT CONNECT ON DATABASE webshop TO webuser;

-- Toegang tot het public schema
GRANT USAGE ON SCHEMA public TO webuser;

-- Toegang om tabellen te lezen
GRANT SELECT ON ALL TABLES IN SCHEMA public TO webuser;

-- (optioneel) Toekomstige tabellen ook automatisch zichtbaar maken
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO webuser;

GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO webuser;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT INSERT, UPDATE, DELETE ON TABLES TO webuser;

*Einde script*