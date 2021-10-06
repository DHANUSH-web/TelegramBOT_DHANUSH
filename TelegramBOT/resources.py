from os import replace
from time import strftime
from datetime import datetime
import random

WISHES = ("hey", "hello", "hi", ":)", "hi there", "bye", "see you")
SMALL_WORD = ("what", "what?", "ok", "emoji")

SMILY = """😀 😃 😄 😁 😆 😅 😂 🤣 🥲😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 
😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🥸 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖 😫 😩 
🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 
😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 
👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾 👋 🤚 🖐 ✋ 
🖖 👌 🤌 🤏 ✌️ 🤞 🤟 🤘 🤙 👈 👉 👆 🖕 👇 ☝️ 👍 👎 ✊ 👊 🤛 🤜 👏 🙌 👐 
🤲 🤝 🙏 ✍️ 💅 🤳 💪 🦾 🦵 🦿 🦶 👣 👂 🦻 👃 🫀 🫁 🧠 🦷 🦴 👀 👁 👅 👄 
💋 🩸 👶 👧 🧒 👦 👩 🧑 👨 👩‍🦱 🧑‍🦱 👨‍🦱 👩‍🦰 🧑‍🦰 👨‍🦰 👱‍♀️ 👱 👱‍♂️ 👩‍🦳 🧑‍🦳 👨‍🦳 👩‍🦲 🧑‍🦲 👨‍🦲 
🧔 👵 🧓 👴 👲 👳‍♀️ 👳 👳‍♂️ 🧕 👮‍♀️ 👮 👮‍♂️ 👷‍♀️ 👷 👷‍♂️ 💂‍♀️ 💂 💂‍♂️ 🕵️‍♀️ 🕵️ 🕵️‍♂️ 👩‍⚕️ 🧑‍⚕️ 👨‍⚕️ 
👩‍🌾 🧑‍🌾 👨‍🌾 👩‍🍳 🧑‍🍳 👨‍🍳 👩‍🎓 🧑‍🎓 👨‍🎓 👩‍🎤 🧑‍🎤 👨‍🎤 👩‍🏫 🧑‍🏫 👨‍🏫 👩‍🏭 🧑‍🏭 👨‍🏭 👩‍💻 🧑‍💻 👨‍💻 👩‍💼 🧑‍💼 👨‍💼 👩‍🔧 🧑‍🔧 👨‍🔧 👩‍🔬 🧑‍🔬 👨‍🔬 👩‍🎨 🧑‍🎨 👨‍🎨 👩‍🚒 🧑‍🚒 👨‍🚒 👩‍✈️ 🧑‍✈️ 👨‍✈️ 👩‍🚀 🧑‍🚀 👨‍🚀 👩‍⚖️ 🧑‍⚖️ 👨‍⚖️ 👰‍♀️ 👰 👰‍♂️ 
🤵‍♀️ 🤵 🤵‍♂️ 👸 🤴 🥷 🦸‍♀️ 🦸 🦸‍♂️ 🦹‍♀️ 🦹 🦹‍♂️ 🤶 🧑‍🎄 🎅 🧙‍♀️ 🧙 🧙‍♂️ 🧝‍♀️ 🧝 🧝‍♂️ 🧛‍♀️ 🧛 🧛‍♂️ 
🧟‍♀️ 🧟 🧟‍♂️ 🧞‍♀️ 🧞 🧞‍♂️ 🧜‍♀️ 🧜 🧜‍♂️ 🧚‍♀️ 🧚 🧚‍♂️ 👼 🤰 🤱 👩‍🍼 🧑‍🍼 👨‍🍼 🙇‍♀️ 🙇 🙇‍♂️ 💁‍♀️ 💁 💁‍♂️ 
🙅‍♀️ 🙅 🙅‍♂️ 🙆‍♀️ 🙆 🙆‍♂️ 🙋‍♀️ 🙋 🙋‍♂️ 🧏‍♀️ 🧏 🧏‍♂️ 🤦‍♀️ 🤦 🤦‍♂️ 🤷‍♀️ 🤷 🤷‍♂️ 🙎‍♀️ 🙎 🙎‍♂️ 🙍‍♀️ 🙍 🙍‍♂️ 
💇‍♀️ 💇 💇‍♂️ 💆‍♀️ 💆 💆‍♂️ 🧖‍♀️ 🧖 🧖‍♂️ 💅 🤳 💃 🕺 👯‍♀️ 👯 👯‍♂️ 🕴 👩‍🦽 🧑‍🦽 👨‍🦽 👩‍🦼 🧑‍🦼 👨‍🦼 🚶‍♀️ 
🚶 🚶‍♂️ 👩‍🦯 🧑‍🦯 👨‍🦯 🧎‍♀️ 🧎 🧎‍♂️ 🏃‍♀️ 🏃 🏃‍♂️ 🧍‍♀️ 🧍 🧍‍♂️ 👭 🧑‍🤝‍🧑 👬 👫 👩‍❤️‍👩 💑 👨‍❤️‍👨 👩‍❤️‍👨 👩‍❤️‍💋‍👩 💏 
👨‍❤️‍💋‍👨 👩‍❤️‍💋‍👨 👪 👨‍👩‍👦 👨‍👩‍👧 👨‍👩‍👧‍👦 👨‍👩‍👦‍👦 👨‍👩‍👧‍👧 👨‍👨‍👦 👨‍👨‍👧 👨‍👨‍👧‍👦 👨‍👨‍👦‍👦 👨‍👨‍👧‍👧 👩‍👩‍👦 👩‍👩‍👧 👩‍👩‍👧‍👦 👩‍👩‍👦‍👦 👩‍👩‍👧‍👧 👨‍👦 👨‍👦‍👦 👨‍👧 👨‍👧‍👦 👨‍👧‍👧 👩‍👦 👩‍👦‍👦 👩‍👧 👩‍👧‍👦 👩‍👧‍👧 🗣 👤 👥 🫂"""

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
            return "See you later, bye 👋"

        return "Hi there! 😊"

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
        return "I hope we are good friends together 😁"

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
        return "Im fine 😇, Thanks for asking\nHow do you do?"

    elif user_input in SMALL_WORD:
        if "emoji" in user_input:
            return random.choice(EMOJIS)
        elif "what" in user_input:
            return "Nothing, tell me about you"

        else:
            return "Ok Fine, see ya.."

    elif user_input in REPLY:
        if user_input in REPLY[0:3]:
            return "Nice to hear 😇"

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
