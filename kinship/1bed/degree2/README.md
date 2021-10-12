Wrapper for KING --kinship --degree 2

```
rule KING_kinship2:
  input:  
    qbed="{dataset}.bed"
  output:
    # kin0="{dataset}.kin0",
    kin="{dataset}.kin",
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/kinship/1bed/degree2"
```
