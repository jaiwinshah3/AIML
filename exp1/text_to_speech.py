
from gtts import gTTS 
import os 
  
mytext = 'Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data.'
  
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output1.mp3") 

os.system("start output.mp3") 