from bot import Twitter

twitter = Twitter()

if __name__ == "__main__":
    # 【ここにコードを書く】

    # --- ツイートする ---
    # twitter.statuses_update("ツイートの内容")

    # --- タイムラインを取得 ---
    # twitter.statuses_home_timeline(ツイートの取得数(1~100))

    # --- ツイートの削除 ---
    # twitter.statuses_destroy("ツイートID")

    # --- 他のユーザのタイムラインを取得 ---
    # twitter.statuses_user_timeline("@を除いた名前", ツイートの取得数(1~100))

    # --- ツイートを検索 ---
    # twitter.search_tweets("検索キーワード", ツイートの取得数(1~100))

    print("finished!")
