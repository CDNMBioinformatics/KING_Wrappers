Wrapper for KING --ibs --degree 3

```
rule KING_ibs:
  input:  
    qbed="{dataset}.bed"
  output:
    kin0="{prefix}.kin0",
    kin="{prefix}.kin",
    allseg="{prefix}allsegs.txt"
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/ibs/1bed/base"
```
