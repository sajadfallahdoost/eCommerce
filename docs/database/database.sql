CREATE DATABASE "Backend" ;

CREATE USER "Backend_user" WITH PASSWORD 'sdjnnfejsajad3574nndfkd' ;

ALTER ROLE "Backend_user" SET client_encoding TO 'utf8' ;

ALTER ROLE "Backend_user" SET default_transaction_isolation TO 'read committed' ;

ALTER ROLE "Backend_user" SET timezone TO 'UTC' ;

ALTER USER "Backend_user" CREATEDB ;

GRANT ALL PRIVILEGES ON DATABASE Backend TO "Backend_user" ;

GRANT ALL ON schema public TO "Backend_user" ;

SELECT has_schema_privilege( 'Backend_user','public','CREATE') ;

ALTER DATABASE "Backend" OWNER TO "Backend_user" ;
