# instaclient

**instaclient** is a Python library for accessing Instagram's features.
With this library you can create Instagram Bots with ease and simplicity. The InstaClient takes advantage of the selenium library to excecute tasks which are not allowed in the Instagram Graph API (such as sending DMs).

The only thing you need to worry about is to spread your requests throughout the day to avoid reaching Instagram spam limits.
> **Disclaimer:** Please note that this is a research project. **I am by no means responsible for any usage of this tool.** Use it on your behalf. I'm also not responsible if your accounts get banned due to the extensive use of this tool.

## Table of Contents

1. [Current Features](#current-features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [Help - Community](#help-community)
6. [Credits](#credits)
7. [License](#license)

## Current Features
- Scrape a user's followers
- Scrape a Hashtag
- Scrape a profile
- Scrape a user's posts
- Scrape a post's info via its shortcode
- Follow a user
- Unfollow a user
- Send DMs to users (both Private & Public)
- Check Incoming Notifications
- Like a post
- Add a comment on a post


#### TO DO:
- [x] Define Classes:
    - [x] Comment
    - [x] Post
    - [x] Location
- [x] Scrape User Posts's shorturl
- [x] Scrape Post by shorturl
- [x] Add comment to post by shorturl
- [x] Like post by shorturl
- [ ] Unlike post by shorturl
- [ ] Scrape Location


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install instaclient.

```bash
pip install instaclient
```
To update the package:
```bash
pip install -U instaclient
```

## Usage
#### INSTALL A DRIVER (LocalHost)
If you are running your code on a localhost, then you'll need to install a chromedriver from [here](https://chromedriver.chromium.org/downloads). Install and extract the chromedriver.exe file and save it in your project folder. Make sure to install the version that matches your Chrome version.
To check your chrome version, type ```chrome://version/``` in the chrome address bar.

#### SET ENVIROMENT VARIABLES (Web Server)
If you are running your code on a web server (Like Heroku), you should set the following enviroment variable:
- ```CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver```
- ```GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome```

#### CREATE THE CLIENT
```python
from instaclient import InstaClient
from instaclient.errors import *

# Create a instaclient object. Place as driver_path argument the path that leads to where you saved the chromedriver.exe file
client = InstaClient(driver_path='<projectfolder>/chromedriver.exe')
```
#### LOGIN INTO INSTAGRAM
```python
from instaclient.errors import *

try:
    client.login(username=username, password=password) # Go through Login Procedure
except VerificationCodeNecessary:
    # This error is raised if the user has 2FA turned on.
    code = input('Enter the 2FA security code generated by your Authenticator App or sent to you by SMS')
    client.input_verification_code(code)
except SuspisciousLoginAttemptError as error:
    # This error is reaised by Instagram
    if error.mode == SuspisciousLoginAttemptError.EMAIL:
        code = input('Enter the security code that was sent to you via email: ')
    else:
        code = input('Enter the security code that was sent to you via SMS: ')
    client.input_security_code(code)
```
#### SEND A DIRECT MESSAGE
```python
result = client.send_dm('<username>', '<Message to send>') # send a DM to a user
```
> Make sure to distrubute your client.send_dm() requests over a period of time to avoid reaching Instagram's spam limits.
#### GET A USER'S FOLLOWERS
```python
followers = client.get_followers(user='<username>') # replace with the target username
```
> The client.scrape_followers() method can take a lot of time depending on the amount of followers you want to scrape.

This method might be updated in the near future to cache scraped data in a SQLite database or to scrape the followers in a separate thread with a queue.
#### SCRAPE NOTIFICATIONS
```python
notifications = client.get_notifications(count=10)
```
> This returns a Notification object, which contains information about the type of notification and the user who caused it.
#### SCRAPE A PROFILE
```python
profile = client.get_profile('<username>')
```
> This returns a Profile object, from which you can get posts and all sorts of information.
#### SCRAPE A PROFILE's POSTS
```python
posts = client.get_user_posts('<username>', count=10)
# or:
profile = client.get_profile('<username>')
profile.get_posts(30)
```
> This returns a list of Post objects.
#### SCRAPE A HASHTAG
```python
hashtag = client.get_hashtag(tag='<tag>')
```
> This returns a Hashtag object, from which you can get the posts data. Using load_posts(), you get a list of BasePost objects, from which you can get the owner of the post
#### ADD A COMMENT
```python
client.comment_post('<post_shortcode>', text='Nice post!')
# or:
post = client.get_user_posts('<username>', count=1)[0]
post.add_comment('Nice post!')
```
#### LIKE A POST
```python
client.like_post('<post_shortcode>')
# or:
post = client.get_user_posts('<username>', count=1)[0]
post.like()
```
#### FOLLOW A USER
```python
client.follow_user('<username>')
# or:
profile = client.get_profile('<username>')
profile.follow()
```
#### UNFOLLOW A USER
```python
client.unfollow_user('<username>')
# or:
profile = client.get_profile('<username>')
profile.unfollow()
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update [tests](https://github.com/wickerdevs/instaclient/tree/master/tests) as appropriate.

## Help Community
You can join this [Telegram Group](https://t.me/instaclient) to ask questions about the instabot's functionalities or to contribute to the package!

## Credits
[AUTHORS](https://github.com/wickerdevs/instaclient/blob/master/AUTHORS.rst)

## License
[MIT](https://choosealicense.com/licenses/mit/)


