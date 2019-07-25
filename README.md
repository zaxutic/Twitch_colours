# Twitch_colours
Script to automatically change username colour upon sending a message

## Setup
- Get an OAuth token from https://twitchapps.com/tmi/
- Rename the `example_auth.py` file in `config` to `auth.py` and replace the placeholder string values with the appropriate values. I.e. replace `YOUR_USERNAME_HERE` with your twitch username and `YOUR_OAUTH_TOKEN_HERE` with the OAuth token you just retrieved from the above link.
- Likewise, rename the `example_channels.json` file in `config` to `channels.json` and change the file to have the channels you want the script to run in. Make sure every entry except the final one has a comma following it.
- Install all package dependencies with `pip install -r requirements.txt`

## Requirements
- Python 3.6+
- Package dependencies are in `requirements.txt`

## Runnings
### Windows
`py -3 colours.py`

### Linux/Unix
`python colours.py`

## Note
During muliple quick successive messages, changes in colour may not display due to delays in Twitch (not the script). The colours also tend to be a message behind in Twitch chat for yourself compared to what other viewers in chat see (so if you see your username as red everyone else probably sees it as orange).
