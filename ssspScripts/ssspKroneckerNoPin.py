#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will run sssp benchmark w/o using pin
usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()
KronTotalsNoPin="%(top)s/Tracking/outputs/sssp/ssspKronTotalsNoPin" %locals()

for threads in [1]:
   for vertices in range(22,26):
     if vertices < 10:
       zero="0"
     else:
       zero=""
     for edges in [4, 8, 16, 32]:
       #run sssp program
       os.system("time (%(top)s/Green-Marl/apps/output_cpp/bin/sssp %(top)s/Green-Marl/apps/output_cpp/data/KronGraph%(zero)s%(vertices)i_%(edges)i_%(threads)i_Thesis.bin %(threads)i) >& %(KronTotalsNoPin)s/totalNoPin%(zero)s%(vertices)i_%(edges)i_%(threads)i_Thesis.txt" %locals())

