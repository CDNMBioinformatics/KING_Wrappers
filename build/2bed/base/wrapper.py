# import os
from snakemake.shell import shell

# prefix = os.path.splitext(snakemake.output[0])[0]

shell("king -b {snakemake.input.qbed},{snakemake.input.rbed} --build --prefix {snakemake.params.prefix}")



