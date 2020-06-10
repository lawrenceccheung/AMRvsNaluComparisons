# AMR-wind vs Nalu-wind comparison 7

## Summary
Run using initial temperature perturbations, looser tolerances

## Details

Top of log file:
```
nodes = 16
cores = 16
ncpus = 256
==============================================================================
                AMR-Wind (https://github.com/exawind/amr-wind)

  AMR-Wind Git SHA :: 449d2d69c01e
  AMReX version    :: 20.05-42-g0c4606cf624a ( 20.05-42-g0c4606cf624a )

  Exec. date       :: Tue Jun  9 18:02:24 2020
  Build date       :: Jun  9 2020 15:53:02
  C++ compiler     :: Intel 18.0.5.20180823

  MPI              :: ON    (Num. ranks = 256)
  GPU              :: OFF
  OpenMP           :: OFF

           This software is released under the BSD 3-clause license.           
 See https://github.com/Exawind/amr-wind/blob/development/LICENSE for details. 
------------------------------------------------------------------------------

MPI initialized with 256 MPI processes
MPI initialized with thread support level 0
AMReX (20.05-42-g0c4606cf624a) initialized
Initializing AMR-Wind ...
```

Get the line_plot.txt file at: 

## Comparison plots
**AMR-wind Hub-height velocity slice**  

**Nalu-wind Hub-height velocity slice**  
<img src="../../NaluRun/vizplots/naluwind_danaero1_Smag_20000_HHslice.png" width="600">  

**AMR-wind streamwise velocity slice**  

**Nalu-wind streamwise velocity slice**  
<img src="../../NaluRun/vizplots/naluwind_danaero1_Smag_20000_StreamSlice.png" width="400">

**AMR-wind streamwise temperature slice**  

**Nalu-wind streamwise temperature slice**  
<img src="../../NaluRun/vizplots/naluwind_danaero1_Smag_20000_StreamSliceT.png" width="500">
