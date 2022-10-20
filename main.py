__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"





from models import *

"""Search for products based on a term. Searching for 'sweater' should yield all products that have the word 'sweater' in the name. This search should be case-insensitive"""

def search(term):
    query = (Products.select().where(fn.LOWER(Products.name).contains(term.lower())))
    
    if query.exists():
        for prod in query:
            print(prod.name)
    
    else:
        print("product not found")


"""View the products of a given user."""

def list_user_products(user_id):
    query = (Products
            .select(Products, Users)
            .join(Users)
            .where(Products.ownerID ==user_id))
 
    for product in query:
        print(product.name, product.ownerID.name)




"""View all products for a given tag"""
def list_products_per_tag(tag_id):
    """View all products for a given tag."""
    query = (ProductTags.select(ProductTags,Products).join(Products).where(ProductTags.product_owner_id==tag_id))

    for prod in query:
        print(prod.tagname)

"""add a product to a user."""

def add_product_to_catalog(user_id, prod,decscr,am,unit_price, selprice):

    try:
         
        queryUser =  Users.select(Users).where(Users.id == user_id).exists()
        queryProducts =  Products.select(Products).where(fn.LOWER(Products.name) == fn.LOWER(prod)).exists()
      
        if queryUser == False:
            return  print("No such User in datase add user first")
        """Check of het product bestaat bij user """
        if queryProducts:
           query =  Products.select(Products).where(Products.ownerID == user_id)
           for product in query:
                if product.name == prod and product.ownerID_id==user_id:
                    return    print("Update Products")

        
        """User exists add product to user"""
        Products.create( name = prod,description=decscr,ownerID =user_id,amount= am, price_per_Unit=unit_price, selling_Price= selprice)

        """check if uniqe tag exist                    
        als die exists kijk of het dezelfde owner id heeft. een product kan verschillende owners hebben  als dat het geval is het geval is
        Dit moet een in het model een denk ik een extrat veld worden
        Moet dus ook data set aanpassen"""
        is_tag_exist = ProductTags.select(ProductTags).where(ProductTags.tagname==prod).exists()
        if is_tag_exist == False:
            ProductTags.create( tagname=prod, categorie= decscr,product_owner_id=user_id)
        else:
            query =  ProductTags.update(product_owner_id = user_id).where(ProductTags.tagname == prod)
            query.execute()
       
    except Exception as e:
        print(e)

def remove_product(product_id):
    queryProduct =  Products.select(Products).where((Products.id) == product_id).exists()
    if queryProduct:
        product = Products.get(Products.id == product_id)
        query = ProductTags.select(ProductTags).where(ProductTags.product_id==product_id)
        """remove tags for product in productstags """
        for tag in query:
            tag.delete_instance()

        product.delete_instance()



        
 
      


   
   
    




def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...

search("PAUL")
list_user_products(1)


# geef als param id van product mee 
list_products_per_tag(1)
add_product_to_catalog(2, 'Martin D 28', "Body vorm Dreadnought met cutaway Sparren bovenblad",4,2.899,3.899)
# add_product_to_catalog(2, 'Fender stratocaster de luxe', "Bouwjaar 1965",4,2.899,3.899)
# remove_product(1)