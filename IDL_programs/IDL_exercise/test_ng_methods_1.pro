PRO test_ng_methods_1

;win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
win = WINDOW(DIMENSIONS=[600, 500])
x = FINDGEN(361)
y = SIN(x*!DTOR)
pl = PLOT(x, y, XRANGE=[0, 360], XMAJOR=5, COLOR='blue', $
  THICK=2, /CURRENT)
wait, 1

pl.Delete
wait, 1

y = COS(x*!DTOR)
wait, 1

plo = PLOT(x, y, COLOR='red', THICK=2, /OVERPLOT)
wait, 1

plo.Erase
wait, 1

pl = PLOT(x, y, XRANGE=[0, 360], XMAJOR=5, COLOR='blue', $
  THICK=2, /CURRENT)
wait, 1

pl.Close

END