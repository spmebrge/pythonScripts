Script descriptions
getSsspKronMetrics.py       
ssspKroneckerNoPin.py 
ssspThreads.py: provide metrics for graph k=22 edge 32 for all threads
getSsspTimeNoPin.py 
ssspKronecker.py 
getSsspThreadsMetrics.py: parses all metrics into seperate files for k=22 e=32 for all threads
getSsspTime.py: 
ssspThreadsNoPin.py: runs k=22 e=32 for all threads with no pin tool to get times
getSsspThreadsTimeNoPin.py: parses times without pin for all threads
sssp_BB_Info_Parser.py: provides BB info (# instructions, calls, address)

1. ssspThreads.py | ssspThreadsNoPin.py 
2. getSsspThreadsMetrics.py | getSsspThreadsTimeNoPin.py | getSsspThreadsTime.py

1 Thread sequence
1. createKroneckerGraphs.py
2. ssspKronecker.py
3. ssspKroneckerNoPin.py
4. getSsspKronMetrics.py
5. getSsspTime.py: 
6. getSsspTimeNoPin.py
7. sssp_BB_Info_Parser.py
