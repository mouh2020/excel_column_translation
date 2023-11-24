from config import *
from googletrans import Translator
import pandas as pd


translator = Translator()
df = pd.read_excel("All-4000.xlsx")
current_row = starting_row
for title in enumerate(df[column_title].to_list()[starting_row:ending_row]) :
    while True :
        try :
            translation = translator.translate(title,src="en",dest="ar")
            df[column_title][current_row] = translation.text
            df.to_excel("translated.xlsx",index=False)
            
            break
        except Exception as e : 
            import time
            print(f"error occured : {str(e)}")
            time.sleep(5)
    print(f"{current_row} -origin text : {title} - translated to : {str(translation.text) if translation else None}")