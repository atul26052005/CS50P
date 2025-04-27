
month_names = [
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

def get_date():
    while True:
        try:
            date_input = input("Date: ").strip()

            if "/" in date_input:
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                    formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                    return formatted_date
                else:
                    raise ValueError("Invalid date values.")

            else:
                parts = date_input.split()
                if "," in parts[1]:
                    if len(parts) == 3:
                        month_name = parts[0].capitalize()
                        day = int(parts[1].strip(','))
                        year = int(parts[2])

                        if month_name in month_names:
                            month = month_names.index(month_name) + 1
                            formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                            if 1 <= day <= 31:
                                formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                                return formatted_date
                            else:
                                raise ValueError("Invalid day. Day must be between 1 and 31.")
                        else:
                            raise ValueError("Invalid month name.")
                    else:
                        raise ValueError("Incorrect format for month day year.")

        except (ValueError, IndexError):
            print("Invalid date. Please try again.")

formatted_date = get_date()
print(formatted_date)