import os
from snakemake.shell import shell

# prefix = os.path.splitext(snakemake.output[0])[0]

shell("king -b {snakemake.input.qbed} --duplicate --prefix {snakemake.params.prefix}")
shell("[-f {snakemake.params.prefix}.con] && {echo "Duplicates Found"} || {echo "No Duplicates Found. Creating Blank File"; echo -e "FID1\tID1\tFID2\tID2\tN\tN_IBS0\tN_IBS1\tN_IBS2\tConcord\tHomConc\tHetConc" > {snakemake.params.prefix}.con}")


