def calculate_alarm_time():
    """
    Calculates the time an alarm will go off on a 24-hour clock.
    """
    while True:
        try:
            current_time_str = input("Enter the current time (in hours, 0-23): ")
            current_time = int(current_time_str)
            if 0 <= current_time <= 23:
                break
            else:
                print("Invalid input. Please enter a time between 0 and 23.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            hours_to_wait_str = input("Enter the number of hours to wait for the alarm (can be negative for previous hours): ")
            hours_to_wait = int(hours_to_wait_str)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    total_hours = current_time + hours_to_wait

    # Use the modulo operator to find the time on a 24-hour clock
    # Python's % handles negative numbers correctly for a 24-hour cycle
    alarm_time = total_hours % 24

    if hours_to_wait < 0:
        print(f"To go back {abs(hours_to_wait)} hours from {current_time}, the alarm will go off at: {alarm_time}")
    else:
        print(f"The alarm will go off at: {alarm_time}")

# Run the program
calculate_alarm_time()
