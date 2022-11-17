__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


from models import *

"""Search for products based on a term. Searching for 'sweater' should yield all products that have the word 'sweater' in the name. This search should be case-insensitive"""

def search(term):
    term = term.lower()
    if not (query := Products.select().where(Products.name.contains(term) | Products.description.contains(term))):
         return  "product not Found" 
    result = [(product.name, product.description) for product in query]
    return  result 

"""View the products of a given user."""

def list_user_products(user_id):
    query = (Products
            .select(Products, Users)
            .join(Users)
            .where(Products.ownerID ==user_id))
    for product in query:
        return product.name, product.ownerID.name

"""View all products for a given tag"""
def list_products_per_tag(tag):
    """View all products for a given tag."""
    result = []
    query = (ProductTags.select(ProductTags,Products).join(Products).where(ProductTags.product_id==Products.id))
    for prod in query:
        if prod.tag_id_id == tag:
            result.append(prod.product_id.name)
    return result 
       

"""add a product to a user."""
def add_product_to_catalog(user_id, prod,decscr,am, selprice):
    try:
        queryUser =  Users.select(Users).where(Users.id == user_id).exists()
        queryProducts =  Products.select(Products).where(fn.LOWER(Products.name) == fn.LOWER(prod)).exists()
        if queryUser == False:
            return  print("No such User in datase add user first")
        """User exists add product to user"""
        Products.create( name = prod,description=decscr,ownerID =user_id,amount= am, selling_Price= selprice)
        return prod ,decscr,user_id, am, selprice

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
  
     


def purchase_product(product_id, buyer_id, quantity):
    queryProducts = Products.select().where(Products.id==product_id )
    if queryProducts.exists():
        for prod in queryProducts:
            if prod.amount< quantity:
                return ("niet genoeg voorraad")
            update_stock(product_id,-quantity)
            Orders.create(customer=buyer_id, amount=quantity,product_name=prod.name)
        return buyer_id, quantity, prod.name
    


"""UnComment functie call to get result"""
# if __name__ == "__main__":

#     print(f" Searchresult: {search('PAUL')} ")

# """Param: userid"""
# print(f" list user-products :{list_user_products(1)}")


# """Param Tagname"""
# print(f" list product per tag :{list_products_per_tag('gibson')}")
# print(f" list product per tag :{list_products_per_tag('electrische gitaar')}")



# """PARAMs:  userOwnerID , name, decription, amount, selling_price,"""

# print(f" add product to catalog :{add_product_to_catalog(1 ,'gibson les paul', 'Body vorm Solid',4,3.899)}")
 
# """ param productid"""
# remove_product(1)

# """params: prodid, amount"""
# update_stock(6,2)
# # """params: product.id, buyer.id, quantity"""

# print(f"purchase: {purchase_product(6,2,2)}")


