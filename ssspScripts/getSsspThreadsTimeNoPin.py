#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will parse time of one graph ran with different threads 1-8

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()
MetricsParsed="%(top)s/Tracking/outputs/sssp/ssspMetricsParsed/Threads" %locals()
KronTotals="%(top)s/Tracking/outputs/sssp/ssspKronMetricThreads" %locals()

#Clear files before writing
os.system("""echo "" > %(MetricsParsed)s/TimeNoPin_Threads.txt""" %locals())

vertices=22
edges=32
for threads in [1, 2, 4, 8, 16, 32, 64, 128]:
     if vertices < 10:
       zero="0"
     else:
       zero=""       
       #time parser with no pin tool
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/TimeNoPin_Threads.txt"%locals())
       os.system("cat %(KronTotals)s/ssspOutputThreadsNoPin%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/real/' >> %(MetricsParsed)s/TimeNoPin_Threads.txt"%locals())

