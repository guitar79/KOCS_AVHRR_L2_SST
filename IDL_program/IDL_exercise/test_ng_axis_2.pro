PRO test_ng_axis_2

fig_sav = 0
cn = 1

x = FINDGEN(101)/10
y1 = SQRT(x)
y2 = x^2

win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)

IF cn EQ 1 THEN BEGIN
  pl1 = PLOT(x, y1, YRANGE=[0, 5], YTITLE='Y1', XTITLE='X', $
    THICK=2, MARGIN=0.1, FONT_SIZE=12, /CURRENT)
ENDIF

IF cn EQ 2 THEN BEGIN
  pl1 = PLOT(x, y1, COLOR='blue', YRANGE=[0, 5], AXIS_STYLE=1, $
    YCOLOR='blue', YTITLE='Y1', XTITLE='X', THICK=2, MARGIN=0.1, $
    FONT_SIZE=12, /CURRENT)
  pl2 = PLOT(x, y2, COLOR='crimson', /OVERPLOT)
ENDIF

IF cn EQ 3 THEN BEGIN
  pl1 = PLOT(x, y1, COLOR='blue', YRANGE=[0, 5], AXIS_STYLE=1, $
    YCOLOR='blue', YTITLE='Y1', XTITLE='X', THICK=2, MARGIN=0.12, $
    FONT_SIZE=12, /CURRENT)
  pl2 = PLOT(x, y2, COLOR='crimson', YRANGE=[0, 100], AXIS_STYLE=4, $
    THICK=2, MARGIN=0.12, FONT_SIZE=12, /CURRENT)
  yaxis = AXIS('y', LOCATION=10, TICKDIR=1, TEXTPOS=1, TARGET=pl2, $
    COLOR='crimson', TITLE='Y2', TICKFONT_SIZE=12)
ENDIF

IF fig_sav THEN win.Save, 'figures/ng_axis_2.png', WIDTH=600

END