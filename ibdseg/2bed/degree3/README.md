Wrapper for KING --ibdseg

```
rule KING_ibdseg3:
  input:  
    qbed="{dataset}.bed"
    rbed="{reference}.bed"
  output:
    seg="{prefix}.seg",
    segments="{prefix}.segments.gz",
    splitped="{prefix}splitped.txt",
    allseg="{prefix}allsegs.txt"
  conda:  "../conda/env.yaml"
  wrapper:
    "https://github.com/CDNMBioinformatics/KING_Wrappers/tree/main/ibdseg/2bed/degree3"
```
