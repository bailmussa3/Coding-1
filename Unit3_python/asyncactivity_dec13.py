
def shppingDiscont(membership, itemName, itemPrice):
     if membership =='supershopper':
         print('you will get 10 percent off  your item.')
         discountAMount = itemPrice * 0.15
         pritn(discountAmount)
         finalAmount =
         elif membership== 'megashppoer':
            print('you will get 15 percent off your item')
         elif membership== 'megashppoer':
            print('you will get 20 percent off your item')
        else:
            print(' you do not have any memebership benefits')

            shippingdiscount('')



        
        
        def membership_discount(membership, item item_price):
    discounts = {
        "superShopper": 0.10,
        "megaShopper": 0.15,
        "ultraShopper": 0.20
    }

    membership ()

    if membership in discounts:
        discount_amount = item_price * discounts[membership_type]
        final_price = item_price - discount_amount
        return "Congratulations {membership}, you saved ${discount_amount} on this {item}. Your final item price is ${final_price:}."
    else:
        return "Invalid membership."

# Example usage
print(membership_discount("superShopper", "TV", 100))  # Output: "Congratulations superShopper, you saved $10.00 on this TV. Your final item price is $90.00."
print(membership_discount("megaShopper", "Laptop", 200))  # Output: "Congratulations megaShopper, you saved $30.00 on this Laptop. Your final item price is $170.00."
print(membership_discount("ultraShopper", "Smartphone", 500))  # Output: "Congratulations ultraShopper, you saved $100.00 on this Smartphone. Your final item price is $400.00."
