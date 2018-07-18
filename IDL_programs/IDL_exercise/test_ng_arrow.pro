PRO test_ng_arrow

fig_sav = 0

ax = [2, 7];[[2, 7], [6, 9]]
ay = [4, 9];[[4, 9], [4, 6]]
win1 = WINDOW(DIMENSIONS=[600, 600])
pl1 = PLOT(/TEST, XRANGE=[0, 10], YRANGE=[0, 10], /NODATA, /CURRENT)
arr = ARROW(ax, ay, HEAD_ANGLE=30, HEAD_INDENT=0, COLOR='blue', THICK=3, /DATA)

u= [2,   1, 1, 1, 2, 3]
v= [0,   0, 0, 1, 2, 3]
x= [0,   0, 2, 4, 5, 6]
y= [0, 0.5, 3, 8,10, 6]
ax = TRANSPOSE([[x], [x+u]])
ay = TRANSPOSE([[y], [y+v]])
win2 = WINDOW(DIMENSIONS=[600, 600])
pl2 = PLOT(/TEST, XRANGE=[0, 10], YRANGE=[0, 15], /NODATA, /CURRENT)
arr = ARROW(ax, ay, HEAD_ANGLE=30, HEAD_INDENT=0, COLOR='red', THICK=2, /DATA)

IF fig_sav THEN BEGIN
  win1.Save, 'figures/ng_arrow_1.png', WIDTH=600
  win2.Save, 'figures/ng_arrow_2.png', WIDTH=600
ENDIF

END