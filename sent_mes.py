import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1066154501:AAE9wTQJSv-7GVZC7RLY9RVM8zkGU7cfN88'
    bot_chatID = '757597475'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)