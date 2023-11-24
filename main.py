from config import *
from googletrans import Translator
import pandas as pd


translator = Translator()
df = pd.read_excel("All-4000.xlsx")

for idx,title in enumerate(df[column_title].to_list()[starting_row:ending_row],start=0) :
    while True :
        try :
            translation = translator.translate(title,src="en",dest="ar")
            df[column_title][idx] = translation.text
            df.to_excel("translated.xlsx",index=False)
            
            break
        except Exception as e : 
            import time
            print(f"error occured : {str(e)}")
            time.sleep(5)
    print(f"{idx} -origin text : {title} - translated to : {str(translation.text) if translation else None}")