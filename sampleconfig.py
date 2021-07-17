#Change this file name to config.py and update appropriately

MTA_KEY = 'your mta developer key' #obtain one at http://web.mta.info/developers/developer-data-terms.html
NUM_TRAINS = 3  #the number of trains to display for each station/direction combination  
STOP_IDS = ['230N', '419N', '230S']  #an array of stations/directions that you would like displayed. Find these in the stations file in staticdata
FEED_URL = 'MTA data feed for relevant lines' #There is no longer a single data feed from the MTA with all lines. Now there are eight different feeds. Enter the URL for the feed containing the line chosen above.
