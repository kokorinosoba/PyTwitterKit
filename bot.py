import sys
import json
from requests_oauthlib import OAuth1Session
from setting import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class Twitter():
    def __init__(self):
        self.requests = OAuth1Session(API_KEY,
                                      API_SECRET_KEY,
                                      ACCESS_TOKEN,
                                      ACCESS_TOKEN_SECRET)

    def print_tweet(self, result):
        if result.status_code == 200:
            tweets = json.loads(result.text)
            print("-" * 60)
            if type(tweets) == dict:
                tweets = tweets["statuses"]
            for tweet in tweets:
                print(f'{tweet["user"]["name"]} @{tweet["user"]["screen_name"]} ID:{tweet["id_str"]}\n{tweet["full_text"]}')
                print("-" * 60)

    def get(self, url, params):
        result = self.requests.get(url, params=params)
        print(sys._getframe(1).f_code.co_name, result)
        self.print_tweet(result)
        return result

    def post(self, url, params):
        result = self.requests.post(url, params=params)
        print(sys._getframe(1).f_code.co_name, result)
        return result

    # --- Accounts and users ---
    # Create and manage lists

    # Follow, Search, and get users

    # Manage account setting and profile

    # Mute, block and report users

    # Subscribe to account activity

    # --- Tweets ---
    # Curate a collection of Tweets

    # Filter realtime tweets

    # Get Tweet timelines
    def GET_statuses_home_timeline(self, count=None, since_id=None, max_id=None, trim_user=None, exclude_replies=None, include_entities=None):
        url = "https://api.twitter.com/1.1/statuses/home_timeline.json?tweet_mode=extended"
        params = {"count": count,
                  "since_id": since_id,
                  "max_id": max_id,
                  "trim_user": trim_user,
                  "exclude_replies": exclude_replies,
                  "include_entities": include_entities}
        return self.get(url, params)

    def GET_statuses_mentions_timeline(self, count=None, since_id=None, max_id=None, trim_user=None, include_entities=None):
        url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json?tweet_mode=extended"
        params = {"count": count,
                  "since_id": since_id,
                  "max_id": max_id,
                  "trim_user": trim_user,
                  "include_entities": include_entities}
        return self.get(url, params)

    def GET_statuses_user_timeline(self, user_id=None, screen_name=None, since_id=None, count=None, max_id=None, trim_user=None, exclude_replies=None, include_rts=None):
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json?tweet_mode=extended"
        params = {"user_id": user_id,
                  "screen_name": screen_name,
                  "since_id": since_id,
                  "count": count,
                  "max_id": max_id,
                  "trim_user": trim_user,
                  "exclude_replies": exclude_replies,
                  "include_rts": include_rts}
        return self.get(url, params)

    # Post, retrieve and engage with Tweets
    def GET_favorites_list(self, user_id=None, screen_name=None, count=None, since_id=None, max_id=None, include_entities=None):
        url = "https://api.twitter.com/1.1/favorites/list.json?tweet_mode=extended"
        params = {"user_id": user_id,
                  "screen_name": screen_name,
                  "count": count,
                  "since_id": since_id,
                  "max_id": max_id,
                  "include_entities": include_entities}
        return self.get(url, params)

    def GET_statuses_lookup(self, id=[], include_entities=None, trim_user=None, map=None, include_ext_alt_text=None, include_card_uri=None):
        id = ",".join(str(s) for s in id)
        url = "https://api.twitter.com/1.1/statuses/lookup.json?tweet_mode=extended"
        params = {"id": id,
                  "include_entities": include_entities,
                  "trim_user": trim_user,
                  "map": map,
                  "include_ext_alt_text": include_ext_alt_text,
                  "include_card_uri": include_card_uri}
        return self.get(url, params)

    def GET_statuses_oembed(self):
        url = ""
        params = {}
        return self.get(url, params)

    def GET_statuses_retweeters_ids(self, id, count=None, cursor=None, stringify_ids=None):
        url = "https://api.twitter.com/1.1/statuses/retweeters/ids.json"
        params = {"id": id,
                  "count": count,
                  "cursor": cursor,
                  "stringify_ids": stringify_ids}
        return self.get(url, params) # IDしか返ってこない

    def GET_statuses_retweets(self):
        url = ""
        params = {}
        return self.get(url, params)

    def GET_statuses_show(self):
        url = ""
        params = {}
        return self.get(url, params)

    def POST_favorites_create(self, id, include_entities=None):
        url = "https://api.twitter.com/1.1/favorites/create.json"
        params = {"id": id,
                  "include_entities": include_entities}
        return self.post(url, params)

    def POST_favorites_destroy(self, id, include_entities=None):
        url = "https://api.twitter.com/1.1/favorites/destroy.json"
        params = {"id": id,
                  "include_entities": include_entities}
        return self.post(url, params)

    def POST_statuses_destroy(self, id, trim_user=None):
        url = f"https://api.twitter.com/1.1/statuses/destroy/{id}.json"
        params = {"id": id,
                  "trim_user": trim_user}
        return self.post(url, params)

    def POST_statuses_retweet(self, id, trim_user=None):
        url = f"https://api.twitter.com/1.1/statuses/retweet/{id}.json"
        params = {"id": id,
                  "trim_user": trim_user}
        return self.post(url, params)

    def POST_statuses_unretweet(self, id, trim_user=None):
        url = f"https://api.twitter.com/1.1/statuses/unretweet/{id}.json"
        params = {"id": id,
                  "trim_user": trim_user}
        return self.post(url, params)

    def POST_statuses_update(self, status, in_relpy_to_status_id=None, auto_populate_reply_metadata=None, exclude_reply_user_ids=None, attachment_url=None, media_ids=None, possibly_sensitive=None, lat=None, long=None, place_id=None, display_coordinates=None, trim_user=None, enable_dmcommands=None, fail_dmcommands=None, card_uri=None):
        url = "https://api.twitter.com/1.1/statuses/update.json"
        params = {"status": status,
                  "in_relpy_to_status_id": in_relpy_to_status_id,
                  "auto_populate_reply_metadata": auto_populate_reply_metadata,
                  "exclude_reply_user_ids": exclude_reply_user_ids,
                  "attachment_url": attachment_url,
                  "media_ids": media_ids,
                  "possibly_sensitive": possibly_sensitive,
                  "lat": lat,
                  "long": long,
                  "place_id": place_id,
                  "display_coordinates": display_coordinates,
                  "trim_user": trim_user,
                  "enable_dmcommands": enable_dmcommands,
                  "fail_dmcommands": fail_dmcommands,
                  "card_uri": card_uri}
        return self.post(url, params)

    # Sample realtime tweets

    # Search Tweets
    def GET_search_tweets(self, search_word, geocode=None, lang=None, locale=None, result_type=None, count=None, until=None, since_id=None, max_id=None, include_entities=None):
        url = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"
        params = {"q": search_word,
                  "geocode": geocode,
                  "lang": lang,
                  "locale": locale,
                  "result_type": result_type,
                  "count": count,
                  "until": until,
                  "since_id": since_id,
                  "max_id": max_id,
                  "include_entities": include_entities}
        return self.get(url, params)
