def display_welcome():
    """Display program header"""
    name = input("What is your name? ")
    print("\n\n")

    print("-" * 30)
    print(name + "'s College Application Tracker")
    print("-" * 30)

    return name




def get_college_count():
    """Get number of colleges user is applying to
    return
        count (int)
    """
    num_of_colleges = int(input("\nHow many colleges are you applying to? "))
    return num_of_colleges




def get_sat_score():
    """Get the scores of the sat if they took one"""
    sat_score = int(input("\nWhat did you get on the last SAT you took? "))
    return sat_score





def get_application_costs(num_of_colleges):
    """
    Calculates total application costs:
    
    Return:
        total_cost(float)
    """
    total_cost = num_of_colleges * 50
    tax = total_cost * 0.08
    total_cost = total_cost + tax

    cost = float(total_cost)

    return cost



def analyze_sat(score):
    """Provide feedback on sat score
    >= 1400 - excellent
    >= 1200 - good score
    >= 1000 - Solid foundation
    else - Consider retaking to improve college options
    """
    if score >= 1400:
        feedback = "Excellent SAT Score!"
    
    elif score >= 1200:
        feedback = "Good SAT Score"

    elif score >= 1000:
        feedback = "Solid foundation"
    else:
        feedback = "Needs improving"

    return feedback




def display_summary(name, colleges, cost, sat_score, sat_feedback):
    """Display complete applications summary"""
    print("\n\n" + name + "'s complete college application summary")
    print("Number of colleges applying to: ", colleges)
    print(f"Cost of applications: {cost:.2f}")
    print("SAT Score: ", sat_score)
    print("Feedback: ", sat_feedback)







def main():
    """Main function - orchestrates the entire program"""
    # Welcome the user
    name = display_welcome()
    num_colleges = get_college_count()
    total_cost = get_application_costs(num_colleges)
    sat = get_sat_score()

    #Analyze data
    feedback = analyze_sat(sat)

    # Display results
    display_summary(name, num_colleges, total_cost, sat, feedback)

    print("\nGood luck with your applications")

if __name__ == "__main__":
    main()