<<<<<<< HEAD
from fastapi import FastAPI, HTTPException, status
from mysql import connector
from pydantic import BaseModel
from enum import Enum



mydb = connector.connect(user = "root",
                  password = "sanaz11",
                  host = "192.168.120.192",
                  database = "classicmodels")
mycursor = mydb.cursor()
app = FastAPI()

@app.get("/home")
def get_user():
    list_name = []
    mycursor.execute("SELECT contactFirstName FROM customers")
    for c in mycursor:
        list_name.append(c[0])
    return list_name


@app.get("/getuser/{id}")
def get_user_id(id:int):
    list_customer = []
    query = "SELECT * FROM customers WHERE customerNumber = %s"
    mycursor.execute(query, (int(id),))
    for instance in mycursor:
        list_customer.append(instance)

    return list_customer


class OfficesAdd(BaseModel):
    city: str
    phone: str
    country: str


@app.post("/home/addoffice/")
def add_office(officeadd: OfficesAdd):
    try:
        query = "INSERT INTO offices (city, phone, country) VALUES(%s, %s, %s)"
        mycursor.execute(query, (officeadd.city, officeadd.phone ,officeadd.country))
        mydb.commit()
        return "success"
    except Exception as ex:
        raise HTTPException(ex, status_code=status.HTTP_304_NOT_MODIFIED)


=======
from fastapi import FastAPI, HTTPException, status
from mysql import connector
from pydantic import BaseModel
from enum import Enum



mydb = connector.connect(user = "root",
                  password = "sanaz11",
                  host = "192.168.120.192",
                  database = "classicmodels")
mycursor = mydb.cursor()
app = FastAPI()

@app.get("/home")
def get_user():
    list_name = []
    mycursor.execute("SELECT contactFirstName FROM customers")
    for c in mycursor:
        list_name.append(c[0])
    return list_name


@app.get("/getuser/{id}")
def get_user_id(id:int):
    list_customer = []
    query = "SELECT * FROM customers WHERE customerNumber = %s"
    mycursor.execute(query, (int(id),))
    for instance in mycursor:
        list_customer.append(instance)

    return list_customer


class OfficesAdd(BaseModel):
    city: str
    phone: str
    country: str


@app.post("/home/addoffice/")
def add_office(officeadd: OfficesAdd):
    try:
        query = "INSERT INTO offices (city, phone, country) VALUES(%s, %s, %s)"
        mycursor.execute(query, (officeadd.city, officeadd.phone ,officeadd.country))
        mydb.commit()
        return "success"
    except Exception as ex:
        raise HTTPException(ex, status_code=status.HTTP_304_NOT_MODIFIED)


>>>>>>> a756265572a35c9219f8292dee8ce0c36c6ef430
