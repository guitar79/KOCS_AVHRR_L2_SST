;+
; NAME:
;       SHOW_COLORS_LIST
;       
; PURPOSE:
;       Shows all available colors for new function graphics in GUI
;       (works only on 8.0 or later version)
;       
; CALLING SEQUENCE:
;       SHOW_COLORS_LIST
;       
; INPUTS:
;       None.
;
; OUTPUT:
;       None. (Just a GUI appears)
;
; METHOD:
;       Click left mouse button on any color box to see the corresponding color name
;       and RGB triple.
;       
; PROCEDURES CALLED:
;       None.
;       
; REVISION HISTORY:
;       Written by Sangwoo Lee         September, 2011
;       (Created on IDL V8.1)
;       Modified to preserved the current DECOMPOSED setting         September, 2011
;       Modified to adjust GUI size according to OS and screen resolution         July, 2015
;       Added RETAIN=2 keyword to WIDGET_DRAW for non-Windows OS         July, 2015
;       Modified not to use TO_HEX routine which requires IDL astro library         July, 2015
;-

PRO SHOW_COLORS_LIST_EVENT, event

WIDGET_CONTROL, event.TOP, GET_UVALUE=info

IF event.RELEASE EQ 1 THEN BEGIN
  uname = WIDGET_INFO(event.ID, /UNAME)
  index = FIX(STRMID(uname, 5, 3))
  ;PRINT, info.cc.(index)
  WIDGET_CONTROL, info.cname_show, SET_VALUE=info.cnames[index]
  rgb = FIX(info.cc.(index))
  rgb_text = '[' + STRTRIM(STRING(rgb[0]), 2) + ', ' + STRTRIM(STRING(rgb[1]), 2) + ', ' + STRTRIM(STRING(rgb[2]), 2) + ']'
  WIDGET_CONTROL, info.rgb_show, SET_VALUE=rgb_text
ENDIF

END

PRO SHOW_COLORS_LIST_EXIT, id

WIDGET_CONTROL, id, GET_UVALUE=info
DEVICE, DECOMPOSED = info.dcp

END

PRO SHOW_COLORS_LIST

cc = !color
cnames = TAG_NAMES(cc)
DEVICE, GET_DECOMPOSED = dcp
DEVICE, DECOMPOSED = 1
oMonInfo = OBJ_NEW('IDLsysMonitorInfo')
mon_rects = oMonInfo -> GetRectangles(EXCLUDE_TASKBAR=1)
scrsz = mon_rects[2:3]
OBJ_DESTROY, oMonInfo
;DEVICE, GET_SCREEN_SIZE = scrsz

CASE !version.os_family OF
  'Windows' : BEGIN
    txsz = 1220
    tysz = 1000
    lysz = 18
    sc_incr = 0
  END
  ELSE : BEGIN
    txsz = 780
    tysz = 805
    lysz = 10
    sc_incr = 70
  END
ENDCASE
sxsz = txsz < scrsz[0]
sysz = tysz < (scrsz[1]-sc_incr)
IF txsz GT scrsz[0] OR tysz GT scrsz[1] THEN scr = 1 ELSE scr = 0

tlb = WIDGET_BASE(XSIZE=txsz, YSIZE=tysz, SCROLL=scr, SCR_XSIZE=sxsz, SCR_YSIZE=sysz, $
  /COLUMN, TITLE='List of Color Names in Function Graphics')
wbase = WIDGET_BASE(tlb, /ALIGN_CENTER, /ROW)

base1 = WIDGET_BASE(wbase, /COLUMN)
FOR i = 0, 20 DO BEGIN
  wlabel = WIDGET_LABEL(base1, VALUE=cnames[i], YSIZE=lysz, /ALIGN_CENTER)
  str = STRING(i, FORMAT='(I3.3)')
  draw = WIDGET_DRAW(base1, XSIZE=80, YSIZE=20, RETAIN=2, UNAME='draw_'+str, /ALIGN_CENTER, /BUTTON_EVENTS)
ENDFOR

base2 = WIDGET_BASE(wbase, /COLUMN)
FOR i = 21, 41 DO BEGIN
  wlabel = WIDGET_LABEL(base2, VALUE=cnames[i], YSIZE=lysz, /ALIGN_CENTER)
  str = STRING(i, FORMAT='(I3.3)')
  draw = WIDGET_DRAW(base2, XSIZE=80, YSIZE=20, RETAIN=2, UNAME='draw_'+str, /ALIGN_CENTER, /BUTTON_EVENTS)
ENDFOR

base3 = WIDGET_BASE(wbase, /COLUMN)
FOR i = 42, 62 DO BEGIN
  wlabel = WIDGET_LABEL(base3, VALUE=cnames[i], YSIZE=lysz, /ALIGN_CENTER)
  str = STRING(i, FORMAT='(I3.3)')
  draw = WIDGET_DRAW(base3, XSIZE=80, YSIZE=20, RETAIN=2, UNAME='draw_'+str, /ALIGN_CENTER, /BUTTON_EVENTS)
ENDFOR

base4 = WIDGET_BASE(wbase, /COLUMN)
FOR i = 63, 83 DO BEGIN
  wlabel = WIDGET_LABEL(base4, VALUE=cnames[i], YSIZE=lysz, /ALIGN_CENTER)
  str = STRING(i, FORMAT='(I3.3)')
  draw = WIDGET_DRAW(base4, XSIZE=80, YSIZE=20, RETAIN=2, UNAME='draw_'+str, /ALIGN_CENTER, /BUTTON_EVENTS)
ENDFOR

base5 = WIDGET_BASE(wbase, /COLUMN)
FOR i = 84, 104 DO BEGIN
  wlabel = WIDGET_LABEL(base5, VALUE=cnames[i], YSIZE=lysz, /ALIGN_CENTER)
  str = STRING(i, FORMAT='(I3.3)')
  draw = WIDGET_DRAW(base5, XSIZE=80, YSIZE=20, RETAIN=2, UNAME='draw_'+str, /ALIGN_CENTER, /BUTTON_EVENTS)
ENDFOR

base6 = WIDGET_BASE(wbase, /COLUMN)
FOR i = 105, 125 DO BEGIN
  wlabel = WIDGET_LABEL(base6, VALUE=cnames[i], YSIZE=lysz, /ALIGN_CENTER)
  str = STRING(i, FORMAT='(I3.3)')
  draw = WIDGET_DRAW(base6, XSIZE=80, YSIZE=20, RETAIN=2, UNAME='draw_'+str, /ALIGN_CENTER, /BUTTON_EVENTS)
ENDFOR

base7 = WIDGET_BASE(wbase, /COLUMN)
FOR i = 126, 146 DO BEGIN
  wlabel = WIDGET_LABEL(base7, VALUE=cnames[i], YSIZE=lysz, /ALIGN_CENTER)
  str = STRING(i, FORMAT='(I3.3)')
  draw = WIDGET_DRAW(base7, XSIZE=80, YSIZE=20, RETAIN=2, UNAME='draw_'+str, /ALIGN_CENTER, /BUTTON_EVENTS)
ENDFOR

wbase2 = WIDGET_BASE(tlb, /ROW, /ALIGN_CENTER)
cname_label = WIDGET_LABEL(wbase2, VALUE='Color Name ')
cname_show = WIDGET_TEXT(wbase2, XSIZE=20)
rgb_label = WIDGET_LABEL(wbase2, VALUE='   RGB Triple ')
rgb_show = WIDGET_TEXT(wbase2, XSIZE=15)

WIDGET_CONTROL, tlb, /REALIZE

ver_cur = !version.release
FOR i = 0, N_ELEMENTS(cnames)-1 DO BEGIN
  uname = 'draw_'+STRING(i, FORMAT='(I3.3)')
  widget_id = WIDGET_INFO(wbase, FIND_BY_UNAME=uname)
  IF widget_id EQ 0 THEN CONTINUE
  ;PRINT, i, cc.(i)
  WIDGET_CONTROL, widget_id, GET_VALUE=wid
  WSET, wid
  out = 0L
  READS, STRJOIN(STRTRIM(STRING(REVERSE(cc.(i)), FORMAT='(Z2.2)'), 2)), out, FORMAT='(Z)'
;  IF ver_cur LT '8.4' THEN $
;    READS, STRJOIN(TO_HEX(REVERSE(cc.(i)), 2)), out, FORMAT='(Z)' ELSE $
;    READS, STRJOIN((REVERSE(cc.(i))).ToHex()), out, FORMAT='(Z)'
  ERASE, COLOR=out
  PLOTS, [0, 0, 0.99, 0.99, 0], [0, 0.95, 0.95, 0, 0], COLOR='000000'x, /NORMAL
ENDFOR

info = {dcp:dcp, cc:cc, cnames:cnames, cname_show:cname_show, rgb_show:rgb_show}
WIDGET_CONTROL, tlb, SET_UVALUE=info

XMANAGER, 'SHOW_COLORS_LIST', tlb, CLEANUP='SHOW_COLORS_LIST_EXIT'

END