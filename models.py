# Models go here

from enum import unique
from peewee import *


# db = SqliteDatabase(":memory:")
db = SqliteDatabase("webshop.db",pragmas={'foreign_keys': 1})


class Base(Model):
    class Meta:
        database = db

class Users(Base):

   
    id = AutoField(primary_key=True)
    name = CharField()
    adres = CharField()
    billing = CharField()


    

class Products(Base):
 
    id = AutoField(primary_key=True)
    name = CharField()
    description = CharField()
    ownerID = ForeignKeyField(Users, backref='Products')
    amount = IntegerField()
    price_per_Unit = DecimalField()
    selling_Price = DecimalField()
   


class Orders(Base):
    id = AutoField(primary_key=True)
    customer = ForeignKeyField(Users.id, backref='Products')
    amount = IntegerField()

    
class ProductTags(Base):
    tagname = CharField(unique=True)
    categorie = CharField()
    product_owner_id = ForeignKeyField(Products, backref='ProductsTags')
    product_id = IntegerField()
    