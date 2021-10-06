from telegram.ext import *
import constants as key
import resources as res

print("DHANUSH Bot started...\n")


def updateData(filename, context):
    with open(filename, 'a') as f:
        f.write(context)


def USER_INFO(user, bot):
    return f"USER({user.message.chat.first_name}): {user.message.text}\nBOT: {bot}\nTime: {res.DHANUSHHV_bot('time')}\n"


def start_command(update, context):
    global info, username, name, user_id, txtFile
    info = update.message.chat
    username = info.username
    name = f"{info.first_name} {info.last_name}"
    user_id = info.id
    txtFile = f"conversations/{username}_{name}.txt"

    app = f"========== DHANUSH BOT ===========\nUsername: {username}\nName: {name}\nUser ID: {user_id}\nTime: {res.DHANUSHHV_bot('time')}\nDate: {res.DHANUSHHV_bot('date')}\n=================================\n"
    print(app)

    updateData(txtFile, app)
    txt = "Hey I'm DhanushBOT, start saying Hi 🙋"
    update.message.reply_text(txt)
    txt = USER_INFO(update, txt)
    updateData(txtFile, txt)


def help_command(update, context):
    print(username)
    with open("example_cmd.txt", 'r') as f:
        txt = f.read()
    update.message.reply_text(txt)
    print(USER_INFO(update, txt))
    updateData(txtFile, "\n" + USER_INFO(update, txt))


def handle_command(update, context):
    text = str(update.message.text).lower()
    response = res.DHANUSHHV_bot(text)
    update.message.reply_text(response)
    print(USER_INFO(update, response))
    updateData(txtFile, "\n" + USER_INFO(update, response))


def error(update, context):
    print(f"{update} caused an error {context.error}")


def main():
    updater = Updater(key.TELEGRAM_API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_command))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
