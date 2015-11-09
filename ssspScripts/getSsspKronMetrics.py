#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will parse metrics into one file located at <top>/Tracking/outputs/MetricParsed

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()
MetricsParsed="%(top)s/Tracking/outputs/sssp/ssspMetricsParsed" %locals()
KronMetrics="%(top)s/Tracking/outputs/sssp/ssspKronMetrics" %locals()

#Clear files before writing
os.system("""echo "" > %(MetricsParsed)s/BB.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/TotalInst.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemReadInst.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemReadSize.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemWriteInst.txt""" %locals())
os.system("""echo "" > %(MetricsParsed)s/MemWriteSize.txt""" %locals())
for threads in [1]:
  for vertices in range(5,26):
     if vertices < 10:
       zero="0"
     else:
       zero=""
     for edges in [4, 8, 16, 32]:
       #Basic Blocks
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/BB.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Number of basic blocks/' >> %(MetricsParsed)s/BB.txt"%locals())

       #Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/TotalInst.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Number of instructions/' >> %(MetricsParsed)s/TotalInst.txt"%locals())

#Memory Read Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemReadInst.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Read Instructions/' >> %(MetricsParsed)s/MemReadInst.txt"%locals())

#Memory Read Size
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemReadSize.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Read Size/' >> %(MetricsParsed)s/MemReadSize.txt"%locals())

#Memory Write Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemWriteInst.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Write Instructions/' >> %(MetricsParsed)s/MemWriteInst.txt"%locals())

#Memory Write Size
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/MemWriteSize.txt"%locals())
       os.system("cat %(KronMetrics)s/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Write Size/' >> %(MetricsParsed)s/MemWriteSize.txt"%locals())
