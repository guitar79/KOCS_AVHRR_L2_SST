PRO my_ng_cocobar1

data = HANNING(600,600)*100 + 100 
PRINT, MIN(data), MAX(data), MEAN(data)
win = WINDOW(DIMENSION=[600,700], /NO_TOOLBAR)
im = IMAGE(data, RGB_TABLE=67, MARGIN=[0.1,0.2,0.1,0.1], /CURRENT)
cb = COLORBAR(TARGET=im, POSITiON=[0.2, 0.10, 0.8, 0.14], $
  TITLE='Value', FONT_SIZE=11, /BORDER, ORIENTATION=1)

END