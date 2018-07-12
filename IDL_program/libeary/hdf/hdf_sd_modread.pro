PRO HDF_SD_MODREAD, HDFID, VARNAME, FILLNAME, SFNAME, DATA, _EXTRA=EXTRA_KEYWORDS

nameid = hdf_sd_nametoindex(hdfid, VARNAME)
if (nameid eq -1) then message, string(varname, format='("VARNAME not found: ", a)')

dataid = hdf_sd_select(hdfid, nameid)
hdf_sd_getdata, dataid, DATA, _extra=extra_keywords
nanid = hdf_sd_attrfind(dataid, FILLNAME)
if (nanid eq -1) then message, string(fillname, format='("FILLNAME not found: ", a)')

hdf_sd_attrinfo, dataid, nanid, data = nan_value
sfid = hdf_sd_attrfind(dataid, SFNAME)
if (sfid eq -1) then message, string(SFNAME, format='("SFNAME not found: ", a)')

hdf_sd_attrinfo, dataid, sfid, data = sf_value

DATA = temporary(DATA)*1.0

nan_idx = where(DATA eq nan_value(0)*1.0, nan_num)
if (nan_num gt 0) then DATA(nan_idx) = !values.f_nan

DATA = temporary(DATA) * sf_value(0)

END
