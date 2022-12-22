## saveDiscoverWeekly

saveDiscoverWeekly is a simple script that can automatically save your current Spotify Discover Weekly playlist. You can use a program like Task Scheduler to make it run on Mondays.

## Running & Authentication

You can simply run the script to make it work. However, you need to edit some variables specified for you to get access to Spotify API.
5 variabales required are in authentication.py file.
After acquiring an access token, Spotify ends it after 1 hour. To solve this issue, I have used refresh token provided by Spotify and script requires a new refresh token everytime. You can skip calling refresh() function if you don't want to do this.
Keep in mind that while acquiring access tokens, you need to give access to the script. 

