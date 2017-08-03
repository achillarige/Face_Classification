from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append("..")

import align.align_dataset_mtcnn as align 
import align_dataset_userprofs as align_users

unaligned_data = 'datasets/face_data_unaligned/'
aligned_data = 'datasets/face_data_aligned/'

unaligned_test = 'datasets/unsorted_unaligned'
aligned_test = 'datasets/unsorted_aligned'

def align_faces(input_dir, output_dir):
    class Arguments:
        def __init__(self):
            self.input_dir = input_dir
            self.output_dir = output_dir
            self.image_size = 182
            self.margin = 44
            self.random_order = 'store_true'
            self.gpu_memory_fraction = 1.0
    align.main(Arguments())

def align_profs(input_dir, output_dir):
    class Arguments:
        def __init__(self):
            self.input_dir = input_dir
            self.output_dir = output_dir
            self.image_size = 182
            self.margin = 44
            self.random_order = 'store_true'
            self.gpu_memory_fraction = 1.0
    align_users.main(Arguments())


