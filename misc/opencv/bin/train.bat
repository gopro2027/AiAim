:: del cascade
:: mkdir cascade
opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 260 -numNeg 1400 -numStages 24 -w 20 -h 20 -precalcValBufSize 2192 -precalcIdxBufSize 2192
PAUSE