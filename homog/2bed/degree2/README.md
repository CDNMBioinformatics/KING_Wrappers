Wrapper for KING --homog --degree 2

```
rule KING_homog2:
  input:  
    qbed="{dataset}.bed"
    rbed="{reference}.bed"
  output:
    # kin0="{dataset}.kin0",
    kin="{dataset}.kin",
  conda:  "../conda/env.yaml"
  wrapper:
    "https://changit.bwh.harvard.edu/resta/KING_Wrappers/tree/master/homog/2bed/degree2"
```
