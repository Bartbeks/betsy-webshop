import os
os.remove("webshop.db")
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

"""name description ownerid amount price_per_unit selling_price tag_id"""
products = (("fender stratocaster", "bouwjaar 1972",1,1,1900, 2200,1),
("gibson les paul", "bouwjaar 1952",2,1,1900, 500.25,2),
("ibanez les paul", "bouwjaar 1978",1,1,1900, 500.25,3),
('Martin D 28', "Body vorm Dreadnought met cutaway Sparren bovenblad van les paul",2,3,2.899,3.899,4))

"""       tagname    categorie"""
tags = [("fender","straocaster"),
("1972","gibson",2),
("rosewood","ibanez les paul"),
("acoustic","Martin")]


"""Referereert naar productid en tagid"""
products_tags=[(1,1),(2,2),(3,3),(2,1)]

orders=[(2, 2),(1,2)]

for person in persons:
    Users.create( name = person[0],adres=person[1],billing = person[2])

for product in products:
    Products.create( name = product[0],description=product[1],ownerID = product[2],amount= product[3], price_per_Unit=product[4], selling_Price= product[5],tag_id =product[6])

for tag in tags:
    Tags.create(  tagname=tag[0],categorie=tag[1])
for tag in products_tags:
    ProductTags.create(product_id=tag[0],tag_id=tag[1])
# for order in orders:
#     Orders.create(customer=tag[0],amount=tag[1])

    