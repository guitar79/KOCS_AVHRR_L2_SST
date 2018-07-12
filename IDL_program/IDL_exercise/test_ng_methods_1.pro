PRO test_ng_methods_1

win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
x = FINDGEN(361)
y = SIN(x*!DTOR)
pl = PLOT(x, y, XRANGE=[0, 360], XMAJOR=5, COLOR='blue', $
  THICK=2, /CURRENT)

;pl.Delete
;
;y = COS(x*!DTOR)
;plo = PLOT(x, y, COLOR='red', THICK=2, /OVERPLOT)
;
;plo.Erase
;
;pl = PLOT(x, y, XRANGE=[0, 360], XMAJOR=5, COLOR='blue', $
;  THICK=2, /CURRENT)
;
;pl.Close

END