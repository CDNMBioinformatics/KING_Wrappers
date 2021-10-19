import os
from snakemake.shell import shell

# prefix = os.path.splitext(snakemake.output[0])[0]

shell("king -b {snakemake.input.qbed},{snakemake.input.rbed} --fam {snakemake.input.qfam},{snakemake.input.rfam} --kinship --prefix {snakemake.params.prefix}")


