from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append("..")

import align.align_dataset_mtcnn as align 

unaligned_data = 'datasets/face_data_unaligned/'
aligned_data = 'datasets/face_data_aligned/'

def align_faces():
    class Arguments:
        def __init__(self):
            self.input_dir = unaligned_data
            self.output_dir = aligned_data
            self.image_size = 182
            self.margin = 44
            self.random_order = 'store_true'
            self.gpu_memory_fraction = 1.0
    align.main(Arguments())
