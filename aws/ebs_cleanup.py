"""
Cleanup unused EBS volume
"""


import boto3


ec2 = boto3.resource("ec2")

status = {"Name": "status", "Values": ["available"]}


def get_available_volume_ids():
    """
    returns list of all available volumes
    """

    volumes = [volume.id for volume in ec2.volumes.filter(Filters=[status])]

    return volumes


def clean_up_volumes():
    """
    deletes all unused EBS volumes
    """

    volume_ids = get_available_volume_ids()

    for volume_id in volume_ids:
        volume = ec2.Volume(volume_id)

        volume.delete()
        print(f"Cleanup EBS Volume: {volume_id}")


if __name__ == "__main__":
    clean_up_volumes()
