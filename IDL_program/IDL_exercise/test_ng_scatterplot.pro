PRO test_ng_scatterplot

fig_sav = 0

x = [1, 2, 5, 4, 7, 3]
y = [1, 3, 6, 7, 5, 2]
value = [13, 79, 220, 467, 784]
;x = RANDOMU(seed, 100)
;y = RANDOMU(seed, 100)
;value = RANDOMU(seed, 100)*1000

win1 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
spl1 = SCATTERPLOT(x, y, SYMBOL='circle', SYM_SIZE=1.5, /SYM_FILLED, $
  SYM_FILL_COLOR='crimson', FONT_SIZE=12, MARGIN=0.1, /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_scatterplot_1.png', WIDTH=800

win2 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
spl2 = SCATTERPLOT(x, y, SYMBOL='circle', SYM_SIZE=1.5, /SYM_FILLED, $
  MAGNITUDE=BYTSCL(value, MIN=0, MAX=1000), RGB_TABLE=34, FONT_SIZE=12, $
  MARGIN=0.1, /CURRENT)
;spl2o = SCATTERPLOT(x, y, SYMBOL='circle', SYM_SIZE=1.5, /OVERPLOT)
IF fig_sav THEN win2.Save, 'figures/ng_scatterplot_2.png', WIDTH=800

win3 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
spl3 = SCATTERPLOT(x, y, SYMBOL='circle', SYM_SIZE=1.5, /SYM_FILLED, $
  MAGNITUDE=BYTSCL(value, MIN=0, MAX=1000), RGB_TABLE=34, $
  FONT_SIZE=12, MARGIN=[0.1, 0.2, 0.1, 0.1], /CURRENT)
;spl3o = SCATTERPLOT(x, y, SYMBOL='circle', SYM_SIZE=1.5, /OVERPLOT)
clbar = COLORBAR(TARGET=spl3, TITLE='Value', RANGE=[0, 1000], $
  POSITION=[0.2, 0.07, 0.8, 0.10], /BORDER, FONT_SIZE=11)
IF fig_sav THEN win3.Save, 'figures/ng_scatterplot_3.png', WIDTH=800

END