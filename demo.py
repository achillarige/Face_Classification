import face_alignment as align
import train_data as trainer
import test_data as tester

#aligning dataset and unsorted directory
unaligned_data = 'datasets/face_data_unaligned/'
aligned_data = 'datasets/face_data_aligned/'

unaligned_test = 'datasets/unsorted_unaligned'
aligned_test = 'datasets/unsorted_aligned'

align.align_profs(unaligned_data, aligned_data)
align.align_faces(unaligned_test, aligned_test)

trainer.train()
tester.test()





