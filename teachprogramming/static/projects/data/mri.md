MRI Data
========

As an undergrad at university, I did a project that took uncompressed binary data of a low resolution mri image and visulised it in java.
I loved the use of real data as a programming exercise.
Below are some notes about the current MRI datasets, fileformats and views.
The goal is to create a set of activities for GCSE level Computing students to visulise this data.

* Viewer
    * Software
        * [Papaya](http://rii-mango.github.io/Papaya/) javascript web viewer for NII files
            * [other?](http://mangoviewer.com/papaya.html)
    * Guides
        * [Creating 3D visualizations of MRI data: A brief guide](https://f1000research.com/articles/4-466)
* File Formats
    * spec
        * [nifti v1 fileformat spec](https://brainder.org/2012/09/23/the-nifti-file-format/) pretty hardcore!
    * Python 
        * [Nibable](https://nipy.org/nibabel/gettingstarted.html) library for loading MRI files
        * [niio](https://github.com/kristianeschenburg/niio)
* Data
    * [OpenNeuro](https://openneuro.org/) - MRI datasets
        * old site [openfmri.org](https://openfmri.org/dataset/)
    * [UK BioBank data](https://www.fmrib.ox.ac.uk/ukbiobank/)
        * [Papaya view of BioBank rfMRI_ICA_d25_good_nodes](https://www.fmrib.ox.ac.uk/ukbiobank/group_means/rfMRI_ICA_d25_good_nodes.html)
            * [T1_T2FLAIR_fMRI.nii.gz](https://www.fmrib.ox.ac.uk/ukbiobank/group_means/ukb/T1_T2FLAIR_fMRI.nii.gz)
            * [rfMRI_ICA_d25_good_nodes.nii.gz](https://www.fmrib.ox.ac.uk/ukbiobank/group_means/ukb/rfMRI_ICA_d25_good_nodes.nii.gz)
        * [Demo](https://www.fmrib.ox.ac.uk/ukbiobank/group_means/WINpapaya/GeneralTemplate/?path=%22../data/General/edge_list_d25.csv%22&param=0;2;Red%20Overlay;Blue%20Overlay;3;15;(0,0,0))
            * [brain_image.gz](https://www.fmrib.ox.ac.uk/ukbiobank/group_means/WINpapaya/brain_image.gz)
    * [DataLad](https://www.datalad.org/) Scientific Data Community? Explorable versioned data? API for data?

```bash
pip3 install nibabel
curl -O "https://www.fmrib.ox.ac.uk/ukbiobank/group_means/WINpapaya/brain_image.gz"
```

Consider javascript viewer - may need arraybuffer?
https://javascript.programmingpedia.net/en/tutorial/417/binary-data

TODO: dump data from medial format into 3d array of plain bytes
