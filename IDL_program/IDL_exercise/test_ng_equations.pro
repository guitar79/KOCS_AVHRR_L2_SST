PRO test_ng_equations

fig_sav = 0

win1 = WINDOW(DIMENSIONS=[600, 500])
;x = [0:100:1.0]
;y = SQRT(x)
;pl = PLOT(x, y, THICK=2, /CURRENT)
pl = PLOT('SQRT(x)', XRANGE=[0, 100], THICK=2, /CURRENT)

;win2 = WINDOW(DIMENSIONS=[600, 500])
;sf = SURFACE('x^2+y^2', XRANGE=[-20, 20], YRANGE=[-20, 20], /CURRENT)

;sf.EQUATION = '1./(x^2+y^2)'

END