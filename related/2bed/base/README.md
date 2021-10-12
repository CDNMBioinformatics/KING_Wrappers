Wrapper for KING --related

```
rule KING_related:
  input:  
    qbed="{dataset}.bed"
    rbed="{reference}.bed"
  output:
    # kin0="{dataset}.kin0",
    kin="{dataset}.kin",
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/related/2bed/base"
```
