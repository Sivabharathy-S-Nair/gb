from gtts import gTTS
import os
text="HAI HOW WAS YOUR DAY"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
os.system('start,output.mp3')
