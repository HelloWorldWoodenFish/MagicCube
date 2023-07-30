# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:06:00 2023

@author: kyle_
"""
initial_status=[[['红', '白', '绿'], ['蓝', '白', '红']],
                [['橙', '白', '绿'], ['蓝', '白', '橙']]]
import copy
def print_cube(status):
    for i in status:
        print(i)
    print()
       
def r_top_corner_ex(status):
    status_o=copy.deepcopy(status)# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:06:00 2023

@author: kyle_
"""
# initial_status=[[['白', '蓝', '橙'], ['白', '绿', '红']],
#                 [['蓝', '红', '白'], ['橙', '白', '绿']]]
#R(C(R(R(C(S)))))/L(Re(L(C(L(S)))))
# initial_status=[[['橙', '绿', '白'], ['蓝', '橙', '白']],
#                 [['白', '蓝', '红'], ['绿', '白', '红']]]
#L(Re(L(L(S))))/R(C(R(Re(R(C(S))))))

# initial_status=[[['绿', '红', '白'], ['白', '红', '蓝']],
#                 [['橙', '白', '绿'], ['蓝', '白', '橙']]]
# #R(C(R(S)))/L(Re(L(S))
initial_status=[[['红', '白', '绿'], ['绿', '白', '橙']],
                [['红', '白', '蓝'], ['蓝', '白', '橙']]]
#L(L(Re(R(S))))))变换两个位置

import copy
def print_cube(status):
    for i in status:
        print(i)
    print()
       
def r_top_corner_ex(status):
    status_o=copy.deepcopy(status)
    status_o[0][0][0]=status[1][1][1]
    status_o[0][0][1]=status[1][1][0]
    status_o[0][0][2]=status[1][1][2]

    status_o[0][1][0]=status[0][0][0]
    status_o[0][1][1]=status[0][0][1]
    status_o[0][1][2]=status[0][0][2]

    status_o[1][0][0]=status[1][0][0]
    status_o[1][0][1]=status[1][0][1]
    status_o[1][0][2]=status[1][0][2]

    status_o[1][1][0]=status[0][1][1]
    status_o[1][1][1]=status[0][1][0]
    status_o[1][1][2]=status[0][1][2]
    print("================Right Top corner exchange===============")
    print_cube(status_o)
    return status_o
def R(status):
    return r_top_corner_ex(status)
    
def l_top_corner_ex(status):
    status_o=copy.deepcopy(status)
    status_o[0][0][0]=status[0][1][0]
    status_o[0][0][1]=status[0][1][1]
    status_o[0][0][2]=status[0][1][2]

    status_o[0][1][0]=status[1][0][0]
    status_o[0][1][1]=status[1][0][2]
    status_o[0][1][2]=status[1][0][1]

    status_o[1][0][0]=status[0][0][0]
    status_o[1][0][1]=status[0][0][2]
    status_o[1][0][2]=status[0][0][1]

    status_o[1][1][0]=status[1][1][0]
    status_o[1][1][1]=status[1][1][1]
    status_o[1][1][2]=status[1][1][2]
    print("================Left Top corner exchange===============")
    print_cube(status_o)
    return status_o

def L(status):
    return l_top_corner_ex(status)   


def clock_top_corner_ex_atom(status):
    status_o=copy.deepcopy(status)
    status_o[0][0][0]=status[1][0][2]
    status_o[0][0][1]=status[1][0][1]
    status_o[0][0][2]=status[1][0][0]

    status_o[0][1][0]=status[0][0][0]
    status_o[0][1][1]=status[0][0][1]
    status_o[0][1][2]=status[0][0][2]

    status_o[1][0][0]=status[1][1][0]
    status_o[1][0][1]=status[1][1][1]
    status_o[1][0][2]=status[1][1][2]

    status_o[1][1][0]=status[0][1][2]
    status_o[1][1][1]=status[0][1][1]
    status_o[1][1][2]=status[0][1][0]
    return status_o

def clock_top_corner_ex(status):
    status_o=clock_top_corner_ex_atom(status)
    print("================clock Top corner exchange===============")
    print_cube(status_o)
    return status_o

def C(status):
    return clock_top_corner_ex(status) 

def re_clock_top_corner_ex(status):
    status_o=clock_top_corner_ex_atom(
                clock_top_corner_ex_atom(
                    clock_top_corner_ex_atom(status)))
    print("================reverse clock Top corner exchange===============")
    print_cube(status_o)
    return status_o
def Re(status):
    return re_clock_top_corner_ex(status) 


S=initial_status
print_cube(S)








    status_o[0][0][0]=status[1][1][1]
    status_o[0][0][1]=status[1][1][0]
    status_o[0][0][2]=status[1][1][2]

    status_o[0][1][0]=status[0][0][0]
    status_o[0][1][1]=status[0][0][1]
    status_o[0][1][2]=status[0][0][2]

    status_o[1][0][0]=status[1][0][0]
    status_o[1][0][1]=status[1][0][1]
    status_o[1][0][2]=status[1][0][2]

    status_o[1][1][0]=status[0][1][1]
    status_o[1][1][1]=status[0][1][0]
    status_o[1][1][2]=status[0][1][2]
    print("================Right Top corner exchange===============")
    print_cube(status_o)
    return status_o
def R(status):
    return r_top_corner_ex(status)
    
def l_top_corner_ex(status):
    status_o=copy.deepcopy(status)
    status_o[0][0][0]=status[0][1][0]
    status_o[0][0][1]=status[0][1][1]
    status_o[0][0][2]=status[0][1][2]

    status_o[0][1][0]=status[1][0][0]
    status_o[0][1][1]=status[1][0][2]
    status_o[0][1][2]=status[1][0][1]

    status_o[1][0][0]=status[0][0][0]
    status_o[1][0][1]=status[0][0][2]
    status_o[1][0][2]=status[0][0][1]

    status_o[1][1][0]=status[1][1][0]
    status_o[1][1][1]=status[1][1][1]
    status_o[1][1][2]=status[1][1][2]
    print("================Left Top corner exchange===============")
    print_cube(status_o)
    return status_o

def L(status):
    return l_top_corner_ex(status)   


def clock_top_corner_ex_atom(status):
    status_o=copy.deepcopy(status)
    status_o[0][0][0]=status[1][0][2]
    status_o[0][0][1]=status[1][0][1]
    status_o[0][0][2]=status[1][0][0]

    status_o[0][1][0]=status[0][0][0]
    status_o[0][1][1]=status[0][0][1]
    status_o[0][1][2]=status[0][0][2]

    status_o[1][0][0]=status[1][1][0]
    status_o[1][0][1]=status[1][1][1]
    status_o[1][0][2]=status[1][1][2]

    status_o[1][1][0]=status[0][1][2]
    status_o[1][1][1]=status[0][1][1]
    status_o[1][1][2]=status[0][1][0]
    return status_o

def clock_top_corner_ex(status):
    status_o=clock_top_corner_ex_atom(status)
    print("================clock Top corner exchange===============")
    print_cube(status_o)
    return status_o

def C(status):
    return clock_top_corner_ex(status) 

def re_clock_top_corner_ex(status):
    status_o=clock_top_corner_ex_atom(
                clock_top_corner_ex_atom(
                    clock_top_corner_ex_atom(status)))
    print("================reverse clock Top corner exchange===============")
    print_cube(status_o)
    return status_o
def Re(status):
    return re_clock_top_corner_ex(status) 


S=initial_status
print_cube(S)
R(L(S))






