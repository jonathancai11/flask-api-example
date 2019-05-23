import datetime
import json

def genItems(items, price, quantity):
    aList = list()
    totalCost = 0
    for i in range(len(items)):
        aList.append({
            "item": items[i],
            "cost": price[i],
            "quantity": quantity[i]
        })
        totalCost += price[i]*quantity[i]

    return aList, totalCost

def genTrans(vendor, year, month, day, hour, minute, items, price, quantity):
    aList = dict()
    aList["vendor"] = vendor
    dateTime = datetime.datetime(year, month, day, hour, minute)
    aList["date"] = dateTime.strftime('%m/%d/%Y')
    aList["time"] = dateTime.strftime('%H:%M')
    aList["items"], aList["totalCost"] = genItems(items, price, quantity)
    return aList

aList = list()
aList.append(genTrans('Regal Theatre', 2019, 5, 16, 20, 3,  ['John Wick 3 IMAX '], [21.38], [1]))
aList.append(genTrans('KFC', 2019, 5, 17, 12, 33,  ['Mashed Potatos', 'Chicken Wings'], [2.99, 6.99], [1, 1]))
aList.append(genTrans('City Dogs', 2019, 5, 18, 15, 43,  ['Chilidog', 'Pepsi'], [4.99, 1.99], [1, 1]))
aList.append(genTrans('Farm Fresh', 2019, 5, 18, 20, 26,  ['Apples', 'Bananas', 'Oranges'], [0.45, 0.56, 0.75], [10, 20, 25]))
aList.append(genTrans('Amazon', 2019, 5, 19, 12, 37,  ['Kindle Fire'], [29.99], [1]))
aList.append(genTrans('Best Buy', 2019, 5, 19, 12, 37,  ['Nintendo Switch'], [249.99], [1]))
aList.append(genTrans('KFC', 2019, 5, 19, 20, 48,  ['French Fries'], [2.99], [2]))
aList.append(genTrans('CVS Pharmarcy', 2019, 5, 20, 19, 23,  ['Q-Tips', 'Contact Lens Solution'], [5.67, 7.82], [1, 1]))
aList.append(genTrans('McDonalds', 2019, 5, 21, 12, 0, ['Double Cheeseburger, Snack Wrap, Pepsi'], [2.0, 3.0 , 1.5], [2, 3, 1]))
aList.append(genTrans('Richmond Gas Works', 2019, 5, 26, 20, 48,  ['Gas'], [15.15], [1]))
aList.append(genTrans('Richmond Water', 2019, 5, 28, 18, 34,  ['Water'], [17.84], [1]))
aList.append(genTrans('Comcast', 2019, 5, 24, 23, 18,  ['Internet'], [19.99], [1]))
aList.append(genTrans('Farm Fresh', 2019, 5, 13, 20, 26,  ['Bread', 'Chips', 'Salsa'], [3.99, 2.99, 9.99], [2, 5, 1]))
aList.append(genTrans('Dominion', 2019, 5, 25, 20, 12,  ['Power'], [13.53], [1]))
aList.append(genTrans('Rent', 2019, 5, 29, 17, 12,  ['Rent'], [550.00], [1]))


with open('history.json', 'w') as fb:
    json.dump(aList, fb, indent= 4)