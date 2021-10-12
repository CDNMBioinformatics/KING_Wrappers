Wrapper for KING --build

```
rule KING_build:
  input:  
    qbed="{dataset}.bed"
  output:
    "{prefix}updateids.txt"
    "{prefix}updateparents.txt"
    "{prefix}allsegs.txt"
    "{prefix}build.log"
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/build/2bed/base"
```
