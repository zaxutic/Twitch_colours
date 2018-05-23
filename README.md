# Twitch_colours
Script to automatically change username colour upon sending a message

## Setup
- Create an `auth` file in the same directory, with your username and oauth token, separated by a space.
- Add channel name for script to run in between quotes in line 70 **OR**  give channel name as input when running script.

## Requirements
- Python 3.x.x

## Running
### Windows
`python colours.py` or execute the file directly
### Mac OS X/Linux
`python3 colours.py`

## Issues
- Only runs within a single channel. Run the script multiple times if you wish to use it in multiple channels.
- Changes in colour will not display if multiple successive messages are sent too quickly.
