import googletrans
import requests
import json
import pyttsx3 as pt
from playsound import playsound
from gtts import gTTS
import os
from googletrans import Translator
translator=Translator()
languages = googletrans.LANGCODES
print(languages)
class news_paper:
    def setup(self,stored):
        self.store=stored
        self.speekup(f"Hello and Welcome to intelligencers News center. here i am going to give {len(self.store)} top and  hot news headlines . tell me your language")
        while True:
            p=0
            print("Enter your language")
            self.choosen = input()
            if self.choosen in languages:
                self.chooseen_lang_code = languages[self.choosen]
                break
            else:
                for i in languages.keys():
                    if self.choosen[:int(len(self.choosen)/2)] in i:
                        print(f"did you mean {i} if yes then say 'Y' if not say 'N")
                        self.check=input()
                        if self.check.upper() == 'Y':
                            self.chooseen_lang_code = languages[i]
                            print("thanks we got it ")
                            p+=1
                            break
                if p>0:
                    break
                print("I thing We Dont have this language in our dictionary .. try again")
        print(self.chooseen_lang_code)
        self.speekup(f"Delivering the News in {googletrans.LANGUAGES[self.chooseen_lang_code]}")

        for j, i in enumerate(self.store):
            if j==0:
                text="First news is "
                id1 = self.guss_lang(text)
                print(id1)
                self.speak_in_lang(text,id1,self.chooseen_lang_code)

            elif j < len(self.store)-1 and j !=0:
                next=("the next news is ")
                id2 = self.guss_lang(next)
                self.speak_in_lang(next, id2,self.chooseen_lang_code)

            else:

                last = ("the last news is ")
                id3 = self.guss_lang(last)
                self.speak_in_lang(last, id3, self.chooseen_lang_code)
            self.speak_in_lang(i,self.guss_lang(i),self.chooseen_lang_code)
        self.speak_in_lang("thanks for paying the attention",'en', self.chooseen_lang_code)
    def speekup(self,text):
        engine.say(text)
        engine.runAndWait()

    def guss_lang(self,title):
        find_lang = translator.detect(title)
        lang = (str(find_lang))
        print(lang[14:16])
        return (lang[14:16])


    def speak_in_lang(self,text,sor_id,des_id):
        out = translator.translate(text,src=sor_id,dest=des_id).text
        obj=gTTS(text=out,lang=des_id)
        obj.save('sampl.mp3')
        playsound('sampl.mp3')
        os.remove('sampl.mp3')
    def speak_error(self,error):
        engine.say(error)
        engine.runAndWait()
if __name__=="__main__":
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=2e5a2cb1608b48a0b6bdab272e8038b4"
    store=[]
    engine=pt.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.setProperty('rate',180 )
    engine.setProperty('volume',1)
    np = news_paper()
    try:
        status=requests.get(url).status_code
        if status==200:
            responce = requests.get(url).text
            py_dict = json.loads(responce)
            for i in py_dict['articles']:
                store.append(i['title'])
            print(store[:7])
            # speakup_news(store[:3])
            np.setup(store[:5])
        else:
            np.speak_error("The side is not reachable at this moment please try after some time ! thank you")
    except Exception as e:
        # print(e)
        np.speak_error("Something went Wrong or this language is not supported or  . connection might be lost")

