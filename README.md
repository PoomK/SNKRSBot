# PieBot
A bot to automate checkout processes on various websites such as Nike and Adidas. Selenium is used to automate the process. Tkinter is used to provide a graphical user interface (GUI). Right now I am only working on the SNKRS app for Thailand.

<h3>To do</h3>

- Design new theme
- SNKRS TH
- Adidas TH (Yeezy)
- Discord bot
- Accounts using SQL

<h2>Software functions</h2>

- If billing same as shipping checkbutton pressed, then billing entries become disabled (https://stackoverflow.com/questions/43082390/tkinter-checkbox-with-command-attached)

<h2>Nike SNKRS</h2>

<h3>Types of SNKRS Drop</h3>

- FLOW : First come first serve basis
- LEO : A queued drop that puts you in line and gives a result in 2-3 minutes
- DAN : used for the most exclusive launches. Unlike LEO, it puts your name in a draw, not a queue

<h3>SNKRS TH</h3>

- Most drops in SNKRS TH uses LEO. This means that you have to try to enter as much entries as possible within 2-3 minutes.

<h4>Bot Process</h4>

1. User will create a task containing the link, size of choice, account details and payment details.
2. Once 9:00 or drop time, user presses the start button.
3. The bot will automate each task one at a time. Time to complete a task will be much quicker than normal humans, allowing larger amounts of entry.

<h4>To do</h4>

- Add ability to update profiles and addresses (https://www.youtube.com/watch?v=i4qLI9lmkqw)
- Add threading to perform multiple tasks at once
- Proxies

<h2>Proxies</h2>

- Take a list of proxies from user
- Split the values (https://www.w3schools.com/python/ref_string_split.asp)

<h2>Discord (https://discord.com/developers/applications/720998084326195200/information)</h2>

- Add logging to discord bot
