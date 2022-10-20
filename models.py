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
    id = AutoField(primary_key=True,index = True)
    name = CharField()
    description = CharField()
    ownerID = ForeignKeyField(Users, backref='Products')
    amount = IntegerField()
    price_per_Unit = DecimalField(decimal_places=2, auto_round=True)
    selling_Price = DecimalField(decimal_places=2, auto_round=True)
    tag_id = IntegerField()
   


class Orders(Base):
    id = AutoField(primary_key=True)
    customer = ForeignKeyField(Users, backref='Orders')
    amount = IntegerField()

    

   

class Tags(Base):
    id = AutoField(primary_key=True)
    tagname = CharField(unique=True)
    categorie = CharField(unique= True)
   

class ProductTags(Base):
    product_id = ForeignKeyField(Products,backref='ProductsTags')
    tag_id = ForeignKeyField(Tags,backref='ProductsTags')

    