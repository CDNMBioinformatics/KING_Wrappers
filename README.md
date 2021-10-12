# KING_Wrappers
snakemake wrappers for using KING (http://people.virginia.edu/~wc9c/KING/)

Available Relationship Inference Options
1) kinship
   - Estimates pair-wise kinship coefficients.
   - Unrelated individuals are treated as a family of size one.
   - If the datasets only consist of unrelated individuals as reported, then all results are saved in the between-family output.
   - If each FID is unique and no pedigrees are provided, within-family inference will be skipped.
   - Kinship relationship ranges:
     - > 0.354: duplicate/MZ twin
     - [0.177, 0.354]: 1st-degree relationship
     - [0.0884, 0.177]: 2nd-degree relationship
     - [0.0422, 0.0884]: 3rd-degree relationship
     - < 0: unrelated
   - Output for within-family relationship (king.kin) contains:
     - FID: Family ID for the pair
     - ID1: Individual ID for the first individual of the pair
     - ID2: Individual ID for the second individual of the pair
     - N_SNP: The number of SNPs that do not have missing genotypes in either of the individuals
     - Z0: Pr(IBD=0) as specified by the provided pedigree data
     - Phi: Kinship coefficient as specified by the provided pedigree data
     - HetHet: Proportion of SNPs with double heterozygotes (eg AG and AG)
     - IBS0: Porportion of SNPs with zero IBS (identical-by-state) (eg AA and GG)
     - Kinship: Estimated kinship coefficient from the SNP data
     - Error: Flag indicating differences between the estimated and specifed kinship coefficients (1 for error, 0.5 for warning)
   - Output for across-family (if pedigrees exist) or between-individuals (when no pedigrees are documented) relationship (king.kin0) contains:
     - FID1: Family ID for first individual of the pair
     - ID1: Individual ID for first individual of the pair
     - FID2: Family ID for the second individual of the pair
     - ID2: Individual ID for second individual of the pair
     - N_SNP: The number of SNPs that do not have missing genotypes in either of the individuals
     - HetHet: Proportion of SNPs with double heterozygotes (eg AG and AG)
     - IBS0: Porportion of SNPs with zero IBS (identical-by-state) (eg AA and GG)
     - Kinship: Estimated kinship coefficient from the SNP data
2) kinship2
   - Estimates pair-wise kinship coefficients using a 2nd-degree of relatedness filter (i.e. only relative pairs with larger kinship coefficients are included in the inference results).
   - Speeds up kinship computing without sacrifying inference accuracy (Only pairs with kinship coefficient > 0.0884 are saved in the king.kin0 output file)
3) ibdseg
   - Carries out IBD segment analysis, which determines all IBD (IBD1 and IBD2) segements shared between relatives from which relatedness can be inferred.
   - Summary of IBD segments (ex.seg) contains:
     - FID1: Family ID for the first individual of the pair
     - ID1: Individual ID for the first individual of the pair
     - FID2: Family ID for the second individual of the pair
     - ID2: Individual ID for the second individual of the pair
     - IBD1Seg: Total length of IBD1 segments divided by total length of all segments, estimate of π1=Pr(IBD=1)
     - IBD2Seg: Total length of IBD2 segments divided by total length of all segments, estimate of π2=Pr(IBD=2)
     - PropIBD: Proportion of genomes shared identical-by-descent, estimated by IBD2Seg + IBD1Seg/2, estimate of π=π2+π1/2
     - InfType: Inferred relationship type, such as Dup/MZTwin, PO, FS, 2nd, 3rd, 4th, UN
   - Detailed IBD segments (ex.segments.gz) contains:
     - FID1: Family ID for the first individual of the pair
     - ID1: Individual ID for the first individual of the pair
     - FID2: Family ID for the second individual of the pair
     - ID2: Individual ID for the second individual of the pair
     - IBDType: Type of IBD segments: IBD1 or IBD2
     - Chr: Chromosome number.
     - StartMB: Start position of the IBD segment (in Mb)
     - StopMB: Stop position of the IBD segment (in Mb)
     - StartSNP: Start SNP of the IBD segment
     - StopSNP: Stop SNP of the IBD segment
     - N_SNP: The number of SNPs in the IBD segment
     - Length: Total Length of the IBD segment (in Mb) 
4) ibdseg3
   - Carries out IBD segment analysis using a 2nd-degree of relatedness filter.
   - Specifies only pairs with IBD proportion > 0.0884 will be saved in the output.
5) related
   - Provides integrative, fast, and accurate inference for close relationships.
   - This method integrates the IBD Segment algorithm with the Kinship algorithm.
   - This option is highly recomended especially when dealing with biobank-level datasets.
   - Identifes close relatives up to the first degree (i.e. is equivalent to using a --degree 1 filter) which only offers substantial computation aldvantes over identifying higer degree realtives
   - This is the recommended method over using --related --degree 2 or higher
   - Outputs for of relationship inference (king.kin and king.kin0) contain:
     - FID: Family ID for the pair
     - ID1: Individual ID for the first individual of the pair
     - ID2: Individual ID for the second individual of the pair
     - N_SNP: The number of SNPs that do not have missing genotypes in either of the individual
     - Z0: Pr(IBD=0) as specified by the provided pedigree data
     - Phi: Kinship coefficient as specified by the provided pedigree data
     - HetHet: Proportion of SNPs with double heterozygotes (e.g., AG and AG)
     - IBS0: Porportion of SNPs with zero IBS (identical-by-state) (e.g., AA and GG)
     - Kinship: Estimated kinship coefficient (φ) from the SNP data
     - IBD1Seg: Total length of IBD1 segments divided by total length of all segments, estimate of π1=Pr(IBD=1)
     - IBD2Seg: Total length of IBD2 segments divided by total length of all segments, estimate of π2=Pr(IBD=2)
     - PropIBD: Proportion of genomes shared identical-by-descent, estimated by IBD2Seg + IBD1Seg/2, estimate of π=π2+π1/2
     - InfType: Inferred relationship type, such as Dup/MZTwin, PO, FS, 2nd, 3rd, 4th, UN
     - Error: Flag Indicating differences between inferred and reported relationship (1 for error, 0.5 for warning)
6) related2
   - Provides integrative, fast, and accurate inference for close relationships using a 2nd-degree of relatedness filter (specifically, all pairs across families with a kinship coefficient less than 0.0884 will be excluded from the output).
7) ibs
   - Provides summary statistics such as the counts of IBS0, IBS1, IBS2, the average IBS, in additional to the kinship estimates.
   - Outputs for relationship inference (kin.ibs and ibs0)
8) homog
   - Estimates pair-wise kinship coefficients assuming a homogeneous population.
   - The best application may be for linear mixed models where the population structure information needs to be explicity incorporated in the kinship coefficient estimation. 
   - Not recommended as a good method to infer relatedness in general populations
   - Outputs for relationship inference (king.kin and king.kin0) contain:
     - FID: Family ID for the pair
     - ID1: Individual ID for the first individiual of the pair
     - ID2: Individual ID for the second individual of the pair
     - N_SNP: The number of SNPs that do not have missing genotypes in either of the individual
     - Z0: Pr(IBD=0) as specified by the provided pedigree data
     - Phi: Kinship coefficient as specified by the provided pedigree data
     - IBD0: Proportion of SNPs with 0 IBD
     - IBD1: Proportion of SNPs with 1 IBD
     - IBD2: Proportion of SNPs with 2 IBD
     - Kinship: Estimated kinship coefficient (φ) from the SNP data
     - Error: Flag Indicating differences between inferred and reported relationship (1 for error, 0.5 for warning)
9) duplicate
   - Implements the fastest (and accurate) algorithm to identify duplicates of MZ twins.
   - If duplicates exist, duplicates are written to kin.con.
     - This wrapper creates an empty kin.con file if no duplicates are found so that snakemake can continue.
10) build
    - Reconstructs pedigrees using SNP data without the need of specifying pedigrees (although it can still be incorporated).
    - Output includes two main files: kinupdateids.txt and kingupdateparents.txt
    - Output includes two additional informational files: kinallsegs.txt and kinbuild.log
