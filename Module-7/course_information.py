def course_information():
    """
    Creates and stores course information in dictionaries, then allows the user
    to look up information for a specific course number.
    """
    # Create the dictionary for course numbers and room numbers.
    room_numbers = {
        "CS101": 3004,
        "CS102": 4501,
        "CS103": 6755,
        "NT110": 1244,
        "CM241": 1411
    }

    # Create the dictionary for course numbers and instructors.
    instructors = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }

    # Create the dictionary for course numbers and meeting times.
    meeting_times = {
        "CS101": "8:00 a.m.",
        "CS102": "9:00 a.m.",
        "CS103": "10:00 a.m.",
        "NT110": "11:00 a.m.",
        "CM241": "1:00 p.m."
    }

    # Get a course number from the user.
    course_number = input("Enter a course number (e.g., CS101): ")

    # Check if the course number exists in the dictionaries.
    if course_number in room_numbers:
        print(f"\nCourse Information for {course_number}:")
        print(f"  Room Number: {room_numbers[course_number]}")
        print(f"  Instructor: {instructors[course_number]}")
        print(f"  Meeting Time: {meeting_times[course_number]}")
    else:
        print("Error: The course number was not found.")

# Run the program
course_information()
