:: del cascade
:: mkdir cascade
opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 1600 -numNeg 4000 -numStages 28 -w 20 -h 20 -precalcValBufSize 2048 -precalcIdxBufSize 4096
PAUSE