#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will parse metrics into one file located at <top>/Tracking/outputs/MetricParsed

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()

#Clear files before writing
os.system("""echo "" > /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/BB.txt""")
os.system("""echo "" > /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/TotalInst.txt""")
os.system("""echo "" > /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemReadInst.txt""")
os.system("""echo "" > /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemReadSize.txt""")
os.system("""echo "" > /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemWriteInst.txt""")
os.system("""echo "" > /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemWriteSize.txt""")
for threads in [1]:
  for vertices in range(5,23):
     if vertices < 10:
       zero="0"
     else:
       zero=""
     for edges in [4, 8, 16, 32]:
       #Basic Blocks
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/BB.txt"%locals())
       os.system("cat /home/kaya3/aavila/thesis-repo/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Number of basic blocks/' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/BB.txt"%locals())

       #Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/TotalInst.txt"%locals())
       os.system("cat /home/kaya3/aavila/thesis-repo/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Number of instructions/' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/TotalInst.txt"%locals())

#Memory Read Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemReadInst.txt"%locals())
       os.system("cat /home/kaya3/aavila/thesis-repo/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Read Instructions/' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemReadInst.txt"%locals())

#Memory Read Size
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemReadSize.txt"%locals())
       os.system("cat /home/kaya3/aavila/thesis-repo/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Read Size/' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemReadSize.txt"%locals())

#Memory Write Instructions
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemWriteInst.txt"%locals())
       os.system("cat /home/kaya3/aavila/thesis-repo/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Write Instructions/' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemWriteInst.txt"%locals())

#Memory Write Size
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemWriteSize.txt"%locals())
       os.system("cat /home/kaya3/aavila/thesis-repo/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/Memory Write Size/' >> /home/kaya3/aavila/thesis-repo/Tracking/outputs/MetricParsed/MemWriteSize.txt"%locals())
