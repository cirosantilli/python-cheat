#!/usr/bin/env gnuplot
set terminal png size 600, 1200
set style data linespoints
set output 'thread_cpu_bound.tmp.png'
set key autotitle columnhead
set multiplot layout 4,1 title "Python Threads vs Processes with 8 hyperthreads" font ",18"
set title font ",14"

set title 'CPU bound'
set key left top
set xlabel "threads"
set ylabel "time (s)"
plot 'thread_cpu_bound.dat' using 1:2, \
     'thread_cpu_bound.dat' using 1:3

set title 'CPU bound / threads'
set key right center
set yrange [0:*]
plot 'thread_cpu_bound.dat' using 1:($2/$1) title 'CpuThread', \
     'thread_cpu_bound.dat' using 1:($3/$1) title 'CpuProcess'

set title 'Thread / Process ratio'
set ylabel "ratio"
set yrange [0:*]
plot 'thread_cpu_bound.dat' using 1:($2/$3) notitle

set title 'IO bound'
set key default
set ylabel "time (s)"
set yrange[0:2]
plot 'thread_cpu_bound.dat' using 1:4 title 'IoThread', \
     'thread_cpu_bound.dat' using 1:5 title 'IoProcess'
