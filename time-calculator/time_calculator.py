def add_time(start, duration, day=False):
    # Sets the variable responsible for dealing with calculations with exceeding 
    # 60 minutes to False by default.
    exceed = ""
    # Sets up a boolean variable that should be used in case the sum of minutes 
    # exceeds 60. 
    add_1_hour = False
    # List with the days of the week in order.
    week_days = [
        "Sunday",
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday"
        ]
    # Reads the first input and returns the hours and minutes as intergers.
    start_hour = int(start.split(":")[0])
    start_minutes = int(start.split(":")[1].split(" ")[0])
    start_meridian = start.split(":")[1].split(" ")[1]
    # Converts the start hours into a 24-hour clock and the into minutes.
    start_hour_min = start_hour * 60
    start_in_minutes = start_hour_min + start_minutes

    # Reads the second input and returns the hours and minutes as intergers.
    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1].split(" ")[0])
    # Converts the duration hours into a 24-hour clock and the into minutes.
    duration_hour_min = duration_hour * 60
    duration_in_minutes = duration_hour_min + duration_minutes
    # Stores the amount of time left to end the first day.
    time_left_in_start = 720 - start_in_minutes
    # Calculates the result that was added on the minutes side.
    result_minutes = start_minutes + duration_minutes
    
    # Handles the cases where the minutes exceed the 60 minute mark.
    if result_minutes >= 60:
        modulus_minutes = result_minutes % 60
        result_minutes = modulus_minutes
        result_minutes = '%02d' % result_minutes
        add_1_hour = True
    else:
        result_minutes = '%02d' % result_minutes

    # Calculates the result that was added on the hours side.
    result_hour = int((start_hour_min + duration_hour_min)/60)
    # If the minutes exceeded 60, add 1 hour to the hour mark.
    if add_1_hour:
        result_hour += 1

    #Handles what to do with the result should it exceed the 12-hour mark.
    if result_hour >= 12:
        result_hour %= 12
    # Deals with the 12th hour.
    if result_hour == 0:
        result_hour = 12
    
    # Deals with the exceeding time
    if duration_in_minutes < time_left_in_start:
        exceeding_time_in_hours = 0
    else: 
        exceeding_time_in_hours = (duration_in_minutes - time_left_in_start) // 60
    exceeding_days = exceeding_time_in_hours // 24
    

    # Deals with the meridian.
    if duration_in_minutes > time_left_in_start:
        if start_meridian == "PM" and (duration_in_minutes % 60 != 0):
            result_meridian = " AM"
        elif start_meridian == "PM" and (duration_in_minutes % 60 == 0):
            result_meridian = " PM"
        elif start_meridian == "AM" and (duration_in_minutes % 60 != 0):
            result_meridian = " PM"
        elif start_meridian == "AM" and (duration_in_minutes % 60 == 0):
            result_meridian = " AM"
    else:
        result_meridian = f" {start_meridian}"

    # Deals with the day of the week.
    if day:
        # Extracts the day from the input
        day = str(day.lower().capitalize())
        day_position_on_list = week_days.index(day)
        # Ensures the list will begin with the desired day.
        while week_days[0] != day:
            for shift_day in week_days[:day_position_on_list]:
                week_days.remove(shift_day)
                week_days.append(shift_day)
        mod_day = exceeding_days % 7
        if time_left_in_start > (exceeding_time_in_hours // 60) and (duration_in_minutes - exceeding_time_in_hours) < 720 and start_meridian == "PM":
            day_of_the_week = f", {week_days[mod_day]}"
        else:
            day_of_the_week = f", {week_days[mod_day + 1]}"
    else:
        day_of_the_week = ""


    # Deals with the 'days later' cases.
    if -1 >= exceeding_days <= 0 and start_meridian == "AM":
        exceed = f" ({exceeding_days + 1} days later)"
    elif exceeding_days > 0 and start_meridian == "PM":
        exceed = f" ({exceeding_days + 1} days later)"
    elif duration_in_minutes > (time_left_in_start + 720) and start_meridian == "AM":
        exceed = " (next day)"
    elif exceeding_time_in_hours >= (time_left_in_start // 60) and start_meridian == "PM":
        exceed = " (next day)"

    # Formatting of the result line.
    new_time = f"{result_hour}:{result_minutes}{result_meridian}{day_of_the_week}{exceed}"

    return new_time