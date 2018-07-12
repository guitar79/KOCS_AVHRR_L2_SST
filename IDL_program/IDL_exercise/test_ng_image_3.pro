PRO test_ng_image_3

fig_sav = 0

file = 'data/bw0406.jpg'
READ_JPEG, file, img
sz = SIZE(img, /DIM)
win1 = WINDOW(DIMENSIONS=sz, /NO_TOOLBAR)
im = IMAGE(img, MARGIN=0, /CURRENT)
IF fig_sav THEN win1.Save, 'figures/ng_image_3A.png', WIDTH=sz[0]

xp1 = 401 & xp2 = 410
yp1 = 341 & yp2 = 350
xps = [xp1, xp2, xp2, xp1]
yps = [yp1, yp1, yp2, yp2]
plg = POLYGON(xps, yps, FILL_BACKGROUND=0, COLOR='red', /DATA)
IF fig_sav THEN win1.Save, 'figures/ng_image_3B.png', WIDTH=sz[0]

img_sub = img[xp1:xp2, yp1:yp2]
win2 = WINDOW(DIMENSIONS=[400, 400], /NO_TOOLBAR)
im_sub = IMAGE(img_sub, MARGIN=0, /CURRENT)
IF fig_sav THEN win2.Save, 'figures/ng_image_3C.png', WIDTH=400

;im_sub.INTERPOLATE = 1
;IF fig_sav THEN win2.Save, 'figures/ng_image_3D.png', WIDTH=400

END