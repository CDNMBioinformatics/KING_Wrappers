Wrapper for KING --related --degree 2

```
rule KING_related2:
  input:  
    qbed="{dataset}.bed"
    rbed="{reference}.bed"
  output:
    # kin0="{dataset}.kin0",
    kin="{dataset}.kin",
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/related/2bed/degree2"
```
