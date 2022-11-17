import os

from models import *


def create_tables():
    with db:
        db.create_tables(
            [Users,
             Products,
             Tags,
             ProductTags,
             Orders
             ]
        )
        
create_tables();

"""id name adres billinginfo"""
persons = ( ("Bart","jan smitzlaan 6 5611 LE Eindhoven", "NLRabo 123456789"),
("Piet","violierstraat 25 5611 LE Eindhoven","NLRabo 123456789")
)

"""name description ownerid amount  selling_price """
products = (("fender stratocaster", "bouwjaar 1972",1,1, 2200),
("gibson les paul", "bouwjaar 1952",2,1, 500.25),
("ibanez les paul", "bouwjaar 1978",1,1, 500.25),
('Martin D 28', "Body vorm Dreadnought met cutaway Sparren bovenblad van les paul",2,3,3.899))

"""       tagname  """
tags = [("fender"),
("gibson"),
("ibanez"),
("martin")
,("electrische gitaar"),("acoustische gitaar")]

"""Referereert naar productid en tagid"""
products_tags=[(1,"fender"),(2,'gibson'),(3,'ibanez'),(4,'martin'),(1,'electrische gitaar'),(2,'electrische gitaar'),(3,'electrische gitaar'),(4, "acoustische gitaar")]

orders=[(2, 2),(1,2)]

for person in persons:
    Users.create( name = person[0],adres=person[1],billing = person[2])

for product in products:
    Products.create( name = product[0],description=product[1],ownerID = product[2],amount= product[3], selling_Price= product[4])

for tag in tags:
    Tags.create(tagname=tag)

for tag in products_tags:
    ProductTags.create(product_id=tag[0],tag_id=tag[1])


# for order in orders:
#     Orders.create(customer=tag[0],amount=tag[1])

    