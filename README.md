A chatbot using cosine similarity

<h2>Usage</h2>

Step 1: download more of the TBBT transcripts in the data directory

Step 2:
python main.py --mode [train/chat] <br>

If mode is train, then we train the chatbot. By default, the model will
restore the previously trained weights (if there is any).

If the mode is chat, we will go into the interaction mode with the bot.

<h2>Sample conversation</h2>
Human:  Hi Sheldon<br>
Bot:  Hi.<br>
Human:  Where are you going?<br>
Bot:  To my room, and no-one’s allowed in.<br>
Human:  Why?  What happened?<br>
Bot:  A death ray?<br>
Human:  Who is dead?!<br>
Bot:  So...  fish.<br>
Human:  Our fish is dead?  We don’t have a fish !!<br>
Bot:  It’s an experiment.<br>
Human:  You are always laughing at me<br>
Bot:  I don’t get it.<br>
Human:  Because you are stupid<br>
Bot:  Really?  That’s impressive.<br>
