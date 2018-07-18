PRO test_ng_poly_1

fig_sav = 0

vx = [0.2, 0.8, 0.8, 0.2]
vy = [0.2, 0.2, 0.8, 0.8]

win1 = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
plg = POLYGON(vx, vy, THICK=3, COLOR='blue', /NORMAL)

IF fig_sav THEN win1.Save, 'figures/ng_polygon_1A.png', WIDTH=600

plg.COLOR = 'crimson'
plg.FILL_COLOR = 'yellow'

IF fig_sav THEN win1.Save, 'figures/ng_polygon_1B.png', WIDTH=600

vx = [0.2, 0.8, 0.8, 0.2, 0.2]
vy = [0.2, 0.2, 0.8, 0.8, 0.2]

win2 = WINDOW(DIMENSIONS=[600, 600], /NO_TOOLBAR)
pll = POLYLINE(vx, vy, THICK=3, COLOR='blue', /NORMAL)

IF fig_sav THEN win2.Save, 'figures/ng_polyline_1B.eps', WIDTH=600

END