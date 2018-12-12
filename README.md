<h1 align="center">UOW-Sols Exam Result Scraper </h1>

[![License: MIT License](https://img.shields.io/dub/l/vibe-d.svg)](LICENSE.md) [![pythonver](https://img.shields.io/badge/python-3.6%2B-ff69b4.svg)](https://www.python.org/) [![Build Status](https://travis-ci.com/xlanor/UOW-Sols-Exam-Scraper.svg?branch=master)](https://travis-ci.com/xlanor/UOW-Sols-Exam-Scraper) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

<hr>

<p align="center">
<i>Because email notifications dont exist.</i>
</p>

This is a rudimentary telegram bot that directly accesses the telegram API directly, not using a framework.

It will first scrape the relevant information from SOLS using headless chrome, and trigger a message to the telegram user through the telegram API.

<hr>

#### Setup

**NOT SUPPORTED FOR WINDOWS**

The following file config.json **MUST** be placed in the src file.

Fill in the relevant details accordingly. If you need help with using telegram bots, google it.

>	  {
>	       "token": "telegram_bot_token_here",
>	       "channelID":"channel_id_or_group_id",
>	       "clientUsn": "sols_user_name",
>	       "clientPw": "sols_password"
>     }

Google Chrome is used as the preferred browser for selenium. Install using apt-get/ .exe/.msi/.app file directly, whatever.

[ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=2.45/) must be placed in src/


Dependecies are managed with [Poetry](https://github.com/sdispater/poetry).

I dont actually know if this really works yet, I guess we'll find out.