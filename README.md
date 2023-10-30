# Amazon-Price-Tracker
An Amazon price tracker made using Python with Sheety API, SMTP API, and Beautiful Soup is a tool that monitors and tracks the price of specific products listed on Amazon. It interacts with multiple technologies to automate the process, alerting users when the desired price threshold is met.
Here's how the system works:

Components:

1.Python Script: The core of the Amazon price tracker. It interacts with the following APIs and libraries:
Sheety API: Manages the Google Sheets where product data is stored.
SMTP API: Sends email notifications to users.
Beautiful Soup: Performs web scraping on the Amazon site to extract product prices.

2.Google Sheets: A sheet to store data related to user-input products, their Amazon links, desired reduced prices, and the most recent prices fetched from Amazon.

Workflow:

1. User Interaction:

The user interacts with the Python script, providing details such as User Email, Amazon URL, and the desired reduced price through the command line or a GUI.

2.Data Entry:

The entered data (product name, Amazon URL, product price, desired price) is stored in a Google Sheet managed by the Sheety API.

3.Web Scraping:

The Python script uses Beautiful Soup to scrape the Amazon website, fetching the current price of the specified product.

4.Comparison:

It compares the current price with the user's desired reduced price stored in the Google Sheet.

5.Notification:

If the price drops below the user's specified threshold:
The script sends an email notification to the user using the SMTP API, alerting them of the price change and providing a direct link to the product on Amazon.


Reference: Google Sheet Structure
Product Name	Amazon Link	Product Price	Reduced Price	User Email
Product 1	Amazon URL 1	$200	$150	abc@xyz.com
Product 2	Amazon URL 2	$80	$50	abc@xyz.com


Key Features:

Automation: The system automates the process of monitoring Amazon prices for multiple products.
Customization: Users can set their desired price reduction thresholds for each product.
Real-time Updates: Regularly scrapes the Amazon website to ensure up-to-date pricing information.
Alert Mechanism: Notifies users via email when the price drops below the desired threshold.

This tool allows users to effectively track Amazon product prices, enabling them to make informed purchase decisions based on their predefined budget constraints.

