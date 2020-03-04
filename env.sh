#!/bin/sh
export TESSDATA_PREFIX=$HOME/tools/tesseract/tesseract/tessdata/

#Mount windows data partirion
sudo ntfs-3g /dev/sdb2 /mnt/win
if [ $? != 0 ]; then
    sudo umount /mnt/win
    sudo ntfsfix /dev/sdb2
    sudo ntfs-3g /dev/sdb2 /mnt/win
fi

