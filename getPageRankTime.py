#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will parse metrics into one file located at <top>/Tracking/outputs/MetricParsed

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()
MetricsParsed="%(top)s/Tracking/outputs/PageRank/PageRankMetricsParsed" %locals()
KronTotals="%(top)s/Tracking/outputs/PageRank/PageRankKronTotals" %locals()

#Clear files before writing
os.system("""echo "" > %(MetricsParsed)s/Time.txt""" %locals())

for threads in [1]:
  for vertices in range(5,23):
     if vertices < 10:
       zero="0"
     else:
       zero=""
     for edges in [4, 8, 16, 32]:
       #Basic Blocks
       os.system("echo '%(zero)s%(vertices)i_%(edges)i_%(threads)i' >> %(MetricsParsed)s/Time.txt"%locals())
       os.system("cat %(KronTotals)s/PageRankOutput%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt | awk '/real/' >> %(MetricsParsed)s/Time.txt"%locals())

