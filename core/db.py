from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ
#from dotenv.main import load_dotenv

#load_dotenv()
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:7569@svc.sel4.cloudtype.app:31144/codewarrior"

# format : "사용하는db:/{username}:{password}@{host}:{port}/{db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
