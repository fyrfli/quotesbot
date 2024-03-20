# @quotesbot

This is the code that posts to https://fyrfli.social/quotesbot.

## Requirements:
- some knowledge of the linux command line
- python installed
- a Mastodon-compatible API token for your instance
- a json-formatted file of quotes to use formatted thus:
    ```
    "quote": "quote"
    "author": "author"
    ```
Your quotes file can either be in the local directory or accessible at a url.

## To install:

- Download the release package
- Extract into your chosen directory:
    - `mkdir quotesbot && cd quotesbot`
    - `tar xfz | gunzip source.[zip|tar.gz]`
- If you have other projects, you can create a virtual environment to run this code:
    - `python3 -m venv .venv` 
    - `source .venv/bin/activate`
    - `python3 -m pip install -r requirements.txt`
- Otherwise, just install from the requirements.txt: `python3 -m pip install -r requirements.txt`
- Copy the env.example to .env and change the values to your own

## To use:
- You can either run the code without any arguments: `python3 random_quotes.py` or you can pass **one** argument through to the code to select a specific quote to post:
    - `python3 random_quotes.py 1`

## Caveats
This is code is *very* rudimentary. It serves a specific purpose:
- To post my favourite quotes to my timeline every few hours
- To practice my python coding skills

## Going forward
It is possible that I may continue to work on this to a point where it's a more sophisticated module, but I can almost guarantee that there are packages out there that do this and more with far more finesse. 
