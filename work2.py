from bot import Twitter
from time import sleep
import random

twitter = Twitter()

with open("tweets.txt") as f:
    tweets = [tweet.strip() for tweet in f.readlines()[1:]]

if __name__ == "__main__":
    # 【ここにコードを書く】

    # --- ツイートする ---
    # twitter.statuses_update("ツイートの内容")

    # --- tweets.txtの内容をツイートさせる ---
    # tweetsという変数にtweets.txtの中身が入っている
    # print(tweets)

    # --- 順番にツイートさせたいなら ---
    # for tweet in tweets:
    #     twitter.statuses_update(tweet)

    # --- ランダムな順番でツイートさせたいなら ---
    # これをfor文の前に置く
    # random.shuffle(tweets)

    # --- ツイートをn秒間隔でさせたいなら ---
    # for文の中にこれを書く
    # sleep(n)

    print("finished!")
