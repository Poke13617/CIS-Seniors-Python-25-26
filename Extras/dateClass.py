class Date:
    """Represents a year, month, and day"""

    # TODO: Write make_date(year,month,day)
    def make_date(year, month, day):
        
        date = f'{day:02d}/{month:02d}/{year:04d}'
        return date
        

    # TODO: Write print_date(date)
    def print_date(date):
        print(date)

    # TODO: Write date_to_tuple(date) -- Return (year,month,day)
    def date_to_tuple(date):
        date = tuple(date.split("/"))
        return date
        # return year, month, day
    # TODO: Write is_after(d1,d2)
    def is_after(d1, d2):
        return d2 > d1
    

    # --- Test Code ---

    d1 = make_date(1933, 6, 22)
    d2 = make_date(1933, 9, 17)
    print_date(d1)
    print_date(d2)
    d1 = date_to_tuple(d1)
    d2 = date_to_tuple(d2)
    print(d1)
    print(d2)
    print(is_after(d2,d1)) # Should print True