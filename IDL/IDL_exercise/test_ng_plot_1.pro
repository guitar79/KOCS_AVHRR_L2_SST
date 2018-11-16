PRO test_ng_plot_1

x = FINDGEN(361)
y = SIN(x*!dtor)
win = WINDOW(DIMENSIONS=[600, 500], /NO_TOOLBAR)
p = PLOT(x, y, COLOR='blue', THICK=2, /CURRENT)

END