# instagram-follower-tracker
This script analyzes the following and followers of a user on Instagram. Unlike traditional follower trackers,
this tracker requires the user to manually input HTML files, but comes with the benefit of being undetectable
by Instagram's servers.

# How to use (ideally use Chrome):

Before starting, download files from this repo to your local machine.

1. At the root of the project, create a `/input` directory with a `followers.html` and `following.html` file
2. Navigate to your Instagram profile on a desktop
3. Click on your followers
4. Inspect the HTML elements of the page. On Chrome, press fn + f12
5. Navigate to the "Elements" tab at the top of the developer tools
6. Scroll down the follower list until the bottom. Do NOT reload the page.
7. Right-click the <html> tag on the second line. Then, Copy -> Copy element
8. Make sure the `followers.html` file is empty. Then, paste your clipboard to `followers.html`.
9. Repeat steps 2-6, but with your following. Use the `following.html` file.
10. Right click `scraper.py` and run the program.
11. Data will be output into the files in the `/output` directory.


# Future Improvements
- Figure out a way to load the entire follower list without sending requests to the server