PRO test_ng_barplot_2

fig_sav = 0

;data = HANNING(200, 200)*30
data = RANDOMN(seed, 10000)+15.5+3*RANDOMN(seed, 10000)
PRINT, MIN(data), MAX(data)
bsz = 1

h = HISTOGRAM(data, MIN=0, MAX=30, BINSIZE=bsz, LOCATION=xloc)
win1 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
p1 = BARPLOT(xloc+bsz/2., h, FILL_COLOR='magenta', XRANGE=[0, 30], $
  XTITLE='Value', YTITLE='Count', FONT_SIZE=12, MARGIN=0.1, /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_barplot_2A.png', WIDTH=800

c = TOTAL(h, /CUMULATIVE)/N_ELEMENTS(data)
win2 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
p2 = BARPLOT(xloc+bsz/2., c, FILL_COLOR='green', XRANGE=[0, 30], $
  XTITLE='Value', YTITLE='Count Ratio', FONT_SIZE=12, MARGIN=0.1, /CURRENT)
IF fig_sav THEN win2.Save, 'figures/ng_barplot_2B.png', WIDTH=800

END