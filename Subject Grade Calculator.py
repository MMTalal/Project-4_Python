# Display the title of the program
print("Subject Grade Calculator")

# Display a separator line for visual clarity
print("-" * 50)

# Prompt the user to input the grade for subject one
SubjectOne = float(input("What's your grade for subject one out of 20? "))

# Check if the input grade is valid
if SubjectOne > 20:
    print("Please try again and input your correct grade for subject one. It should be less than 20.")
else:
    # Prompt the user to input the grade for subject two
    SubjectTwo = float(input("What's your grade for subject two out of 20? "))

    # Check if the input grade is valid
    if SubjectTwo > 20:
        print("Please try again and input your correct grade for subject two. It should be less than 20.")
    else:
        # Prompt the user to input the grade for subject three
        SubjectThree = float(input("What's your grade for subject three out of 20? "))

        # Check if the input grade is valid
        if SubjectThree > 20:
            print("Please try again and input your correct grade for subject three. It should be less than 20.")
        else:
            # Prompt the user to input the grade for subject four
            SubjectFour = float(input("What's your grade for subject four out of 20? "))

            # Check if the input grade is valid
            if SubjectFour > 20:
                print("Please try again and input your correct grade for subject four. It should be less than 20.")
            else:
                # Prompt the user to input the grade for subject five
                SubjectFive = float(input("What's your grade for subject five out of 20? "))

                # Check if the input grade is valid
                if SubjectFive > 20:
                    print("Please try again and input your correct grade for subject five. It should be less than 20.")
                else:
                    # Prompt the user to input the grade for subject six
                    SubjectSix = float(input("What's your grade for subject six out of 20? "))

                    # Check if the input grade is valid
                    if SubjectSix > 20:
                        print("Please try again and input your correct grade for subject six. It should be less than 20.")
                    else:
                        # Calculate the total grade by summing all subject grades
                        total_grade = SubjectOne + SubjectTwo + SubjectThree + SubjectFour + SubjectFive + SubjectSix

                        # Display the calculated total grade as a percentage
                        print(f"Your total grade is {(total_grade * 100) / 120:.2f}")

                        # Classify the grade based on the calculated total grade
                        if 0 < total_grade < 50:
                            print("Unfortunately, your grade is below 50%. You have failed.")
                        elif 50 < total_grade < 65:
                            print("Congratulations! Your grade is above 50%. You are acceptable.")
                        elif 65 < total_grade < 75:
                            print("Congratulations! Your grade is above 65%. You are good.")
                        elif 75 < total_grade < 90:
                            print("Congratulations! Your grade is above 75%. You are very good.")
                        else:
                            print("Congratulations! Your grade is above 90%. You are excellent.")