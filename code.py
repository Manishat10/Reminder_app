from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

# User input for reminder title, message, and time
Toasttitle = input("\nTitle of reminder: ")
msg = input("Message: ")
minutes = float(input("How many minutes until the reminder?: "))

# Convert minutes to seconds
seconds = minutes * 60

# Confirmation message
print("\nReminder set successfully! It will notify you in {:.2f} minutes.".format(minutes))

# Pause the program for the specified duration
time.sleep(seconds)

# Show the toast notification
toaster.show_toast(Toasttitle, msg, duration=10, threaded=True)

# Keep checking if the notification is still active
while toaster.notification_active():
    time.sleep(0.1)
