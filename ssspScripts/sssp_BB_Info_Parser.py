#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will generate the Kronecker.txt graphs with 2^3 vertices for the edges 4
#The .bin files will be created for each .txt previously generated
#The pin tool will use the .so algorithm to grab BBL info on the sssp benchmark with the given .bins

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()
KronTotals="%(top)s/Tracking/outputs/sssp/ssspKronTotals" %locals()
KronMetrics="%(top)s/Tracking/outputs/sssp/ssspKronMetrics" %locals()

#run pin using Block_Calls_Thesis BB info collector on sssp program
#command="%(top)s/pin-2.14-71313-gcc.4.4.7-linux/pin -t %(top)s/pin-2.14-71313-gcc.4.4.7-linux/source/tools/MyPinTool/obj-intel64/Block_Calls_Thesis.so -o %(top)/Tracking/outputs/sssp/ssspBBL/BBL_Info.txt -- %(top)s/Green-Marl/apps/output_cpp/bin/sssp %(top)s/Green-Marl/apps/output_cpp/data/KronGraph05_4_1_Thesis.bin 1" %locals()

#generate graph into .txt
for threads in [1]:
  for vertices in range(22,26):
     if vertices < 10:
       zero="0"
     else:
       zero=""
     for edges in [4, 8, 16, 32]:
#os.system("%(top)s/graphbench/data/generator/generator_seq 0%(vertex)i -e 4 -o %(top)s/Tracking/outputs/kroneckerGraphs/KronGraph0%(vertex)i_4_1_Thesis.txt" %locals())

#convert .txt graph to .bin/
#os.system("%(top)s/Green-Marl/apps/output_cpp/bin/graph_gen %(top)s/Green-Marl/apps/output_cpp/data/KronGraph0%(vertex)i_4_1_Thesis.bin %(top)s/Tracking/outputs/kroneckerGraphs/KronGraph0%(vertex)i_4_1_Thesis.txt 0" %locals())

#os.system(command)
        os.system("%(top)s/pin-2.14-71313-gcc.4.4.7-linux/pin -t %(top)s/pin-2.14-71313-gcc.4.4.7-linux/source/tools/MyPinTool/obj-intel64/Block_Calls_Thesis.so -o %(top)s/Tracking/outputs/sssp/ssspBBL/BBL_Info_%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt -- %(top)s/Green-Marl/apps/output_cpp/bin/sssp %(top)s/Green-Marl/apps/output_cpp/data/KronGraph%(zero)s%(vertices)i_%(edges)i_%(threads)i_Thesis.bin %(threads)i >> %(top)s/Tracking/outputs/sssp/ssspBBL/BBL_Info_%(zero)s%(vertices)i_%(edges)i_%(threads)i.txt" %locals())
  
#sorts the BBL info by unique address back into the same file
#os.system("sort -s -n -u %(top)s/Tracking/outputs/sssp/ssspBBL/BBL_Info.txt -o %(top)s/Tracking/outputs/sssp/ssspBBL/BBL_Info.txt" %locals())
