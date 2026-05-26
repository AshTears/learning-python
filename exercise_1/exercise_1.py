# Stock Transaction Program

# Initial variables
no_of_shares = 1000
commission = 0.02

# Stock purchase
purchase_amount = no_of_shares * 32.87
commission_on_purchase = purchase_amount * commission
total_cost = purchase_amount + commission_on_purchase
print("The total cost of the stocks purchased is:", total_cost)

# Stock sale
sale_amount =  no_of_shares * 33.92
commission_on_sale = sale_amount * commission
amount_received = sale_amount - commission_on_sale
print("The amount received after selling the stock:", amount_received)

# Profit/Loss
profit_loss = amount_received - total_cost
print("The profit made on the sale is:", profit_loss)


