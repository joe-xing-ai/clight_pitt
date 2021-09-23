import logging
import optparse
import os
import sys
import re
import datetime

from aws_api import aws_api


def upload_videos_to_cloud(s3, data_path, bucket):

    video_entries = []
    for root, dirs, files in os.walk(data_path):
        for file in files:
            # Note: we only look at avi or mp4 video files
            if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".MP4") or file.endswith(".AVI"):
                file_path = os.path.join(root, file)
                cloud_key = file_path
                tuple_entry = (file_path, cloud_key)
                video_entries.append(tuple_entry)

    n_videos = len(video_entries)
    logging.info("upload_data: found %s videos files, getting ready to upload now..." % n_videos)

    for i in range(n_videos):
        tuple_entry = video_entries[i]
        file_path, cloud_key = tuple_entry

        video_object = s3.Object(bucket, cloud_key)

        logging.info("upload video %s out of total %s videos: %s to %s ... " % (i, n_videos, file_path, cloud_key))
        video_object.upload_file(file_path)

    logging.info("upload to aws s3 bucket is done!")


def main():
    """
    how to use:

    python upload_data.py --data_path your_path_to_video_files

    :return:
    """
    parser = optparse.OptionParser()
    parser.add_option('--data_path', action="store", default="./data/", help=None)
    parser.add_option('--bucket', action="store", default="clightpitt", help=None)
    parser.add_option('--credential', action='store', default='clight_pitt.csv', help=None)
    options, args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)

    s3_resource = aws_api(options.credential, "us-east-2")

    upload_videos_to_cloud(s3_resource, options.data_path, options.bucket)


if __name__ == "__main__":
    main()
