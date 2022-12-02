from datetime import datetime
date_format = "%d/%m/%Y"
today = datetime.today()
d1 = today.strftime(date_format)
d2 = input("Enter a date in (dd/mm/yyyy) format: ")
try:
    date1 = datetime.strptime(d1, date_format)
    date2 = datetime.strptime(d2, date_format)
    result = date1 - date2
    d3 = result.days * -1
    if d3 < 0:
            d3 = d3 * -1
            print("There have been",d3,"days between today and",d2)      
    elif d3 > 0:  
        print("There are",d3,"days between today and",d2)
    else:
        print("Today is",d2)
except ValueError:
    print("Invalid date format.")