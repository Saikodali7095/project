# Student Details:
# Name : - Kodali Sai Pavan Krishna
# Student mail id: - skodali1@student.fitchburgstate.edu
# Student id: - @01470537

def get_valid_days(task_name):
    """
    Helper function to validate user input for deadlines.
    Checks for data type (int) and logical range (0-365).
    """
    while True:
        user_input = input(f"How many days until '{task_name}' is due? ")
        try:
            days = int(user_input)

            # Range Validation using if/else
            if days < 0:
                print(">> Input Error: Deadlines cannot be in the past! Please enter a positive number.")
            elif days > 365:
                print(">> Input Error: That's over a year away! Please enter a value between 0 and 365.")
            else:
                return days  # Valid input received

        except ValueError:
            # Custom error message for wrong data types
            print(f">> Type Error: '{user_input}' is not a valid number. Please enter a whole integer.")


def main():
    # --- Data Type Selection & Initialization ---
    project_name = "StudyBuddy"
    is_running = True
    task_count = 0

    print(f"--- {project_name}: Student Task Tracker ---")
    print("Keep your deadlines in sight and your stress levels low.\n")

    while is_running:
        task_name = input("Enter task name (or type 'exit' to quit): ").strip()

        # Conditional Logic for exiting the loop
        if task_name.lower() == 'exit':
            is_running = False
            print(f"\nFinal session summary: {task_count} tasks managed.")
            print("Shutting down StudyBuddy. Good luck studying!")
        elif not task_name:
            print(">> Input Error: Task name cannot be empty.")
        else:
            # Call our validation helper function
            days_until_due = get_valid_days(task_name)
            task_count += 1

            # Priority Mapping Logic
            if days_until_due <= 2:
                priority = "HIGH"
                action = "Start immediately!"
            elif 3 <= days_until_due <= 7:
                priority = "MEDIUM"
                action = "Schedule this for the week."
            else:
                priority = "LOW"
                action = "Keep it on your radar."

            print(f" >> [Priority: {priority}] {action}")

        print("-" * 40)


if __name__ == "__main__":
    main()