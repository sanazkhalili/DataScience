from typing import List
from pydantic import BaseModel
import datetime
import enum

class Subject(str, enum.Enum):
    novel = "novel"
    psychology = "psychology"
    english = "english"
    computer = "computer"

class BookSCh(BaseModel):
    name : str
    price : int
    subject : Subject
    author : str
    start_date : datetime.date
    stop_date : datetime.date
    end_status : bool
    favorit_status : bool

    class Config():
        orm_mode=True


class NoteBook(BaseModel):
    id_book:int 
    context:str 

    class Config():
        orm_mode=True


class ShowBookWithNote(BaseModel):
    test: BookSCh
    notebook : List[NoteBook]

    class Config():
        orm_mode=True





