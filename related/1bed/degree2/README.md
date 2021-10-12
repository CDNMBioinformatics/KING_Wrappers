Wrapper for KING --related --degree 2

```
rule KING_related2:
  input:  
    qbed="{dataset}.bed"
  output:
    # kin0="{dataset}.kin0",
    kin="{dataset}.kin",
  conda:  "../conda/env.yaml"
  wrapper:
    "https://changit.bwh.harvard.edu/resta/KING_Wrappers/tree/master/related/1bed/degree2"
```
