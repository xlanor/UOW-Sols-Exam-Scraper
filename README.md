<h1 align="center">UOW-Sols Exam Result Scraper </h1>

[![License: MIT License](https://img.shields.io/dub/l/vibe-d.svg)](LICENSE) [![pythonver](https://img.shields.io/badge/python-3.6%2B-ff69b4.svg)](https://www.python.org/) [![Build Status](https://travis-ci.com/xlanor/UOW-Sols-Exam-Scraper.svg?branch=master)](https://travis-ci.com/xlanor/UOW-Sols-Exam-Scraper) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

<hr>

<p align="center">
<i>Because email notifications dont exist.</i>
</p>

This is a rudimentary telegram bot that directly accesses the telegram API directly, not using a framework.

It will first scrape the relevant information from SOLS using headless chrome, and trigger a message to the telegram user through the telegram API.

The modules to be targeted must be set.

<hr>

#### Setup

**NOT SUPPORTED FOR WINDOWS**

The following file **MUST** be placed in src/.

The file name **MUST** be called **config.json**

Fill in the relevant details accordingly. If you need help with using telegram bots, google it.

>	  {
>	       "token": "telegram_bot_token_here",
>	       "channelID":"channel_id_or_group_id",
>	       "clientUsn": "sols_user_name",
>	       "clientPw": "sols_password",
>           "modulesToFind":[
>                   "CSCI204","CSCI235"
>               ]
>     }

Google Chrome is used as the preferred browser for selenium. Install using apt-get/ .exe/.msi/.app file directly, whatever.

*For ubuntu*

>	  sudo apt-get update
>	  sudo apt-get install -y libappindicator1 fonts-liberation
>	  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
>	  sudo dpkg -i google-chrome*.deb

If you run into dependecy issues when installing, use
>	  sudo apt fix-broken install

It is highly recomended to set up a virtual environment.

[Documentation](https://docs.python.org/3/library/venv.html) on using venvs is linked here.


[ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=2.45/) must be placed in src/


Dependecies are managed with [Poetry](https://github.com/sdispater/poetry).


After setting up the venv, you can then run 
>	  poetry install


I ran this headlessly using pm2, with the following in the src/ folder
> pm2 start ./main.py --interpreter path-to-venv-bin-python


I dont actually know if this really works yet, I guess we'll find out.
