#!/bin/sh
lstmeval --model /mnt/win/TU_Projects/KZ/output/red_october_checkpoint \
  --traineddata ~/tools/tesseract/tesseract/tessdata/bul.traineddata \
  --eval_listfile ~/tu/KZ/train_data/bul.training_files.txt
