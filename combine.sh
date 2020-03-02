#/bin/bash

lstmtraining --stop_training \
    --continue_from /mnt/win/TU_Projects/KZ/output/red_october_checkpoint \
    --traineddata ~/tools/tesseract/tesseract/tessdata/bul.traineddata \
    --model_output output/bul.traineddata
