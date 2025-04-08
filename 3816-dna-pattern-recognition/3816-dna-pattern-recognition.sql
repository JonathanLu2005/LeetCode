# Write your MySQL query statement below

# sample id, dna sequence, species

# return it with new columns on its dna sequence
# has_start = start with atg
# has_stop = stop with taa, tag, tga
# has_atat = has atat
# has_ggg = has ggg or more

select *,
    dna_sequence REGEXP '^ATG' as has_start,
    dna_sequence REGEXP 'TAA$|TAG$|TGA$' as has_stop,
    dna_sequence REGEXP 'ATAT' as has_atat,
    dna_sequence REGEXP 'GGG' as has_ggg
from samples
order by sample_id;