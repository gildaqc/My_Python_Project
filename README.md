### WEEK 3
## 1. Write the README

% scp ~/Downloads/Bioinformatic/bacterial_dataset.zip quezadgc@ilogin.ibex.kaust.edu.sa:~/
quezadgc@ilogin.ibex.kaust.edu.sa's password: 
bacterial_dataset.zip                                  100%   16MB  14.0MB/s   00:01    

 % ssh quezadgc@ilogin.ibex.kaust.edu.sa

## 2. Uncompress the zip file on IBEX
[quezadgc@login509-02-r ~]$ ls
bacterial_dataset.zip  Ecoli_first10.fna  genomes   README.md
ecoli-10-lines.fna     ecoli.fna          in_class

[quezadgc@login509-02-r ~]$ unzip bacterial_dataset.zip 
Archive:  bacterial_dataset.zip
replace README.md? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: README.md               
  inflating: ncbi_dataset/data/data_summary.tsv  
  inflating: ncbi_dataset/data/assembly_data_report.jsonl  
  inflating: ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008525.1/GCF_000008525.1_ASM852v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008605.1/GCF_000008605.1_ASM860v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008625.1/GCF_000008625.1_ASM862v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008745.1/GCF_000008745.1_ASM874v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000027305.1/GCF_000027305.1_ASM2730v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008545.1/GCF_000008545.1_ASM854v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008565.1/GCF_000008565.1_ASM856v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008725.1/GCF_000008725.1_ASM872v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000008785.1/GCF_000008785.1_ASM878v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna  
  inflating: ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000006825.1/GCF_000006825.1_ASM682v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000006865.1/GCF_000006865.1_ASM686v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000007125.1/GCF_000007125.1_ASM712v1_genomic.fna  
  inflating: ncbi_dataset/data/GCF_000091085.2/GCF_000091085.2_ASM9108v2_genomic.fna  
  inflating: ncbi_dataset/data/dataset_catalog.json  
  inflating: md5sum.txt              
[quezadgc@login509-02-r ~]$ 

##3. 
## PRINT THE LARGEST GENOME
[quezadgc@login509-02-r data]$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'echo "$(tail -n +2 "$1" | wc -c) $(basename "$1")"' _ {} \; | sort -n | tail -n 1 | awk '{print "The largest genome is in \"" $2 "\": " $1}'
#### THIS CODE WILL SCAN ALL THE .fna FILES IN THE GIVEN DIRECTORY. Exec IS TO EXECUTE THE COMMAND IN EACH FILE. tail IS TO COUNT THE NUMBER OF CHARACTERS IN EACH FILE EXCLUDING THE FIRST LINE WHICH IS THE TITLE. Sort TO ORDER THE FILES AND FIND THE ONE WHICH LARGEST NUMBER OF CHARACTERS. echo IS TO PRINT THE OUTPUT (FILE NAME AND NUMBER OF CHARACTERS IN GENOME). 

OUTPUT: The largest genome is in "GCF_000006745.1_ASM674v1_genomic.fna": 4083974


## PRINT THE SMALLEST GENOME
[quezadgc@login509-02-r data]$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'echo "$(tail -n +2 "$1" | wc -c) $(basename "$1")"' _ {} \; | sort -n | head -n 1 | awk '{print "The smallest genome is in \"" $2 "\": " $1}'
## THIS CODE WILL DO THE SAME AS THE ONE BEFORE WITH THE DIFFERENCE THAT NOW I USE THE tail. tail WILL GIVE ME THE SMALLEST VALUE OF THE CHARACTERS IN THE GENOME. 
 
OUTPUT: The smallest genome is in "GCA_000008725.1_ASM872v1_genomic.fna": 1055551


4. 

## FIND THE NUMBER OF GENOMES WITH AT LEAST TWO “C” IN THE SPECIES NAME

[quezadgc@login509-02-r data]$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'grep -E "^>" "$1" | awk -F " " "{print \$2}" | grep -E "c.*c" | wc -l' _ {} \; | awk '{total += $1} END {print total}'
## grep IS TO SHOW A COUNT OF MATCHES.
OUTPUT: 14

## FIND THE NUMBER OF GENOMES WITH AT LEAST TWO “C” IN THE SPECIES NAME BUT WITHOUT THE WORD “COCCUS”

[quezadgc@login509-02-r data]$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'grep -E "^>" "$1" | awk -F " " "{print \$2}" | grep -E "c.*c" | grep -v "coccus" | wc -l' _ {} \; | awk '{total += $1} END {print total}'
OUTPUT: 4


5. 
## FIND THE NUMBER OF FILES LARGER THAN 3MB (-size  Finds files larger than 3MB and wc -l: Counts the number of lines in the output, giving you the total number of files found.)

[quezadgc@login509-02-r data]$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -size +3M | wc -l
OUTPUT: 6
