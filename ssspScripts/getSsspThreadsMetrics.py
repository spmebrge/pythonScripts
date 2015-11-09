#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will parse metrics of one graph for different threads 1-8 into one file located at <top>/Tracking/outputs/MetricParsed/Threads

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()
MetricsParsed="%(top)s/Tracking/outputs/sssp/ssspMetricsParsed/Threads" %locals()
KronMetrics="%(top)s/Tracking/outputs/sssp/ssspKronMetricThreads" %locals()

#Clear files before writing
os.system("""echo "" > %(MetricsParsed)s/BB_Threads.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/TotalInst_Threads.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemReadInst_Threads.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemReadSize_Threads.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemWriteInst_Threads.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemWriteSize_Threads.txt""" %locals())

vertices=22
edges=32
for threads in [1, 2, 4, 8, 16, 32, 64, 128]:
     if vertices < 10:
       zero="0"
     else:
       zero=""
       #Basic Blocks
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/BB_Threads.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetricThreads%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Number of basic blocks/' >> %(MetricsParsed)s/BB_Threads.txt"%locals())

       #Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/TotalInst_Threads.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetricThreads%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Number of instructions/' >> %(MetricsParsed)s/TotalInst_Threads.txt"%locals())

#Memory Read Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemReadInst_Threads.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetricThreads%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Read Instructions/' >> %(MetricsParsed)s/MemReadInst_Threads.txt"%locals())

#Memory Read Size
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemReadSize_Threads.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetricThreads%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Read Size/' >> %(MetricsParsed)s/MemReadSize_Threads.txt"%locals())

#Memory Write Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemWriteInst_Threads.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetricThreads%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Write Instructions/' >> %(MetricsParsed)s/MemWriteInst_Threads.txt"%locals())

#Memory Write Size
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemWriteSize_Threads.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetricThreads%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Write Size/' >> %(MetricsParsed)s/MemWriteSize_Threads.txt"%locals())
