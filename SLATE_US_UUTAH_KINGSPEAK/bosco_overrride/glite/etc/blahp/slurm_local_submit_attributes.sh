#!/bin/sh
echo "#SBATCH --partition=lonepeak-osg"
echo "#SBATCH --ntasks=4"
echo "#SBATCH --mem=24G"
echo "#SBATCH --time=72:00:00"