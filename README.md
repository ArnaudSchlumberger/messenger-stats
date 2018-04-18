# messenger-stats
Generate some statistics about a Facebook Messenger conversation

Parse Facebook Archive of Messenger Conversation
2018 by ruderascal

Download a copy of all your facebook data (https://www.facebook.com/help/212802592074644?helpref=uf_permalink)
Note that this may take a while to process

Locate the HTML file of the conversation you are looking to analyze
All the HTML files are in the "messages" folder of the data
Open the file in a text editor
**REMOVE EVERYTHING UP TO THE FIRST \<div class="message">**
**REMOVE EVERYTHING AFTER THE LAST \</p>**

Save the file as a .txt to the **SAME FOLDER THIS SCRIPT IS IN**

Now, fill in the following variables
And then you're good to run the script using
python messenger-stats.py

ENJOY!
