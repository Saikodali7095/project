#Student Details:
#Name : - Kodali Sai Pavan Krishna
#Student mail id: - skodali1@student.fitchburgstate.edu
#Student id: - @01470537

def main():
    # --- Data Type Selection & Initialization ---
    project_name = "StudyBuddy"  # String: App identity
    is_running = True            # Boolean: Control flow for the app loop
    task_count = 0               # Integer: Tracking quantity of work
    
    print(f"--- {project_name}: Student Task Tracker ---")
    print("Keep your deadlines in sight and your stress levels low.\n")

    while is_running:
        # --- Variable Identification & Coverage ---
        # Collecting user input to drive the logic
        task_name = input("Enter task name (or type 'exit' to quit): ").strip()
        
        # --- Conditional Logic Mapping ---
        if task_name.lower() == 'exit':
            is_running = False
            print(f"\nFinal session summary: {task_count} tasks managed.")
            print("Shutting down StudyBuddy. Good luck studying!")
        else:
            try:
                # Prompting for a numeric deadline (days)
                days_until_due = int(input(f"How many days until '{task_name}' is due? "))
                task_count += 1
                
                # Nested Logic for Priority Mapping
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
                
            except ValueError:
                print("Error: Please enter a whole number for the deadline.")
        
        print("-" * 30)

if __name__ == "__main__":
    main()
