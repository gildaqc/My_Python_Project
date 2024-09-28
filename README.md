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
## Problem 4: Finding reading frames including the reverse complements and applying code to all 14 downloaded genomes 

```bash
find /home/quezadgc/ncbi_dataset/data -type f -name "*GCF*.fna" | while read genome; do python gene_finder_RvCom.py "$genome"; done > all_orfs.txt
```
OUTPUT: all_orfs.txt (Text file containing all the open reading frames for the 14 downloaded genomes)

## Problem 5: Implementing gene finder with length filter
We need to run the code of "GeneFinderFilter.py" to implement a filter by length that discards short ORFs that are unlikely to be functional genes (e.g., less than 100 codon)

```bash
touch genefinder_filtered.py
nano genefinder_filtered.py
python gene_finder_filter.py all_orfs.txt -l 100 > gfind_filter_output.fasta
git add gene_finder_filter.py
git commit -m "added gene_finder_filter.py"
```
## Problem 6: Implementing gene finder with length, rbs site and rbs type filter
We need to run the code of "GeneFinderFilter.py" to filter all predicted ORFs based on whether they contain a Shine-Dalgarno sequence  (AGGAGG) up to 20bp upstream of the start codon.

```bash
touch gene_finder_rbs.py
nano gene_finder_rbs.py 
python gene_finder_rbs.py gfind_filter_output.fasta -l 100 -u 20 -r AGGAGG > ORFs_RBS_OUTPUT.fasta
git add gene_finder_rbs.py 
git commit -m "added gene_finder_rbs.py"
```

