PRO My_image_2

file = 'data/bw0406.jpg'
READ_JPEG, file, img
help, img
print, MIN(img), MAX(img)

sz = SIZE(img, /DIM)
PRINT, sz

win = WINDOW(DIMENSIONS=sz)
im = IMAGE(img, RGB_TABLE=34, MARGIN=0, /CURRENT)

img_sub = img[401:410, 341:350]
win_sub = WINDOW(DIMENSIONS=[600,600], /NO_TOOLBAR)
im_sub =  IMAGE(img_sub, margin=0, /CURRENT)
im_sub.INTERPOLATE = 1

END