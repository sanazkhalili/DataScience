from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Boolean, Text, Enum
from database import Base
import enum

class subjects(str, enum.Enum):
    novel = "novel"
    psychology = "psychology"
    english = "english"
    computer = "computer"



class ReadBook(Base):
    __tablename__="readbook"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    subject = Column(Enum(subjects))
    author = Column(String(50))
    start_date = Column(Date)
    stop_date = Column(Date)
    end_status = Column(Boolean)
    favorit_status = Column(Boolean)


class SuggestionBook(Base):
    __tablename__="suggestionbook"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    author = Column(String(50))
    who = Column(String(50))
    subject = Column(Enum(subjects))


class NoteBook(Base):
    __tablename__="notebook"
    id = Column(Integer, primary_key=True, index=True)
    id_book = Column(Integer, ForeignKey("readbook.id"), nullable=False)
    context = Column(Text)
