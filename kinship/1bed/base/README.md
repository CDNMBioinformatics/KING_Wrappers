Wrapper for KING --kinship

```
rule KING_kinship:
  input:  
    qbed="{dataset}.bed"
  output:
    # kin0="{dataset}.kin0",
    kin="{dataset}.kin",
  conda:  "../conda/env.yaml"
  wrapper:
    "https://changit.bwh.harvard.edu/resta/KING_Wrappers/tree/master/kinship/1bed/base"
```
