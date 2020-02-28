# NI-NumberTracker
Application for Noram International to track worker productivity.

Requirements for Client PC's

1.) Python 3.7.0 or newer
  Libraries used:
    - Selenium
    - PyMongo
    - Schedule
  
2.) Google Chrome
3.) Chrome Driver (check which version you need by entering chrome://version in Chrome browser.)

Requirements for Web Server

1.) Python 3.7.0 or newer
 - gunicorn3
 - nginix
 - Flask
 - Git
 2.) MongoDB
 
NI NumberTracker uses Selenium to take control of the Google Chrome web browser so it may easily grab needed information on worker productivity. The application will automatically open the needed web pages and log in according to the station its at. Since the company uses different accounts for each individual PC, the logins are hard coded for each one. The application will update a database every 45 seconds with productivity numbers as an employee works. These numbers can be seen from a seperate web server working in tandem with the database to display numbers station by station. The web server will only allow certain IP addresses to access it, ensuring only manager or supervisor work stations can view the information.
 
