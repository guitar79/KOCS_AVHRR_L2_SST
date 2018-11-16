PRO my_first_plot

  x = FINDGEN(101)*0.1
  y=SQRT(x)

  win = WINDOW(DIMENSIONS=[1000, 800], /NO_TOOLBAR)
  p= PLOT(x, y, /CURRENT, color="red", THICK = 3)


END