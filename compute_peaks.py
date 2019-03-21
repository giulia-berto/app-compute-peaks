import os
from os.path import join
import numpy as np
import nibabel as nib
import argparse
from mrtrix import create_fods, create_brain_mask


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-t1', nargs='?', const=1, default='',
	                    help='T1')
    parser.add_argument('-dwi', nargs='?', const=1, default='',
	                    help='dwi')   
    parser.add_argument('-bvals', nargs='?', const=1, default='',
	                    help='bvals') 
    parser.add_argument('-bvecs', nargs='?', const=1, default='',
	                    help='bvecs')  
    parser.add_argument('-csd_type', nargs='?', const=1, default='',
	                    help='available options: csd_msmt_5tt | csd_msmt | csd')  
    parser.add_argument('-brain_mask', nargs='?', const=1, default='',
	                    help='The brain mask')   
    parser.add_argument('-out_dir', nargs='?', const=1, default='',
	                    help='The output directory') 	
    args = parser.parse_args()

    if args.brain_mask != 'null':
	print("Using provided brain mask.")
	brain_mask = args.brain_mask
    else:	
	print("Computing brain mask from T1 using BET.")
    	brain_mask = create_brain_mask(args.t1, args.out_dir)

    create_fods(args.dwi, args.out_dir, args.bvals, args.bvecs, brain_mask, args.csd_type, nr_cpus=-1)
