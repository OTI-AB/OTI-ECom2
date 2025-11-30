from .cart import Cart

# Create context processor
def cart(request):
    # Return default data
    return {'cart': Cart(request)}