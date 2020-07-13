import argparse
import os.path
import sys

def publish_trajectory(path):
    print("Reading from path: %s" % path)
    assert os.path.exists(path), "The file does not exists: %s" % path

def parse_path(args):
    root = args.root
    file_name = args.file_name
    dataset = args.dataset
    path = os.path.join(root, dataset, file_name)
    return path

if __name__=="__main__":
    print("Script is started.")
    parser = argparse.ArgumentParser(
        description='Publish groundtruth trajectory from a txt/csv file')
    parser.add_argument('-d', '--dataset', help='data set', choices=['uzh_fpv', 'euroc_mav'], required=True)
    parser.add_argument('-f', '--file_name', help='file name', required=True)
    parser.add_argument('-r', '--root', help='root of datasets', default='/home/jamesdi1993/workspace/catkin_ws_ov/src/open_vins/ov_data')

    args = parser.parse_args(sys.argv[3:])
    path = parse_path(args)
    publish_trajectory(path)