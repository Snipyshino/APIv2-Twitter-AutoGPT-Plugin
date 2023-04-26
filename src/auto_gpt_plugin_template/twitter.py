"""This module contains functions for interacting with the Twitter API."""
from __future__ import annotations
from . import AutoGPTTwitter
import pandas as pd
import tweepy

plugin = AutoGPTTwitter()


def post_tweet(tweet_text: str) -> str:
    """Posts a tweet to twitter.

    Args:
        tweet_text (str): The tweet to post.

    Returns:
        str: The tweet that was posted.
    """

    _tweetID = plugin.api.create_tweet(text=tweet_text, user_auth=True)

    return f"Success! Tweet: {_tweetID.data.text}"


def post_reply(tweet_text: str, id: int) -> str:
    """Posts a reply to a tweet.

    Args:
        tweet_text (str): The tweet to post.
        id (int): The ID of the tweet to reply to.

    Returns:
        str: The tweet that was posted.
    """

    replyID = plugin.api.create_tweet(
        text=tweet_text,
        in_reply_to_tweet_id=id,
        user_auth=True,
    )

    return f"Success! Tweet: {replyID.data.text}"


# def get_mentions() -> str | None:
#     """Gets the most recent mention.

#     Args:
#         api (tweepy.API): The tweepy API object.

#     Returns:
#         str | None: The most recent mention.
#     """
#     columns = ["created_at", "author_id", "id", "text"]

#     userResponse = plugin.api.get_user(
#         username=target_user,
#         user_auth=True,
#     )

#     print("Twitter User Object: ", userResponse)

#     _tweets = plugin.api.get_users_mentions()

#     for tweet in _tweets:
#         return (
#             f"@{tweet.user.screen_name} Replied: {tweet.full_text}"
#             f" Tweet ID: {tweet.id}"
#         )  # Returns most recent mention

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
        id=userResponse.data.id, max_results=number_of_tweets, user_auth=True
    )

    data = []

    for tweet in tweetsResponse.data:
        data.append([tweet.created_at, tweet.author_id, tweet.id, tweet.text])

    df = str(pd.DataFrame(data, columns=columns))

    print(df)

    return df  # Prints a dataframe object containing the Time, User, ID, and Tweet
