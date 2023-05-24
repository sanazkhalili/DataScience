from fastapi import APIRouter, Depends
from dependencies import get_db
from sqlalchemy.orm import Session
from models import book as book_model
from schemas import  book_schema
from fastapi import HTTPException

route = APIRouter()


@route.post("/add_readbook")
def add_readbook(book:book_schema.BookSCh ,db:Session=Depends(get_db)):
    print()
    new_book = book_model.ReadBook(name=book.name ,price=book.price ,subject= book.subject
                                    ,author=book.author ,start_date=book.start_date ,stop_date=book.stop_date
                                      ,end_status=book.end_status ,favorit_status=book.end_status)
    
    db.add(new_book)
    db.flush()
    db.commit()
    db.refresh(new_book)
    return "It is saved"


@route.post("/add_note_book")
def add_readbook(book:book_schema.NoteBook ,db:Session=Depends(get_db)):
    test_exist = db.query(book_model.ReadBook).filter(book_model.ReadBook.id==book.id_book).first()
    print(test_exist)
    if test_exist is None:
        raise HTTPException(detail="this is error", status_code=400)
    
    new_book = book_model.NoteBook(id_book=book.id_book, context=book.context)
    db.add(new_book)
    db.flush()
    db.commit()
    db.refresh(new_book)
    return "It is saved"



def get_note(db:Session, id:int):
    return db.query(book_model.NoteBook).filter(book_model.NoteBook.id_book == id).all()


@route.get('/one_book/{id_book}')
def get_book(id_book:int, db:Session=Depends(get_db)):

    note = get_note(db, id_book)
    book = db.query(book_model.ReadBook).filter(book_model.ReadBook.id == id_book).first()
    
    return book_schema.ShowBookWithNote(notebook=note, test=book_schema.BookSCh(**vars(book)))

@route.get('/all_note')
def get_all_note(db:Session=Depends(get_db)):
    return db.query(book_model.NoteBook).filter(book_model.NoteBook.id_book == 1).all()
