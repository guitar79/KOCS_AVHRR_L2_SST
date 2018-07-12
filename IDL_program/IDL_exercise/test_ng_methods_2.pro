PRO test_ng_methods_2

win = WINDOW(DIMENSIONS=[600, 500])
x = FINDGEN(361)
y = SIN(x*!DTOR)
pl = PLOT(x, y, XRANGE=[0, 360], YRANGE=[-1, 1], XTICKINTERVAL=90, $
  COLOR='crimson', THICK=2, /CURRENT)

;ynew = SIN(x*!DTOR)*0.5
;pl.SetData, x, ynew

;amps = [1.0:-1.0:-0.1]
;FOR j = 0, N_ELEMENTS(amps)-1 DO BEGIN
;  ynew = SIN(x*!DTOR)*amps[j]
;  pl.SetData, x, ynew
;  WAIT, 0.1
;ENDFOR

;pl.GetData, xnew, ynew
;PRINT, ynew

END