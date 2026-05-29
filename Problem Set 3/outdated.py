months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:

    date = input("Date: ")
    try:
        if "/" in date:
            date = date.replace(" ", "")
            month, day, year = date.split("/")
            month, day = int(month), int(day)

        elif "," in date:
            month = date.split(" ",maxsplit=1) 
            if month[0] in months:
                month, day, year = date.split()
                day, month, year = int(day.replace(",", "")), months.index(month)+1, int(year)

        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError

    except (AttributeError, ValueError, NameError, KeyError):
        pass

    else:
        print(f"{year}-{month:02}-{day:02}")
        break
