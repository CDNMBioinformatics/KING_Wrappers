Wrapper for KING --duplicate

```
rule KING_duplicate:
  input:  
    qbed="{dataset}.bed"
    rbed="{reference}.bed"
  output:
    "{prefix}.con"
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/duplicate/2bed/base"
```
