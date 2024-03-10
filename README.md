# Melvin - personal telegram bot

A Telegram bot that allows you to control your PC remotely from anywhere using your mobile device.

## Description

This Telegram bot is built using Python-telegram-bot library and enables users to execute various commands on their PC through Telegram messages. It provides functionalities like opening specific websites, running CMD scripts, retrieving active window title, switching windows, and controlling system power options such as restart and shutdown.

## Prerequisites

- Python 3.8+
- python-telegram-bot==21.0.1 
- PyAutoGUI==0.9.54

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/anuragk16/Melvin---personal-telegram-bot
    cd Melvin---personal-telegram-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirement.txt
    ```

3. Obtain Telegram bot token:
    - To create a new bot and obtain the bot token.
    ```bash
    Open telegram on any device and login. 
    Tap on the start conversation button in the bottom right to start a new conversation.
    Tap the magnifying glass “Search” icon near the top right.
    Type “botfather”.
    Tap on the “@BotFather” that appears. Make sure it has a blue checkmark next to it
    It will display a welcome message.
    Click the “Start” button.
    Send a message “/newbot”
    ```

4. Set up the bot token and required variables:
    - Set the following values in `setting.py`
    ```bash
    username : str = "Your_username"
    user_id : int = "Your_id"
    token_ : str = "Your_Token"
    ```

    To get the username and id:
    ```bash
    Open telegram on any device. 
    Tap on the start conversation button in the bottom right to start a new conversation.
    Tap the magnifying glass “Search” icon near the top right.
    Type “userinfobot”.
    Tap on the “@userinfobot” that appears.
    It will display a welcome message.
    Click the “Start” button.
    You will get a message with first line contain your username ( @your_username)
    And second line contain Id
    ```

6. Run the bot:
    ```bash
    python main.py
    ```

## Usage

1. Start the bot by sending `/start` command to it.
2. Use `/help` command to get information about available commands.
3. Send specific commands like `/google`, `/youtube`, `/cmd_hack`, etc., to execute corresponding actions on your PC.
4. To search on Google, type "GS" followed by the text to be searched.
5. To search on YouTube, type "YS" followed by the text to be searched.
6. Enter keyboard mode to use keyboard commands. Use `/exit_keyboard` to exit keyboard mode.
7. To type on the current window, write "TYPE" followed by the text you want to type. For example, if you want to type "Hello World", send the message "TYPE Hello World". This will type "Hello World" on your PC's current window (If there is typing area).
8. Note: The `/cmd_hack` command is not harmful; it is just for demonstration purposes. It runs a CMD script as a demonstration and does not perform any harmful actions.

## Commands

- `/start`: Start the bot.
- `/help`: Get information about available commands.
- `/google`: Open Google in the default browser.
- `/youtube`: Open YouTube in the default browser.
- `/cmd_hack`: Run CMD script.
- `/awt`: Show active window title.
- `/altab`: Switch window.
- `/close_sys`: Close current window.
- `/restart`: Restart the system.
- `/shutdown`: Shutdown the system.
- `/keyboard_mode`: Enter keyboard mode.

## Screenshot:

![Screenshot 2024-03-10 104923](https://github.com/anuragk16/Melvin---personal-telegram-bot/assets/90235816/2462746e-86f0-47f8-a488-314dd4e32f49)

![Screenshot 2024-03-10 104840](https://github.com/anuragk16/Melvin---personal-telegram-bot/assets/90235816/cf63359c-b34f-4bd2-88c8-431fe079b244)

# Future Updates

We're constantly working on improving the functionality and usability of this Telegram PC Control Bot. Here are some planned updates for future releases:

## Future Updates

I'm constantly working on improving the functionality and usability of this Telegram PC Control Bot. Here are some planned updates for future releases:

### Planned Features

1. **Screenshot Feature**: I plan to add a feature that allows users to request a screenshot of their PC's current screen through the Telegram bot. This will enable users to remotely view their PC's screen directly from their mobile device.

2. **Audio Messages**: In addition to text commands, I aim to introduce support for sending and receiving audio messages within the Telegram bot. This feature will enhance the user experience by enabling voice-based communication with the bot.

3. **Voice Commands**: I'm exploring the implementation of voice recognition capabilities to interpret voice commands sent to the bot. Users will be able to control their PC using voice commands, making the interaction more intuitive and convenient.

Stay tuned for updates on these exciting features! I'm dedicated to delivering an even more powerful and user-friendly experience with each new release.


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library contributors.



