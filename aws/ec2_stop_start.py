"""
Stop and Start Amazon EC2 Instances
"""


import sys
import boto3


filter_items = {
    "type": {"Name": "instance-type", "Values": ["t2.micro"]},
    "tag": {"Name": "tag:Env", "Values": ["Dev"]},
    "state": {"Name": "instance-state-name", "Values": ["running", "stopped"]},
}

filters = [filter_items["type"], filter_items["tag"], filter_items["state"]]


def get_aws_regions():
    """
    returns list of all AWS regions
    """

    ec2 = boto3.resource("ec2")

    regions = ec2.meta.client.describe_regions().get("Regions")
    region_names = [region.get("RegionName") for region in regions]

    return region_names


def start_stop_instances(action: str):
    """
    stop and start instances
    """

    regions = get_aws_regions()

    for region in regions:
        print("Region: ", region)

        ec2 = boto3.resource("ec2", region_name=region)

        instances = ec2.instances.filter(Filters=filters)

        if len(list(instances)) > 0:
            for instance in instances:
                if action == "stop":
                    instance.stop()

                if action == "start":
                    instance.start()

                print(f"{action} instance {instance.id}: Done")
        else:
            print("No instances found")


def run():
    """
    run script
    """

    action = input("Enter Action:")

    if action not in ["start", "stop"]:
        print("Invalid action")
        sys.exit()
    else:
        start_stop_instances(action)


if __name__ == "__main__":
    run()
