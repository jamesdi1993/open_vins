#!/usr/bin/env python
from vio_manager import GTVIOManager
from ros_visualizer import ROSVisualizer

import argparse
import os.path
import sys

def publish_trajectory(path):
    print("Reading from path: %s" % path)
    assert os.path.exists(path), "The file does not exists: %s" % path

    vio_manager = GTVIOManager(path)
    visualizer = ROSVisualizer(vio_manager)
    for i in range(10000):
        visualizer.publish_state()


def parse_path(args):
    root = args.root
    file_name = args.file_name
    dataset = args.dataset
    path = os.path.join(root, dataset, file_name)
    return path

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description='Publish groundtruth trajectory from a txt/csv file')
    parser.add_argument('-d', '--dataset', help='data set', choices=['uzh_fpv', 'euroc_mav'], required=False)
    parser.add_argument('-f', '--file_name', help='file name', required=False)
    parser.add_argument('-r', '--root', help='root of datasets', default='/home/jamesdi1993/workspace/catkin_ws_ov/src/open_vins/ov_data')

    args, _ = parser.parse_known_args(sys.argv[1:])
    print(args)
    path = parse_path(args)
    publish_trajectory(path)