# Parse Facebook Archive of Messenger Conversation
# 2018 by ruderascal

####################################################################
########################## INSTRUCTIONS ############################
####################################################################

# Download a copy of all your facebook data (https://www.facebook.com/help/212802592074644?helpref=uf_permalink)
# Note that this may take a while to process
#
# Locate the HTML file of the conversation you are looking to analyze
# All the HTML files are in the "messages" folder of the data
# Open the file in a text editor
# REMOVE EVERYTHING UP TO THE FIRST <div class="message">
# REMOVE EVERYTHING AFTER THE LAST </p>
#
# Save the file as a .txt to the SAME FOLDER THIS SCRIPT IS IN
#
# Now, fill in the following variables
# And then you're good to run the script using
# python messenger-stats.py
#
# ENJOY!

####################################################################
############################# VARIABLES ############################
####################################################################

# name of the file with the chat history
filename = "donald.txt"

# your user name (PRECISELY as used on facebook)
me = "Rude Rascal"

# other user name (PRECISELY as used on facebook)
you = "Donald Trump"

# month you started messaging in
monthstart = 4

# year you started messaging in
yearstart = 2012

# Last message sent on (day number, if April 1st write "1")
lastday = 18

####################################################################
########### PLEASE DON'T TOUCH ANYTHING FROM HERE ON FORTH #########
########### (UNLESS YOU KNOW WHAT YOU'RE DOING) ####################
####################################################################

# importing the file.

file = open(filename, "r")
content = file.read()
file.close()

# parsing the message to create an array with single messages

import re
by_message = re.split('<div class="message">', content)


########################## GET DATA ###########################
# Total number of messages
print "####################################################################"
print "################ HI THERE, HERE ARE SOME STATS #####################"
print "####################################################################"
print "Total number of messages: %d" % len(by_message)
print ""

##### Some more calculations...
me_msg = list()
you_msg = list()

for i in range(1, len(by_message)):

	if by_message[i].count(">%s<" % me):
		me_msg.append(by_message[i])

	elif by_message[i].count(">%s<" % you):
		you_msg.append(by_message[i])

print "Number of messages sent by %s: %d" % (me, len(me_msg))
print "Number of messages sent by %s: %d" % (you, len(you_msg))
print ""
print "####################################################################"
print ""

# Number of words per sender
me_words = list()
you_words = list()

for i in range(1, len(me_msg)):
	message = re.split("<p>", me_msg[i])
	message_end = re.split("</p>", message[1])
	words = re.split(" ", message_end[0])
	me_words.append(len(words))

for i in range(1, len(you_msg)):
	message = re.split("<p>", you_msg[i])
	message_end = re.split("</p>", message[1])
	words = re.split(" ", message_end[0])
	you_words.append(len(words))

print "Number of words sent by %s: %d" % (me, sum(me_words))
print "Average message length for %s: %r" % (me, round(sum(me_words)/float(len(me_words)), 2))
print ""
print "Number of words sent by %s: %d" % (you, sum(you_words))
print "Average message length for %s: %r" % (you, round(sum(you_words)/float(len(you_words)), 2))
print ""
print "####################################################################"
print ""

# Longest message by user
def longest_message(me_msg, me_words):
	for i in range(1, len(me_words)):
		if me_words[i] == max(me_words):
			message = re.split("<p>", me_msg[i+1])
			message_end = re.split("</p>", message[1])
			return message_end[0]
			break

print "Longest message sent by %s: %r words" % (me, max(me_words))
print longest_message(me_msg, me_words)
print ""
print "####################################################################"
print ""

print "Longest message sent by %s: %r words" % (you, max(you_words))
print longest_message(you_msg, you_words)
print ""
print "####################################################################"
print ""

# Here's a new function to calculate the next averages
def generateAvg(content_to_parse, message_txt_1, message_txt_2, yearstart, monthstart, lastday):
	from datetime import datetime, date, time
	monthlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	duration_months = ((datetime.now().year - yearstart) * 12) - monthstart + datetime.now().month + 1
	daily_avg_by_month = list()
	days_messaged = 0

	for i in range (1, duration_months + 1):
		messagecount = list()

		if monthstart > 12:
			monthstart = 1
			yearstart = yearstart + 1

		if  i == duration_months:
			monthlength[monthstart-1] = lastday

		for j in range(1, monthlength[monthstart-1] + 1):
			days_messaged = days_messaged + 1
			messagecount.append(content_to_parse.count("%s %d, %d" % (monthlist[monthstart-1], j, yearstart)))

		print "%s %s %d: %r" % (message_txt_1, monthlist[monthstart-1], yearstart, round(sum(messagecount)/float(len(messagecount)),2))
		daily_avg_by_month.append(sum(messagecount))
		monthstart = monthstart + 1

	print "%s %r" % (message_txt_2, round(sum(daily_avg_by_month) / float(days_messaged),2))
	return days_messaged

# Daily average by month, total
days = generateAvg(content, "Average daily messages in", "All time daily average:", yearstart, monthstart, lastday)
print ""
print "####################################################################"
print ""

# Daily average by month, me
generateAvg("".join(me_msg), "Average daily messages from " + me + " in", "All time daily average from " + me + ":", yearstart, monthstart, lastday)
print ""
print "####################################################################"
print ""

# Daily average by month, you
generateAvg("".join(you_msg), "Average daily messages from " + you + " in", "All time daily average from " + you + ":", yearstart, monthstart, lastday)
print ""
print "####################################################################"
print ""

# Total conversation duration (as returned by the daily average by month function)
print "You started messaging %d days ago" % days
print ""
print "####################################################################"
print "####################### THAT'S ABOUT IT ############################"
print "####################################################################"
