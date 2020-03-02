TESSERACT_SRC_HOME="/home/screamofwoods/tools/tesseract/tesseract/src/training"
TESSERACT_LSTM="/mnt/win/TU_Projects/KZ/langdata_lstm"
TESSERACT_TESSDATA="/home/screamofwoods/tools/tesseract/tesseract/tessdata"
OUT_DATA_DIR="train_data"
FONTS_DIR="fonts"

rm -rf $OUT_DATA_DIR
mkdir $OUT_DATA_DIR

#pushd $TESSERACT_SRC_HOME
#HANDWRITTEN='Azbuka03_D Medium'

tesstrain.sh \
    --fonts_dir '/home/screamofwoods/tu/KZ/fonts' \
    --fontlist 'Red October Light' \
    --exposures 0 \
    --lang bul \
    --linedata_only \
    --langdata_dir $TESSERACT_LSTM \
    --tessdata_dir $TESSERACT_TESSDATA \
    --save_box_tiff \
    --maxpages 400
    --output_dir $OUT_DATA_DIR

#popd
