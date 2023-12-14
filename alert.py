import time
from plyer import notification

def drink_water_reminder():
    title = "Drink Water Reminder"
    message = "It's time to drink water!"
    
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # e.g., 'path/to/icon.png'
        timeout=10,  # seconds
    )

def main():
    while True:
        # Set the time for the reminder (15 minutes in seconds)
        reminder_time = 15 * 60
        
        # Wait for the specified time
        time.sleep(reminder_time)
        
        # Trigger the drink water reminder
        drink_water_reminder()

if __name__ == "__main__":
    main()
