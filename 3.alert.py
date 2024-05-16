import requests
import socket
import datetime

def get_server_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    # check stage http
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")
        
# bot token and chat id
bot_token = 'Your Token Telegram'
chat_id = your ID telegram

# get time now
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# get name server and ip
server_name, server_ip = get_server_ip()

# messages
message = f"""

🖥️   Server:    {server_name} 
🌐  IP:        {server_ip} 
⏰  Time:      {current_time}
🟢  Status:    'Jenkins CI/CD SUCCESS'