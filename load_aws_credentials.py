import os
import logging


def load_aws_credentials(credential_file):
    if not os.path.exists(credential_file):
        logging.error("load_aws_credentials: aws credential file does not exist")
        return

    with open(credential_file, "r") as f:
        lines = f.readlines()
        assert len(lines) == 2, "load_aws_credentials: aws credential file content corrupted"
        line = lines[1]
        return line.strip().split(",")

