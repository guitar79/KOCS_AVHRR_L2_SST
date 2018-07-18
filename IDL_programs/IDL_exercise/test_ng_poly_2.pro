PRO test_ng_poly_2

fig_sav = 0

x = FINDGEN(101)
y = SQRT(x)
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
pl = PLOT(x, y, THICK=2, FONT_SIZE=12, /CURRENT)

IF fig_sav THEN win.Save, 'figures/ng_polyline_2A.png', WIDTH=600

ind = 40
PRINT, x[ind], y[ind]
line1 = POLYLINE([x[ind], x[ind]], [0, y[ind]], THICK=2, $
  LINESTYLE=2, COLOR='crimson', /DATA)
line2 = POLYLINE([0, x[ind]], [y[ind], y[ind]], THICK=2, $
  LINESTYLE=2, COLOR='crimson', /DATA)
tx = TEXT(x[ind]-4, y[ind]+0.4, '(40.0, 6.3)', ALIGNMENT=0.5, $
  FONT_COLOR='crimson', FONT_SIZE=16, /DATA)

IF fig_sav THEN win.Save, 'figures/ng_polyline_2B.png', WIDTH=600

END