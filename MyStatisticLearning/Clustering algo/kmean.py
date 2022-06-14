#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:47:58 2022

@author: felix
"""

def createLine(XY_list, accuracy=0.00005, endurance=2000):
    #XY_list being a list of lists [[], [], []]
    #accuracy being marginal delta-distance (in %) where we want to stop
    #endurance being the maximum amount of iterations user wants
    
    # all encompassing function that solves any linear function
    def Curve(X = 0, B = 0, A = 1, Y = 1, solve = 'y'):
        if solve == 'y':
            return X*A + B
        
        elif solve == 'x':
            return (Y-B)/A
        
        elif solve == 'b':
            return Y - X*A
        
        elif solve == 'a':
            return (Y - B)/X
        
        else:
            raise Exception(f'Value for solve "{solve}" does not exist. Try : "x", "y" or "b"')
    
    # gets coordinates of value on a line(slope=a_, y-intercept=b_) closest to point xy
    def Coordinates(xy, a_, b_):
            b = Curve(X = xy[0], A = -1/a_, Y = xy[1], solve = 'b')
            
            x_ = (b - b_)/(a_+1/a_)
            y_ = Curve(X = x_, B = b_, A = a_)
            
            return [x_, y_]
    
    xmean = sum([xy[0] for xy in XY_list])/len(XY_list)
    ymean = sum([xy[1] for xy in XY_list])/len(XY_list)
    b_ = ymean-0.1
    b_delta = 1
    
    count = 1
    while True:
        # collecting the different point and their distance relative to to seperating line
        
        dist_tot = 0
        dist_tot_up = 0
        dist_tot_down = 0
        
        a_ = Curve(X = xmean, B = b_, Y = ymean, solve='a')
        print(a_, "\t", b_)
        for xy in XY_list:
            # UP
            xy_up = Coordinates(xy, a_, b_+b_delta)
            #this must be maximized
            dist_tot_up += ((xy_up[0] - xy[0])**2 + (xy_up[1] - xy[1])**2)**(1/2)
            
            # MIDDLE
            xy_ = Coordinates(xy, a_, b_)
            #this must be maximized
            dist_tot += ((xy_[0] - xy[0])**2 + (xy_[1] - xy[1])**2)**(1/2)
            
            # DOWN
            xy_down = Coordinates(xy, a_, b_-b_delta)
            #this must be maximized
            dist_tot_down += ((xy_down[0] - xy[0])**2 + (xy_down[1] - xy[1])**2)**(1/2)
            
            
        up_middle_down = {"dist_tot_up": dist_tot_up, "dist_tot": dist_tot, "dist_tot_down": dist_tot_down}
        l=list(up_middle_down.items())
        l.sort(reverse=True) #sort in reverse order
        # convert the list in dictionary 
            
        if l[0][0] == "dist_tot_up":
            b_ = b_ + b_delta
        
        elif l[0][0] == "dist_tot":
            b_ = b_
        
        else:
            b_ = b_ - b_delta
            
        dist_tot = l[0][1]
        
        try:
            if ((dist_tot-dist_tot_last)/dist_tot_last) <= accuracy:
                return {"a": a_, "b": b_, "stop": "accuracy", "iterations": count}
        
        except:
            pass
        
        dist_tot_last = dist_tot
        
        count += 1
        
        if count == endurance:
            return {"a": a_, "b": b_, "stop": "endurance", "iterations": count}


