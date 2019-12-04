#!/usr/bin/env python
# The purpose of this script is to parse the most relevant columns from Bystro output

def main():
    import re
    import sys
    #print(sys.version)
    
    
    #----------------------
    # Get the file names
    #----------------------
    infilename = input('Enter input filename: ')
    outfilename = input('Enter output filename: ')
    
    #----------------------
    # Open the files
    #----------------------
    infile = open(infilename,'r')
    outfile = open(outfilename,'w')

    #----------------------
    #Print column titles
    #----------------------
    print('Chromosome\t', 'Position\t', 'Type\t', 'phastCons\t', 'phyloP\t', 'cadd\t', 'dbSNP.name\t', 'dbSNP.func\t', 'gnomad.genomes.id\t', 'gnomad.genomes.af\t', 'refSeq.siteType\t', 'refSeq.exonicAllelefunction\t', 'refSeq.name\t', 'refSeq.name2\t', 'refSeq.description\t', file=outfile)
    #Labels 'refSeq.siteType', 'refSeq.exonicAlleleFunction', 'refSeq.description', 'refSeq.name', 'refSeq.name2', 'phyloP', 'CADD', 'dbSNP.name', 'dbSNP.func', 'gnomad.genomes.id', 'gnomad.genomes.af', 'gnomad.exomes.id', 'gnomad.exomes.af', 'refSeq.clinvar.alleleID', 'refSeq.clinvar.phenotypeList', 'refSeq.clinvar.clinicalSignificance'
    
    #----------------------
    # Process the input file
    #----------------------
    for line in infile:
    
        #----------------------
        #Ignore hypothesis line
        #----------------------
        m = re.match('Hypothesis', line)
        if m:
            #print(line)
            #print('Found the hypothesis line')
            continue
        
        #----------------------
        #Ignore header line
        #----------------------
        label = re.match('chrom', line)
        if label:
            continue
        
        #----------------------
        #Split input line
        #----------------------
        temp = line.split('\t')
        
        #----------------------
        # Process Gene Names contained in temp[33] - refSeq.name2
        #----------------------
        genename = temp[33]
        #print('The gene name is:', genename)
        
        #Ignore lines that start with '!' - contain no gene name
        genetemp = re.match('\A!', genename)
        if genetemp:
            #print('Made it into first match')
            #print(genetemp)
            continue
        else:
            # Split array containing gene names - delimitated by ; or |
            #print('Made it into the second match')
            print('The gene name (in else) is', genename, file=outfile)
            # Get rid of | characters in string
            genestemp = genename.replace('|', ';')
            print('The genestemp after replace is', genestemp, file=outfile)
            genes = genestemp.split(';')
            print('The genes after split are', genes, file=outfile)
            geneset = set(genes)
            print('The genes after set are', geneset, file=outfile)
            #genetemp = str(genes)
            #print("The genetemp after turning into a string is", genetemp, file=outfile)
            #genesfinal = genetemp.split('\|')
            #print(genesfinal, file=outfile)
            # Identify unique gene names with set
            #gene_set = set(genes)
            #print(set(genesfinal), file=outfile)
        
        # Use gene names to find OMIM entries (for adjacent column)
        # Output unique gene names to single column - delimit by ;
        # Output OMIM information - delimit by ;
                
                
                
        #----------------------
        #Print desired columns from bystro
        #----------------------
        #print(line[:-1])

        #print(temp[0], '\t', temp[1], '\t', temp[2], '\t', temp[45], '\t', temp[46], '\t', temp[47], '\t', temp[48], '\t', temp[52], '\t', temp[66], '\t', temp[67], '\t', temp[16], '\t', temp[17], '\t', temp[32], '\t', temp[33], '\t', temp[30], '\t', file=outfile)
        # , temp[32], temp[33], temp[36], temp[37], temp[38], temp[88], temp[89] 
    # close both files
    infile.close()
    outfile.close()
    
main()
