Wrapper for KING --ibdseg --degree 3

```
rule KING_ibdseg:
  input:  
    qbed="{dataset}.bed"
  output:
    seg="{prefix}.seg",
    segments="{prefix}.segments.gz",
    splitped="{prefix}splitped.txt",
    allseg="{prefix}allsegs.txt"
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/ibdseg/1bed/base"
```
