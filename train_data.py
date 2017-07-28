from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append("..")

import classifier

def train():
    class Arguments:
        def __init__(self):
            self.mode = "TRAIN"
            self.data_dir = "datasets/face_data_aligned"
            self.model = "20170512-110547.pb"
            self.classifier_filename = "face_classifier.pkl"
            self.seed = 666
            self.use_split_dataset = 'store_true'
            self.min_nrof_images_per_class = 1
            self.nrof_train_images_per_class = 1
            self.batch_size = 90
            self.image_size = 160

    classifier.main(Arguments())