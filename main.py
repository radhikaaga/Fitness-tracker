from backend.authentication.register_user import register_user
from backend.authentication.update_user import update_user
from backend.email_alerts.reminder_scheduler import start_reminder_scheduler
from backend.nutritionix.exercise_api import get_exercise_info
from backend.nutritionix.nutrition_api import get_nutritional_info
from backend.pixela.graph_pixels import manage_pixel_entry
from backend.pixela.pixel_scheduler import start_pixel_scheduler
from backend.speech_recognition.speech_input import get_speech_input
from database.csv_manager import CSVManager

# Use hardcoded username since you're not using .env for it
username = "riddhikhandelwal"
graph_id = "weight-gain"

# Get token from CSV file
token = CSVManager("resources/users.csv").get_token_by_username(username)

# Print token for verification
print(f"Token for {username}: {token}")

if token is None:
    print("Failed to retrieve user token from CSV file")
else:
    # Example: Nutrition Info
    food_info = get_nutritional_info("1 apple", username, graph_id)
    print(food_info)

    # You can uncomment the others below as needed
    # exercise_info = get_exercise_info("30 minutes running", username, graph_id)
    # print(exercise_info)

    # start_pixel_scheduler(username, graph_id)
    # start_reminder_scheduler()
