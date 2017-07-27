from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append("..")

import classifier

args = classifier.parse_arguments(["CLASSIFY", "datasets/unsorted_aligned/",  
    "20170512-110547.pb", "face_classifier.pkl", "--train_dir=datasets/face_data_aligned/"])
classifier.main(args)