Wrapper for KING --homog

```
rule KING_homog:
  input:  
    qbed="{dataset}.bed"
  output:
    # kin0="{dataset}.kin0",
    kin="{dataset}.kin",
  conda:  "../conda/env.yaml"
  wrapper:
    "https://changit.bwh.harvard.edu/resta/KING_Wrappers/tree/master/homog/1bed/base"
```