from os import replace
from time import strftime
from datetime import datetime
import random

WISHES = ("hey", "hello", "hi", ":)", "hi there", "bye", "see you")
SMALL_WORD = ("what", "what?", "ok", "emoji")

SMILY = """๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คฃ ๐ฅฒ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฅฐ ๐ ๐ ๐ ๐ 
๐ ๐ ๐ ๐ ๐คช ๐คจ ๐ง ๐ค ๐ ๐ฅธ ๐คฉ ๐ฅณ ๐ ๐ ๐ ๐ ๐ ๐ ๐ โน๏ธ ๐ฃ ๐ ๐ซ ๐ฉ 
๐ฅบ ๐ข ๐ญ ๐ค ๐  ๐ก ๐คฌ ๐คฏ ๐ณ ๐ฅต ๐ฅถ ๐ฑ ๐จ ๐ฐ ๐ฅ ๐ ๐ค ๐ค ๐คญ ๐คซ ๐คฅ ๐ถ ๐ ๐ 
๐ฌ ๐ ๐ฏ ๐ฆ ๐ง ๐ฎ ๐ฒ ๐ฅฑ ๐ด ๐คค ๐ช ๐ต ๐ค ๐ฅด ๐คข ๐คฎ ๐คง ๐ท ๐ค ๐ค ๐ค ๐ค  ๐ ๐ฟ 
๐น ๐บ ๐คก ๐ฉ ๐ป ๐ โ ๏ธ ๐ฝ ๐พ ๐ค ๐ ๐บ ๐ธ ๐น ๐ป ๐ผ ๐ฝ ๐ ๐ฟ ๐พ ๐ ๐ค ๐ โ 
๐ ๐ ๐ค ๐ค โ๏ธ ๐ค ๐ค ๐ค ๐ค ๐ ๐ ๐ ๐ ๐ โ๏ธ ๐ ๐ โ ๐ ๐ค ๐ค ๐ ๐ ๐ 
๐คฒ ๐ค ๐ โ๏ธ ๐ ๐คณ ๐ช ๐ฆพ ๐ฆต ๐ฆฟ ๐ฆถ ๐ฃ ๐ ๐ฆป ๐ ๐ซ ๐ซ ๐ง  ๐ฆท ๐ฆด ๐ ๐ ๐ ๐ 
๐ ๐ฉธ ๐ถ ๐ง ๐ง ๐ฆ ๐ฉ ๐ง ๐จ ๐ฉโ๐ฆฑ ๐งโ๐ฆฑ ๐จโ๐ฆฑ ๐ฉโ๐ฆฐ ๐งโ๐ฆฐ ๐จโ๐ฆฐ ๐ฑโโ๏ธ ๐ฑ ๐ฑโโ๏ธ ๐ฉโ๐ฆณ ๐งโ๐ฆณ ๐จโ๐ฆณ ๐ฉโ๐ฆฒ ๐งโ๐ฆฒ ๐จโ๐ฆฒ 
๐ง ๐ต ๐ง ๐ด ๐ฒ ๐ณโโ๏ธ ๐ณ ๐ณโโ๏ธ ๐ง ๐ฎโโ๏ธ ๐ฎ ๐ฎโโ๏ธ ๐ทโโ๏ธ ๐ท ๐ทโโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ ๐ต๏ธโโ๏ธ ๐ต๏ธ ๐ต๏ธโโ๏ธ ๐ฉโโ๏ธ ๐งโโ๏ธ ๐จโโ๏ธ 
๐ฉโ๐พ ๐งโ๐พ ๐จโ๐พ ๐ฉโ๐ณ ๐งโ๐ณ ๐จโ๐ณ ๐ฉโ๐ ๐งโ๐ ๐จโ๐ ๐ฉโ๐ค ๐งโ๐ค ๐จโ๐ค ๐ฉโ๐ซ ๐งโ๐ซ ๐จโ๐ซ ๐ฉโ๐ญ ๐งโ๐ญ ๐จโ๐ญ ๐ฉโ๐ป ๐งโ๐ป ๐จโ๐ป ๐ฉโ๐ผ ๐งโ๐ผ ๐จโ๐ผ ๐ฉโ๐ง ๐งโ๐ง ๐จโ๐ง ๐ฉโ๐ฌ ๐งโ๐ฌ ๐จโ๐ฌ ๐ฉโ๐จ ๐งโ๐จ ๐จโ๐จ ๐ฉโ๐ ๐งโ๐ ๐จโ๐ ๐ฉโโ๏ธ ๐งโโ๏ธ ๐จโโ๏ธ ๐ฉโ๐ ๐งโ๐ ๐จโ๐ ๐ฉโโ๏ธ ๐งโโ๏ธ ๐จโโ๏ธ ๐ฐโโ๏ธ ๐ฐ ๐ฐโโ๏ธ 
๐คตโโ๏ธ ๐คต ๐คตโโ๏ธ ๐ธ ๐คด ๐ฅท ๐ฆธโโ๏ธ ๐ฆธ ๐ฆธโโ๏ธ ๐ฆนโโ๏ธ ๐ฆน ๐ฆนโโ๏ธ ๐คถ ๐งโ๐ ๐ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ 
๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐ผ ๐คฐ ๐คฑ ๐ฉโ๐ผ ๐งโ๐ผ ๐จโ๐ผ ๐โโ๏ธ ๐ ๐โโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ 
๐โโ๏ธ ๐ ๐โโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐คฆโโ๏ธ ๐คฆ ๐คฆโโ๏ธ ๐คทโโ๏ธ ๐คท ๐คทโโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ 
๐โโ๏ธ ๐ ๐โโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐ ๐คณ ๐ ๐บ ๐ฏโโ๏ธ ๐ฏ ๐ฏโโ๏ธ ๐ด ๐ฉโ๐ฆฝ ๐งโ๐ฆฝ ๐จโ๐ฆฝ ๐ฉโ๐ฆผ ๐งโ๐ฆผ ๐จโ๐ฆผ ๐ถโโ๏ธ 
๐ถ ๐ถโโ๏ธ ๐ฉโ๐ฆฏ ๐งโ๐ฆฏ ๐จโ๐ฆฏ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐โโ๏ธ ๐ ๐โโ๏ธ ๐งโโ๏ธ ๐ง ๐งโโ๏ธ ๐ญ ๐งโ๐คโ๐ง ๐ฌ ๐ซ ๐ฉโโค๏ธโ๐ฉ ๐ ๐จโโค๏ธโ๐จ ๐ฉโโค๏ธโ๐จ ๐ฉโโค๏ธโ๐โ๐ฉ ๐ 
๐จโโค๏ธโ๐โ๐จ ๐ฉโโค๏ธโ๐โ๐จ ๐ช ๐จโ๐ฉโ๐ฆ ๐จโ๐ฉโ๐ง ๐จโ๐ฉโ๐งโ๐ฆ ๐จโ๐ฉโ๐ฆโ๐ฆ ๐จโ๐ฉโ๐งโ๐ง ๐จโ๐จโ๐ฆ ๐จโ๐จโ๐ง ๐จโ๐จโ๐งโ๐ฆ ๐จโ๐จโ๐ฆโ๐ฆ ๐จโ๐จโ๐งโ๐ง ๐ฉโ๐ฉโ๐ฆ ๐ฉโ๐ฉโ๐ง ๐ฉโ๐ฉโ๐งโ๐ฆ ๐ฉโ๐ฉโ๐ฆโ๐ฆ ๐ฉโ๐ฉโ๐งโ๐ง ๐จโ๐ฆ ๐จโ๐ฆโ๐ฆ ๐จโ๐ง ๐จโ๐งโ๐ฆ ๐จโ๐งโ๐ง ๐ฉโ๐ฆ ๐ฉโ๐ฆโ๐ฆ ๐ฉโ๐ง ๐ฉโ๐งโ๐ฆ ๐ฉโ๐งโ๐ง ๐ฃ ๐ค ๐ฅ ๐ซ"""

EMOJIS = SMILY.split(" ")
QNA = ("who are you", "who are you?", "what are you doing", "what are you doing?", "what is your name", "what is your name?",
       "which is your favourite color", "what is your favourite color")
JOKES = ("i love you", "will you marry me", "i like you")
COMMAND1 = ("time", "time?", "what is the time", "what is the time?",
            "what is the time now", "what is the time now?")
COMMAND2 = ("date", "date?", "what is the date", "what is the date?",
            "what is the date today", "what is the date today?")
REPLY = ("i'm fine", "i am also fine", "i'm also fine", "not good", "i'm not fine",
         "nice", "fine", "good", "i'm good")
CARE = ("how are you", "how do you do")
DAY_COMMAND = ("day", "day?", "today", "today?",
               "which day today", "which day today?")
MONTH_COMMAND = ("month", "month?", "which month", "which month?")


def DHANUSHHV_bot(user_input):
    # convert the user_input to string
    user_input = str(user_input).lower()

    if user_input in WISHES:
        if "bye" in user_input or "see ya" in user_input or "see you" in user_input:
            return "See you later, bye ๐"

        return "Hi there! ๐"

    elif "help" in user_input:
        with open("example_cmd.txt", 'r') as f:
            return f.read()

    elif user_input in QNA:
        if QNA[2] in user_input:
            return "I'm chating with you"

        elif QNA[4] in user_input:
            return "My name is DhanushBot"

        elif QNA[6] in user_input:
            return "My favorite color is BLACK"

        return "I'm DhanushBOT and I developed by Dhanush H V"

    elif user_input in JOKES:
        return "I hope we are good friends together ๐"

    elif user_input in COMMAND1:
        hour = int(strftime("%H"))
        if hour > 12:
            hour -= 12

        if hour > 9:
            time = strftime(f"{hour}:%M:%S %p")
        else:
            time = strftime(f"0{hour}:%M:%S %p")
            
        return time

    elif user_input in CARE:
        return "Im fine ๐, Thanks for asking\nHow do you do?"

    elif user_input in SMALL_WORD:
        if "emoji" in user_input:
            return random.choice(EMOJIS)
        elif "what" in user_input:
            return "Nothing, tell me about you"

        else:
            return "Ok Fine, see ya.."

    elif user_input in REPLY:
        if user_input in REPLY[0:3]:
            return "Nice to hear ๐"

        elif "not good" in user_input:
            return "My heart warming, god bless you..."

        else:
            return "OK, fine!!!"

    elif user_input in COMMAND2:
        return strftime("%d/%m/%Y")

    elif user_input in DAY_COMMAND:
        WEEK_DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday")
        return f"Today is {WEEK_DAYS[datetime.now().weekday()+1].title()}"

    elif user_input in MONTH_COMMAND:
        MONTHS = ("January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December")
        return MONTHS[datetime.now().month-1]

    else:
        try:
            return eval(user_input)
        except Exception:
            return "I didn't get it, will you repeat it"
