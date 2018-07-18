PRO test_ng_buffer

win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR, BUFFER=0)
x = FINDGEN(361)
y = SIN(x*!DTOR)
pl = PLOT(x, y, XRANGE=[0, 360], XTICKINTERVAL=90, $
  COLOR='magenta', THICK=2, MARGIN=0.1, FONT_SIZE=12, /CURRENT)

win.Save, 'figures/ng_buffer.png', WIDTH=600

END