__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


from models import *

"""Search for products based on a term. Searching for 'sweater' should yield all products that have the word 'sweater' in the name. This search should be case-insensitive"""

def search(term):
    term = term.lower()
    if not (query := Products.select().where(Products.name.contains(term) | Products.description.contains(term))):
         return print("product not Found")
    result = [(product.name, product.description) for product in query]
    return  print(f" Searchresult: {result} ")

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
    
    query = (ProductTags.select(ProductTags,Tags).join(Tags).where(Tags.id==tag_id))

    for prod in query:
       return print(f" products per tag {prod.product_id.name}")

"""add a product to a user."""
def add_product_to_catalog(user_id, prod,decscr,am,unit_price, selprice,tag_id):
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
                    return  print("Product bestaat al")        
        """User exists add product to user"""
        return  Products.create( name = prod,description=decscr,ownerID =user_id,amount= am, price_per_Unit=unit_price, selling_Price= selprice,tag_id=tag_id )

    except Exception as e:
        print(e)

def remove_product(product_id):
    queryProduct =  Products.select(Products).where((Products.id) == product_id).exists()
    tagsquery= ProductTags.select(ProductTags).where(ProductTags.product_id== product_id)
    if queryProduct:
        product = Products.get(Products.id == product_id)
        """first remove producttags"""
        for tag in  tagsquery:
            tag.delete_instance()
        product.delete_instance()


def update_stock(product_id, new_quantity):
    queryProducts = Products.select(Products).where(Products.id==product_id )
    if queryProducts.exists():
        prod = Products.get(Products.id == product_id)
        old_amount = prod.amount
        new_amount = old_amount + new_quantity
        update_Amount = Products( id =product_id ,amount=new_amount)
        """ check of updated amount geen negatief number is"""
        if update_Amount.amount >= 0:
            update_Amount.save(only=[Products.amount])
        else:
            return print(f"Amount kan niet null of negatief zijn max aantal product in stock = {old_amount}") 
    else: 
        return print("product bestaat niet")
    #   Products.update(Products.amount).where(Products.amount=new_amount)
     


def purchase_product(product_id, buyer_id, quantity):
    queryProducts = Products.select(Products).where(Products.id==product_id )
    if queryProducts.exists():
     Orders.create(customer=buyer_id, amount=quantity)
     update_stock(product_id,quantity)
     return


search("PAUL")
list_user_products(1)

# geef als param id van product mee 
list_products_per_tag(10)
"""PARAMs:  userOwnerID , name, decription, amount, price per unit, selling_price,"""
add_product_to_catalog(1 ,'gibson les paul', "Body vorm Solid",4,2.899,3.899,10)
"""parm: productid"""
remove_product(2)
"""params: prodid, amount"""
update_stock(6,2)
"""params: product.id, buyer.id, quantity"""
purchase_product(1,2,2)


