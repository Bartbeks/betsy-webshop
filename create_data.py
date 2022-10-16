from models import *


def create_tables():
    with db:
        db.create_tables(
            [Users,
             Products,
             Orders,
             ProductTags,
            
             ]
        )
        
create_tables();


persons = ( ("Bart","jan smitzlaan 6 5611 LE Eindhoven", "NLRabo 123456789"),
("Piet","violierstraat 25 5611 LE Eindhoven","NLRabo 123456789")
)

products = (("fender stratocaster", "bouwjaar 1972",1,1,1900, 2200),("gibson les paul", "bouwjaar 1952",2,1,1900, 50000,25))


for person in persons:
    
    
    Users.create( name = person[0],adres=person[1],billing = person[2])

for product in products:
    print(product[0])
    
    Products.create( name = product[0],description=product[1],ownerID = product[2],amount= product[3], price_per_Unit=product[4], selling_Price= product[5])