A chatbot using cosine similarity

<h2>Usage</h2>

Step 1: download more of the TBBT transcripts in the data directory

Step 2:
python main.py --mode [train/chat] <br>

If mode is train, then we train the chatbot. By default, the model will
restore the previously trained weights (if there is any).

If the mode is chat, we will go into the interaction mode with the bot.

<h2>Sample conversation</h2>
Human:  Hi Sheldon
Bot:  Hi.
Human:  Where are you going?
Bot:  To my room, and no-one’s allowed in.
Human:  Why?  What happened?
Bot:  A death ray?
Human:  Who is dead?!
Bot:  So...  fish.
Human:  Our fish is dead?  We don’t have a fish !!
Bot:  It’s an experiment.
Human:  You are always laughing at me
Bot:  I don’t get it.
Human:  Because you are stupid
Bot:  Really?  That’s impressive.
