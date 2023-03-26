"""
Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result."""
price=float(input("Price: "))
a=input("Are you prime member? " )
def cdp(price, a):
    if (a=="yes" or a=="Yes" or a=="YES"):
        d1 = 0.15*price
        p_a_d1= price-d1
        d2= 0.08*p_a_d1
        p_a_d2=p_a_d1-d2
        return p_a_d2
    else:
        b_f_d=0.08*price
        f_p= price-b_f_d
        return f_p
print("Your final price after calculating all discounts is Rs",cdp(price,a))