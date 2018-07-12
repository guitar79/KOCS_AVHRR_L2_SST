PRO test_ng_ellipse

fig_sav = 0

win = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
pl = PLOT(/TEST, /NODATA, XRANGE=[0, 100], YRANGE=[0, 100], $
  FONT_SIZE=12, /CURRENT)
ep = ELLIPSE(50, 50, MAJOR=50, MINOR=50, $
  COLOR='crimson', THICK=2, CLIP=0, /DATA)
IF fig_sav THEN win.Save, 'figures/ng_ellipse.png', WIDTH=600

END