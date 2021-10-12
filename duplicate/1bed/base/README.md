Wrapper for KING --duplicate

```
rule KING_duplicate:
  input:  
    qbed="{dataset}.bed"
  output:
    "{prefix}.con"
  conda:  "../conda/env.yaml"
  wrapper:
    "https://changit.bwh.harvard.edu/resta/KING_Wrappers/tree/master/duplicate/1bed/base"
```
