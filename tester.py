#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will generate the Kronecker.txt graphs with 2^[5-10] vertices for the edges [4, 8, 16, 32]
#The .bin files will be created for each .txt previously generated

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()
zero=""
#os.system("cd /home/kaya1/aavila/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ManualExamples"%locals())
#os.system("make pinatrace_thesis.test"%locals())
for threads in [1]:
  for vertices in range(5,23):
     if vertices < 10:
       zero="0"
     else:
       zero=""
     for edges in [4, 8, 16, 32]:
        #generate graph into .txt
          os.system("""echo "%(zero)s%(vertices)i_%(edges)i_%(threads)i" """ %locals())
