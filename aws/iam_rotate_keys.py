"""
Rotate IAM Keys
"""


from datetime import datetime, timezone
import boto3


MAX_KEY_AGE = 90


client = boto3.client("iam")


def calculate_key_age(create_date):
    """
    calculates key age
    """
    today = datetime.now(timezone.utc)

    age = today - create_date

    return age.days


def get_iam_usernames():
    """
    returns list of all IAM users
    """

    paginator = client.get_paginator("list_users")

    usernames = []

    for response in paginator.paginate():
        usernames += [users.get("UserName") for users in response.get("Users")]

    return usernames


def get_access_keys():
    """
    returns list of access keys for IAM users
    """

    usernames = get_iam_usernames()

    access_keys = []

    for username in usernames:
        user_access_keys = client.list_access_keys(UserName=username)

        access_keys += list(user_access_keys.get("AccessKeyMetadata"))

    return access_keys


def deactivate_access_keys():
    """
    deactivates access keys older than MAX_KEY_AGE
    """

    access_keys = get_access_keys()

    for access_key in access_keys:
        username = access_key["UserName"]
        key_id = access_key["AccessKeyId"]
        create_date = access_key["CreateDate"]

        key_age = calculate_key_age(create_date)

        if key_age > MAX_KEY_AGE:
            print(f"Deactivating key for {username}")

            client.update_access_key(
                UserName=username, AccessKeyId=key_id, Status="Inactive"
            )


if __name__ == "__main__":
    deactivate_access_keys()
