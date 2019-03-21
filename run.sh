#!/bin/bash

dwi='jq -r .dwi config.json'
bvals='jq -r .bvals config.json'
bvecs='jq -r .bvals config.json'
t1=`jq -r '.t1' config.json`
csd_type=`jq -r '.csd' config.json`

if [ $t1 != "null" ]; then
	mkdir -p tractseg_output
	ln -sf $t1 T1w_acpc_dc_restore_brain.nii.gz
fi

python compute_peaks.py \
		-t1 $t1 \
		-dwi $dwi \ 
		-bvals $bvals \ 
		-bvecs $bvecs \ 
		-csd_type $csd_type \ 
		-out_dir tractseg_output
