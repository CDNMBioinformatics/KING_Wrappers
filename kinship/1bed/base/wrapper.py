import os
from snakemake.shell import shell

# prefix = os.path.splitext(snakemake.output[0])[0]

shell("king -b {snakemake.input.qbed} --fam {snakemake.input.qfam} --kinship --prefix {snakemake.params.prefix}")


