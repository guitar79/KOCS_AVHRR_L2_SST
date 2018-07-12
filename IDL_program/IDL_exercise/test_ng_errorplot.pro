PRO test_ng_errorplot

fig_sav = 0

x = [2, 3, 5, 7, 8]
y = [8.5, 11.2, 9.3, 8.1, 12.6]
yerr = [2.4, 1.8, 2.7, 2.2, 1.9]
xerr = [1.0, 0.9, 1.5, 1.2, 0.8]

win1 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
epl1 = ERRORPLOT(x, y, yerr, XRANGE=[0, 10], YRANGE=[0, 20], $
  LINESTYLE=2, ERRORBAR_THICK=2, ERRORBAR_COLOR='green', ERRORBAR_CAPSIZE=0.4, $
  SYMBOL='circle', SYM_COLOR='crimson', /SYM_FILLED, SYM_SIZE=1.2, $
  TITLE='ERRORPLOT (Y)', FONT_SIZE=12, MARGIN=0.1, /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_errorplot_1.png', WIDTH=800

win2 = WINDOW(DIMENSIONS=[800, 600], /NO_TOOLBAR)
epl2 = ERRORPLOT(x, y, xerr, yerr, XRANGE=[0, 10], YRANGE=[0, 20], $
  LINESTYLE=2, ERRORBAR_THICK=2, ERRORBAR_COLOR='green', ERRORBAR_CAPSIZE=0.4, $
  SYMBOL='circle', SYM_COLOR='crimson', /SYM_FILLED, SYM_SIZE=1.2, $
  TITLE='ERRORPLOT (Y and X)', FONT_SIZE=12, MARGIN=0.1, /CURRENT)
IF fig_sav THEN win2.Save, 'figures/ng_errorplot_2.png', WIDTH=800

END