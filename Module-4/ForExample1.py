# Initialize total_score to 0
total_score = 0
# Define the number of students
num_students = 5
# Loop through each student to get their score
for i in range(num_students):
    # Prompt user for score and add to total
    score = input("Enter score for student {}: ".format(i + 1))
    total_score = total_score + int(score)
# Calculate and print the average score
average_score = total_score / num_students
print("Average score:", average_score)