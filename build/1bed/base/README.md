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
    "https://changit.bwh.harvard.edu/resta/KING_Wrappers/tree/master/build/1bed/base"
```
