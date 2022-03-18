
#First given code snippets
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Create a total_price variable and set it to 0
total_price = 0

#Looping through the price list and add a each item to the total price
for price in prices:
  total_price += price

#Create an average_price variable that is the average of total_price
average_price = total_price/len(prices)

#Print the value of average_price
print("Average Haircut Price: " + str(average_price))

#Create new_prices which has all the element minus 5
new_prices = [price -5 for price in prices]

#Print new_prices
print(str(new_prices))


#REVENUE
#Create a new variable called total_revenue and set it to 0
total_revenue = 0

#Use for loop to create a variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
  total_revenue = prices[i] * last_week[i]

#Print total revenue
print("Total Revenue: " + str(total_revenue))

#daily_average_avenue is total_avenue divided by 7
daily_average_avenue = total_revenue / 7

#Print daily average
print(daily_average_avenue)

#cuts_under_30
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print(cuts_under_30)