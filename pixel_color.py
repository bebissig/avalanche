# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 00:39:06 2019

@author: Lenovo
"""

from PIL import Image
import numpy as np


class SLFlevel_from_png(object):
    ''' Loading the hopefully unchaning region map with SLF levels. 
    MEthod SLF_from_coord returns level at coordinates in meters. '''
    
    def __init__(self,im_namepath):
        self.im = Image.open('example_image.png')
        self.rgb_im = self.im.convert('RGB')

    def coord_to_pixel(self,coord_x, coord_y):
        # manually extracted fixpoints (map.geo.admin, far northwest and southeast)
        # 0_rochers_du_cerf_p1196
        # 1_near_costi_di_san_giuan_p264
        x = [528300.17,811066.74] # coord
        y = [203018.39, 126667.08]
        px_x = [87,581] #pixel coord
        px_y = [177,316]
        
        px_per_m_x = np.abs((px_x[0]-px_x[1])/ (x[0]- x[1]))
        px_per_m_y = np.abs((px_y[0]-px_y[1])/ (y[0]- y[1]))
        px_per_m = np.average([px_per_m_x,px_per_m_y])
        
        px_x = np.average([(coord_x-x[0])*px_per_m+px_x[0],(coord_x-x[1])*px_per_m+px_x[1]])
        px_y = np.average([-(coord_y-y[0])*px_per_m+px_y[0],-(coord_y-y[1])*px_per_m+px_y[1]])

        
#        print('Pixel per kilometer, x-direction: {:.2f}'.format(1000*px_per_m_x))
#        print('Pixel per kilometer, y-direction: {:.2f}'.format(1000*px_per_m_y))
#        print('Avergae pixel per kilometer: {:.2f}'.format(1000*px_per_m))
    
        return [int(px_x), int(px_y)]
        
    def rgb_from_px(self,px):
        r,g,b = self.rgb_im.getpixel((px[0],px[1]))
        return [r,g,b]
    
    def SLF_from_rgb(self,rgb):
        ''' Levels 4 and 5 still to be implementend.
        Level 5 (red/black checkered by some conditional for black and red being present).'''
        if rgb ==  [255, 153, 0]:
            SLF_level = 3
        elif rgb == [255, 255, 0]:
            SLF_level = 2
        elif rgb == [203, 255, 102]:
            SLF_level = 1
        elif rgb == [0, 0, 0]:
            SLF_level = 0
        return SLF_level  
    
    def SLF_from_coord(self,coord_x,coord_y):
        px = self.coord_to_pixel(coord_x,coord_y)
        rgb = self.rgb_from_px(px)
        return self.SLF_from_rgb(rgb)
    
SLF_png = SLFlevel_from_png('gk1_b_0.png')
print(SLF_png.SLF_from_coord(687599.62, 164450.40)) # test near andermatt
print(SLF_png.SLF_from_coord(568000.44, 133374.62)) # test east lac lemain
print(SLF_png.SLF_from_coord(546700.39, 206724.65)) # test jura
print(SLF_png.SLF_from_coord(648749.31, 232724.92)) # test near zurich

	
