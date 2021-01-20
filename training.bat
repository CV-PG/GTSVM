
gtsvm_initialize -f "./features/final.train" -o "./features/data_video.mdl" -C 2 -k gaussian -1 0.115625
gtsvm_optimize -i "./data_video.mdl" -o "./features/data_video.mdl" -e 0.01 -n 1000000
gtsvm_shrink -i "./features/data_video.mdl" -o "G./features/data_video_shrunk.mdl"
gtsvm_classify -f "./features/final_test.train" -i "./features/data_video_shrunk.mdl" -o "./features/result.txt"
