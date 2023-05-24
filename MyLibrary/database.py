from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import  sqlalchemy


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:sanaz11@localhost:3306/bookdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()
Base.metadata.create_all(bind=engine)

