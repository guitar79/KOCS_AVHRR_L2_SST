# -*- coding: utf-8 -*-
"""
@author: guitar79@naver.com
"""

import os
drbase = '/media/guitar79/6T1/KOSC/L2_SST_NOAA/'
for year in range(2011,2017):
    for i in sorted(os.listdir(drbase+str(year))):
        #if i[-4:] == '.jpg' or i[-4:] == '.JPG' and os.path.exists('%s%s/%s.asc' %(drbase, str(year), i[:-4])):
        if i[-4:] == '.jpg' or i[-4:] == '.JPG':          
            if os.path.isfile('%s%s/%s.asc.zip' %(drbase, str(year), i[:-4])):
                os.remove('%s%s/%s.asc.zip' %(drbase, str(year), i[:-4]))
                print ('deleting %s%s/%s.asc.zip' %(drbase, str(year), i[:-4]))
            else :
                print ('no file %s%s/%s.asc.zip' %(drbase, str(year), i[:-4]))