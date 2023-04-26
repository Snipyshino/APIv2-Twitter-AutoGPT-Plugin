"""This module contains functions for interacting with the Twitter API."""
from __future__ import annotations
from . import AutoGPTTwitter
import pandas as pd
import tweepy

plugin = AutoGPTTwitter()


def post_tweet(tweet_text: str) -> str:
    """Posts a tweet to twitter.

    Args:
        tweet (str): The tweet to post.

    Returns:
        str: The tweet that was posted.
    """

    _tweetID = plugin.api.create_tweet(text=tweet_text, user_auth=True)

    return f"Success! Tweet: {_tweetID.text}"


def post_reply(tweet_text: str, tweet_id: int) -> str:
    """Posts a reply to a tweet.

    Args:
        tweet (str): The tweet to post.
        tweet_id (int): The ID of the tweet to reply to.

    Returns:
        str: The tweet that was posted.
    """

    replyID = plugin.api.create_tweet(
        text=tweet_text,
        in_reply_to_tweet_id=tweet_id,
        user_auth=True,
    )

    return f"Success! Tweet: {replyID.text}"


def search_twitter_user(target_user: str, number_of_tweets: int) -> str:
    """Searches a user's tweets given a number of items to retrieve and
      returns a dataframe.

    Args:
        target_user (str): The user to search.
        num_of_items (int): The number of items to retrieve.
        api (tweepy.API): The tweepy API object.

    Returns:
        str: The dataframe containing the tweets.
    """
    columns = ["created_at", "author_id", "id", "text"]

    userResponse = plugin.api.get_user(
        username=target_user,
        user_auth=True,
    )

    print("Twitter User Object: ", userResponse)

    tweetsResponse = plugin.api.get_users_tweets(
        id=userResponse.data.id, max_results=number_of_tweets
    )

    data = []

    for tweet in tweetsResponse.data:
        data.append([tweet.created_at, tweet.author_id, tweet.id, tweet.text])

    df = str(pd.DataFrame(data, columns=columns))

    print(df)

    return df  # Prints a dataframe object containing the Time, User, ID, and Tweet
