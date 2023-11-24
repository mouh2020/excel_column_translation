from config import *
from googletrans import Translator
import pandas as pd


translator = Translator()
df = pd.read_excel("All-4000.xlsx")
for i in range(starting_row,ending_row) :
    while True :
        try :
            translation = translator.translate(df["Title"][i],src=src_language,dest=dest_language)
            df[column_title][i] = translation.text
            df.to_excel("translated.xlsx",index=False)
            break
        except Exception as e : 
            import time
            print(f"error occured : {str(e)}")
            time.sleep(5)
    print(f"{i} -origin text : {str(translation.origin) if translation else None} - translated to : {str(translation.text) if translation else None}")