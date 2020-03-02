#!/bin/sh
rm -rf output/*
OMP_THREAD_LIMIT=8 lstmtraining \
	--continue_from bul.lstm \
	--model_output /mnt/win/TU_Projects/KZ/output/red_october \
	--traineddata ~/tools/tesseract/tesseract/tessdata/bul.traineddata \
	--train_listfile train_data/bul.training_files.txt \
	--max_iterations 3000
