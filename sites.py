# sites.py
import requests
import hashlib
import time
import json

# ---------- Helper function for requests ----------
def send_request(url, method="GET", data=None, headers=None, cookies=None):
    time.sleep(1.5)
    if headers is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }
    try:
        if method.upper() == "GET":
            r = requests.get(url, headers=headers, cookies=cookies, timeout=15)
        else:
            r = requests.post(url, data=data, headers=headers, cookies=cookies, timeout=15)
        return r
    except Exception as e:
        print(f"Request error: {e}")
        return None

# ---------- Placeholder ----------
def not_implemented(email):
    return None

# ========== WORKING CHECK FUNCTIONS ==========
def check_gravatar(email):
    email_hash = hashlib.md5(email.lower().strip().encode()).hexdigest()
    url = f"https://en.gravatar.com/{email_hash}.json"
    r = send_request(url)
    if r is None:
        return None
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
        return False   # NOT REGISTERED
    else:
        return None

def check_lastfm(email):
    url = "https://www.last.fm/forgot-password"
    data = {"email": email}
    headers = {"Referer": "https://www.last.fm/forgot-password"}
    r = send_request(url, method="POST", data=data, headers=headers)
    if r is None:
        return None
    if "Email not found" in r.text or "That email address is not registered" in r.text:
        return False
    elif "reset link sent" in r.text.lower() or "you'll receive an email" in r.text.lower():
        return True
    else:
        return None

def check_flickr(email):
    url = "https://identity.flickr.com/forgot-password"
    data = {"email": email}
    headers = {"Referer": "https://identity.flickr.com/forgot-password"}
    r = send_request(url, method="POST", data=data, headers=headers)
    if r is None:
        return None
    if "No account found" in r.text or "doesn't have a Flickr account" in r.text:
        return False
    elif "reset password" in r.text.lower() and "sent" in r.text.lower():
        return True
    else:
        return None

def check_tumblr(email):
    url = "https://www.tumblr.com/forgot"
    data = {"email": email}
    headers = {"Referer": "https://www.tumblr.com/forgot"}
    r = send_request(url, method="POST", data=data, headers=headers)
    if r is None:
        return None
    if "We couldn't find an account" in r.text:
        return False
    elif "reset your password" in r.text.lower() and "sent" in r.text.lower():
        return True
    else:
        return None

def check_quora(email):
    url = "https://www.quora.com/forgot"
    data = {"email": email}
    headers = {"Referer": "https://www.quora.com/forgot"}
    r = send_request(url, method="POST", data=data, headers=headers)
    if r is None:
        return None
    if "No account found" in r.text or "doesn't have a Quora account" in r.text:
        return False
    elif "reset link sent" in r.text.lower():
        return True
    else:
        return None

def check_pinterest(email):
    url = "https://www.pinterest.com/reset"
    data = {"email": email}
    headers = {"Referer": "https://www.pinterest.com/reset"}
    r = send_request(url, method="POST", data=data, headers=headers)
    if r is None:
        return None
    if "Couldn't find your account" in r.text:
        return False
    elif "reset link sent" in r.text.lower():
        return True
    else:
        return None

def check_discord(email):
    url = "https://discord.com/api/v9/auth/forgot"
    headers = {"Content-Type": "application/json", "Referer": "https://discord.com/"}
    data = {"email": email}
    r = send_request(url, method="POST", headers=headers, data=json.dumps(data))
    if r is None:
        return None
    try:
        resp = r.json()
        if resp.get("message") == "You will be emailed a link to reset your password.":
            return True
        elif resp.get("message") == "User not found":
            return False
        else:
            return None
    except:
        return None

def check_reddit(email):
    url = "https://www.reddit.com/api/forgot"
    data = {"email": email}
    headers = {"Referer": "https://www.reddit.com/"}
    r = send_request(url, method="POST", data=data, headers=headers)
    if r is None:
        return None
    if "We don't recognize that email" in r.text:
        return False
    elif "reset link sent" in r.text.lower():
        return True
    else:
        return None

# ========== MASTER SITE LIST ==========
SITES = [
    {"name": "Apple", "func": not_implemented},
    {"name": "Ebay", "func": not_implemented},
    {"name": "Facebook", "func": not_implemented},
    {"name": "Flickr", "func": check_flickr},
    {"name": "Foursquare", "func": not_implemented},
    {"name": "Github", "func": not_implemented},
    {"name": "Google", "func": not_implemented},
    {"name": "Gravatar", "func": check_gravatar},   # now returns False for 404
    {"name": "Instagram", "func": not_implemented},
    {"name": "Lastfm", "func": check_lastfm},
    {"name": "Linkedin", "func": not_implemented},
    {"name": "Microsoft", "func": not_implemented},
    {"name": "Myspace", "func": not_implemented},
    {"name": "Pinterest", "func": check_pinterest},
    {"name": "Skype", "func": not_implemented},
    {"name": "Spotify", "func": not_implemented},
    {"name": "Tumblr", "func": check_tumblr},
    {"name": "Twitter", "func": not_implemented},
    {"name": "Vimeo", "func": not_implemented},
    {"name": "Weibo", "func": not_implemented},
    {"name": "Yahoo", "func": not_implemented},
    {"name": "Discord", "func": check_discord},
    {"name": "Ok", "func": not_implemented},
    {"name": "Kakao", "func": not_implemented},
    {"name": "Booking", "func": not_implemented},
    {"name": "Airbnb", "func": not_implemented},
    {"name": "Amazon", "func": not_implemented},
    {"name": "Qzone", "func": not_implemented},
    {"name": "Adobe", "func": not_implemented},
    {"name": "Mailru", "func": not_implemented},
    {"name": "Wordpress", "func": not_implemented},
    {"name": "Imgur", "func": not_implemented},
    {"name": "Disneyplus", "func": not_implemented},
    {"name": "Netflix", "func": not_implemented},
    {"name": "Jdid", "func": not_implemented},
    {"name": "Flipkart", "func": not_implemented},
    {"name": "Bukalapak", "func": not_implemented},
    {"name": "Archiveorg", "func": not_implemented},
    {"name": "Lazada", "func": not_implemented},
    {"name": "Zoho", "func": not_implemented},
    {"name": "Samsung", "func": not_implemented},
    {"name": "Evernote", "func": not_implemented},
    {"name": "Envato", "func": not_implemented},
    {"name": "Patreon", "func": not_implemented},
    {"name": "Tokopedia", "func": not_implemented},
    {"name": "Rambler", "func": not_implemented},
    {"name": "Quora", "func": check_quora},
    {"name": "Atlassian", "func": not_implemented},
    {"name": "TikTok", "func": not_implemented},
    {"name": "Snapchat", "func": not_implemented},
    {"name": "Reddit", "func": check_reddit},
    {"name": "Telegram", "func": not_implemented},
    {"name": "Twitch", "func": not_implemented},
    {"name": "Medium", "func": not_implemented},
    {"name": "VK", "func": not_implemented},
    {"name": "Etsy", "func": not_implemented},
    {"name": "Alibaba", "func": not_implemented},
    {"name": "AliExpress", "func": not_implemented},
    {"name": "Wish", "func": not_implemented},
    {"name": "Groupon", "func": not_implemented},
    {"name": "Rakuten", "func": not_implemented},
    {"name": "Newegg", "func": not_implemented},
    {"name": "Best Buy", "func": not_implemented},
    {"name": "Target", "func": not_implemented},
    {"name": "Home Depot", "func": not_implemented},
    {"name": "IKEA", "func": not_implemented},
    {"name": "Shopify", "func": not_implemented},
    {"name": "Hulu", "func": not_implemented},
    {"name": "HBO Max", "func": not_implemented},
    {"name": "Paramount+", "func": not_implemented},
    {"name": "Peacock", "func": not_implemented},
    {"name": "SoundCloud", "func": not_implemented},
    {"name": "Bandcamp", "func": not_implemented},
    {"name": "Deezer", "func": not_implemented},
    {"name": "Tidal", "func": not_implemented},
    {"name": "Dailymotion", "func": not_implemented},
    {"name": "Crunchyroll", "func": not_implemented},
    {"name": "GitLab", "func": not_implemented},
    {"name": "Bitbucket", "func": not_implemented},
    {"name": "Docker Hub", "func": not_implemented},
    {"name": "npm", "func": not_implemented},
    {"name": "PyPI", "func": not_implemented},
    {"name": "RubyGems", "func": not_implemented},
    {"name": "Heroku", "func": not_implemented},
    {"name": "Netlify", "func": not_implemented},
    {"name": "Vercel", "func": not_implemented},
    {"name": "DigitalOcean", "func": not_implemented},
    {"name": "Linode", "func": not_implemented},
    {"name": "Notion", "func": not_implemented},
    {"name": "Airtable", "func": not_implemented},
    {"name": "Asana", "func": not_implemented},
    {"name": "Monday.com", "func": not_implemented},
    {"name": "ClickUp", "func": not_implemented},
    {"name": "Zapier", "func": not_implemented},
    {"name": "IFTTT", "func": not_implemented},
    {"name": "Canva", "func": not_implemented},
    {"name": "Figma", "func": not_implemented},
    {"name": "Dropbox", "func": not_implemented},
    {"name": "Box", "func": not_implemented},
    {"name": "Slack", "func": not_implemented},
    {"name": "Zoom", "func": not_implemented},
]
