#!/usr/bin/env bash
set -eu
# Plot results for thread_cpu_bound.py
./thread_cpu_bound.py "${1:-1000000}" | tee thread_cpu_bound.dat
./thread_cpu_bound.gnuplot
