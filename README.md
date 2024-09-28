# WEEK 3 & 4

## Step 1: Initialize BioPython
```bash
ssh quezadgc@ilogin.ibex.kaust.edu.sa
pip install biopython
```

## Step 2: Create Git Repository
```bash
mkdir Week4
cd Week4/
git init
touch gene_finder.py README.md
nano gene_finder.py 
```
## Problem 1: Finding reading frames
We need to run the code of "GeneFinder.py" to find the open reading frames and I used the file "test1.fasta" to test the code.

```bash
python gene_finder.py test1.fasta
```
OUTPUT:
``` bash
>ORF_0_12
ATGCGTACGTAG
>ORF_27_93
ATGATGCTAGCTAACGTAGCTAGCTATACGATCGATGACGTAGCTGATGCTGGTACGATATCGTAG
>ORF_30_93
ATGCTAGCTAACGTAGCTAGCTATACGATCGATGACGTAGCTGATGCTGGTACGATATCGTAG
>ORF_19_31
ATGCGTAAATGA
>ORF_61_70
ATGACGTAG
>ORF_73_97
```

## Problem 2: Finding reading frames including the reverse complements
We need to run the code of "GeneFinderRvCom.py" to find the open reading frames and I used the file "test1.fasta" to test the code.

```bash
touch gene_finder_RvCom.py
nano gene_finder_RvCom.py 
python gene_finder_RvCom.py test1.fasta 
```
OUTPUT:
``` bash
>ORF_0_12
ATGCGTACGTAG
>ORF_27_93
ATGATGCTAGCTAACGTAGCTAGCTATACGATCGATGACGTAGCTGATGCTGGTACGATATCGTAG
>ORF_30_93
ATGCTAGCTAACGTAGCTAGCTATACGATCGATGACGTAGCTGATGCTGGTACGATATCGTAG
>ORF_19_31
ATGCGTAAATGA
>ORF_61_70
ATGACGTAG
>ORF_73_97
```
## Problem 5: Finding reading frames including the reverse complements and applying code to all 14 downloaded genomes 

```bash
find /home/quezadgc/ncbi_dataset/data -type f -name "*GCF*.fna" | while read genome; do python gene_finder_RvCom.py "$genome"; done > all_orfs.txt
```
