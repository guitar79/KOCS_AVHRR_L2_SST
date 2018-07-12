PRO test_ng_plot3d_1

fig_sav = 0

n = 10
x = RANDOMU(seed, n)*10
y = RANDOMU(seed, n)*10
z = RANDOMU(seed, n)*10

win1 = WINDOW(DIMENSIONS=[600, 500])
pl1 = PLOT3D(x, y, z, LINESTYLE='none', CLIP=0, AXIS_STYLE=2, $
  SYMBOL='circle', SYM_COLOR='crimson', SYM_SIZE=2, /SYM_FILLED, /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_plot3d_1A.png', WIDTH=600

win2 = WINDOW(DIMENSIONS=[600, 500])
pl2 = PLOT3D(x, y, z, LINESTYLE='none', CLIP=0, AXIS_STYLE=2, $
  SYM_OBJECT=ORB(), SYM_COLOR='crimson', SYM_SIZE=2, /CURRENT)
IF fig_sav THEN win2.Save, 'figures/ng_plot3d_1B.png', WIDTH=600

END