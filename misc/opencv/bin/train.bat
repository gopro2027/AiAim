:: del cascade
:: mkdir cascade
opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 140 -numNeg 500 -numStages 22 -w 20 -h 20 -precalcValBufSize 8192 -precalcIdxBufSize 8192
PAUSE