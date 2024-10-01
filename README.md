### WEEK 3
## 1. Write the README
```bash
% scp ~/Downloads/Bioinformatic/bacterial_dataset.zip quezadgc@ilogin.ibex.kaust.edu.sa:~/
% quezadgc@ilogin.ibex.kaust.edu.sa's password:
OUTPUT: bacterial_dataset.zip 100% 16MB 14.0MB/s 00:01  
```
## 2. Uncompress the zip file on IBEX
``` bash
$ unzip bacterial_dataset.zip 
```
## 3. 
### PRINT THE LARGEST GENOME
``` bash
$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'echo "$(tail -n +2 "$1" | wc -c) $(basename "$1")"' _ {} \; | sort -n | tail -n 1 | awk '{print "The largest genome is in \"" $2 "\": " $1}'
```
THIS CODE WILL SCAN ALL THE .fna FILES IN THE GIVEN DIRECTORY. Exec IS TO EXECUTE THE COMMAND IN EACH FILE. tail IS TO OUTPUT THE CONTENT OF THE FILES EXCLUDING THE FIRST LINE WHICH IS THE TITLE. wc -c IS TO COUNT THE NUMBER OF CHARACTERS IN EACH FILE. Sort TO LIST IN ASCENDING ORDER, WITH THE LARGEST GENOME AT THE BOTTOM. tail TO EXTRACT THE LAST LINE OF THE LIST. echo IS TO PRINT THE OUTPUT (FILE NAME AND NUMBER OF CHARACTERS IN GENOME). 

OUTPUT: The largest genome is in "GCF_000006745.1_ASM674v1_genomic.fna": 4083974


### PRINT THE SMALLEST GENOME
``` bash
$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'echo "$(tail -n +2 "$1" | wc -c) $(basename "$1")"' _ {} \; | sort -n | head -n 1 | awk '{print "The smallest genome is in \"" $2 "\": " $1}'
```
THIS CODE WILL DO THE SAME AS THE ONE BEFORE WITH THE DIFFERENCE THAT NOW I USE THE head THAT WILL GIVE ME THE SMALLEST VALUE OF THE CHARACTERS IN THE LIST. 
 
OUTPUT: The smallest genome is in "GCA_000008725.1_ASM872v1_genomic.fna": 1055551


## 4. 

### FIND THE NUMBER OF GENOMES WITH AT LEAST TWO “C” IN THE SPECIES NAME
``` bash
$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'grep -E "^>" "$1" | awk -F " " "{print \$2}" | grep -E "c.*c" | wc -l' _ {} \; | awk '{total += $1} END {print total}'
```
grep IS TO SEARCH SOMETHING.

OUTPUT: 14

### FIND THE NUMBER OF GENOMES WITH AT LEAST TWO “C” IN THE SPECIES NAME BUT WITHOUT THE WORD “COCCUS”

``` bash
$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -exec sh -c 'grep -E "^>" "$1" | awk -F " " "{print \$2}" | grep -E "c.*c" | grep -v "coccus" | wc -l' _ {} \; | awk '{total += $1} END {print total}'
```
OUTPUT: 4


## 5. FIND THE NUMBER OF FILES LARGER THAN 3MB (-size  Finds files larger than 3MB and wc -l: Counts the number of lines in the output, giving you the total number of files found.)

``` bash
$ find /home/quezadgc/ncbi_dataset/data -type f -name "*.fna" -size +3M | wc -l
```
OUTPUT: 6
