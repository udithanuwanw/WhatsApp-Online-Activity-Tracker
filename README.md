WhatsApp Online Activity Tracker

This repository contains a Python script designed to track the online activity of WhatsApp contacts. The script utilizes Selenium, a powerful tool for automating web browsers, to monitor the online status of specified contacts. Here's how to use it effectively:

Instructions:
Prerequisites:

Ensure you have Python installed on your system.
Install the necessary Python packages listed in requirements.txt. You can do this by running:
Copy code
pip install -r requirements.txt
Download and install ChromeDriver appropriate for your Chrome browser version.
Setup:

Save the phone numbers of the contacts you want to track in a file named trackinglist.txt, with each phone number on a separate line.
Execution:

Run the Python script whatsapp_tracker.py.
The script will open a Chrome browser window and navigate to WhatsApp Web.
Scan the QR code to log in to your WhatsApp account.
Monitoring:

The script will continuously monitor the online activity of the specified contacts.
It will log the online and offline events of each contact in separate CSV and text files.
You will receive Telegram notifications for every change in the online status of the tracked contacts.
Important Notes:
Privacy: This script only tracks the online activity of contacts whose phone numbers you have specified in trackinglist.txt. No other information is collected or stored.
Contact Privacy: Ensure that the contacts you're tracking have their online status visible to you. You must have them saved in your contacts list.


Disclaimer:
This script is intended for educational purposes and personal use only. Usage of this script may violate WhatsApp's terms of service. Use it responsibly and at your own risk.

Support:
If you encounter any issues or have questions about the script, feel free to open an issue in the repository. We'll do our best to assist you.

License:
This project is licensed under the MIT License. Feel free to modify and distribute it according to the terms of the license.