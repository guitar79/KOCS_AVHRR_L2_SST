PRO test_ng_axis_1

fig_sav = 0

x = FINDGEN(361)
y = SIN(x*!DTOR)

cn = 1

CASE cn OF

1 : BEGIN
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
pl = PLOT(x, y, COLOR='crimson', THICK=3, XRANGE=[0, 360], $
  XTICKINTERVAL=90, XTITLE='Degree', YTITLE='Value', $
  TITLE='Sine Plot', FONT_SIZE=11, AXIS_STYLE=2, CLIP=0, /CURRENT)
END

2 : BEGIN
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
pl = PLOT(x, y, COLOR='crimson', THICK=3, XRANGE=[0, 360], $
  XTICKINTERVAL=90, XTITLE='Degree', YTITLE='Value', $
  TITLE='Sine Plot', FONT_SIZE=11, AXIS_STYLE=1, CLIP=0, /CURRENT)
END

3 : BEGIN
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
pl = PLOT(x, y, COLOR='crimson', THICK=3, XRANGE=[0, 360], $
  XTICKINTERVAL=90, XTITLE='Degree', YTITLE='Value', $
  TITLE='Sine Plot', FONT_SIZE=11, AXIS_STYLE=1, CLIP=0, /CURRENT)
pl.AXES[0].Location = [0, 0]
xtn = pl.XTICKNAME
xtn[0] = ''
pl.XTICKNAME = xtn
pl.XTITLE = ''
tx = TEXT(360, 0.15, 'Degree', ALIGNMENT=1, FONT_SIZE=11, /DATA)
pl.YTICKFONT_STYLE = 'bold'
pl.YTEXT_COLOR = 'dodger blue'
END

4 : BEGIN
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
pl = PLOT(x, y, COLOR='crimson', THICK=3, XRANGE=[0, 360], $
  XTICKINTERVAL=90, TITLE='Sine Plot', FONT_SIZE=11, AXIS_STYLE=3, $
  CLIP=0, /CURRENT)
END

ENDCASE

IF fig_sav THEN win.Save, 'figures/ng_axis_1.png', WIDTH=600

END