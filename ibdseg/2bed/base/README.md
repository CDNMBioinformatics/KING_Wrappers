Wrapper for KING --ibdseg

```
rule KING_ibdseg:
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
    "https://changit.bwh.harvard.edu/resta/KING_Wrappers/tree/master/ibdseg/2bed/base"
```
