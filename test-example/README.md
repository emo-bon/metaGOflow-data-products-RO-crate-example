# Test example of Data Products RO-Crate

Workflow execution:
CWLtool
all steps
HWLTKDRXY.UDI210 data
HWLTKDRXY.UDI210-results.tar.bz2 results tarball

conda activate metaGOflow
export DATA_FORWARD="DBB_AAADOSDA_1_1_HWLTKDRXY.UDI210_clean.fastq.gz"
export DATA_REVERSE="DBB_AAADOSDA_1_2_HWLTKDRXY.UDI210_clean.fastq.gz"
./run_wf.sh -n run -d  HWLTKDRXY.UDI210 \
-f input_data/${DATA_FORWARD} \
-r input_data/${DATA_REVERSE}

cwltool --debug ${SINGULARITY} --outdir ${OUT_DIR_FINAL} ${CWL} ${RENAMED_YML}

```
$ tree
.
├── DBB_AAADOSDA_1_1_HWLTKDRXY.UDI210_clean 
│   ├── GC-distribution.out.sub-set > discard
│   ├── GC-distribution.out.sub-set_bin > discard
│   ├── GC-distribution.out.sub-set_pcbin > discard
│   ├── nucleotide-distribution.out.sub-set > discard
│   ├── seq-length.out.sub-set > discard
│   ├── seq-length.out.sub-set_bin > discard
│   ├── seq-length.out.sub-set_pcbin > discard
│   └── summary.out > discard
├── DBB_AAADOSDA_1_1_HWLTKDRXY.UDI210_clean.fastq.gz.sha1 > discard
├── DBB_AAADOSDA_1_1_HWLTKDRXY.UDI210_clean.fastq.trimmed.fasta > SeqDataRO ?
├── DBB_AAADOSDA_1_2_HWLTKDRXY.UDI210_clean 
│   ├── GC-distribution.out.sub-set > discard
│   ├── GC-distribution.out.sub-set_bin > discard
│   ├── GC-distribution.out.sub-set_pcbin > discard
│   ├── nucleotide-distribution.out.sub-set > discard
│   ├── seq-length.out.sub-set > discard
│   ├── seq-length.out.sub-set_bin > disacard
│   ├── seq-length.out.sub-set_pcbin > discard
│   └── summary.out > discard
├── DBB_AAADOSDA_1_2_HWLTKDRXY.UDI210_clean.fastq.gz.sha1 > discard
├── DBB_AAADOSDA_1_2_HWLTKDRXY.UDI210_clean.fastq.trimmed.fasta > SeqDataRO ?
├── DBB.merged_CDS.faa > Unknown
├── DBB.merged_CDS.ffn > Unknown
├── DBB.merged.cmsearch.all.tblout.deoverlapped > discard
├── DBB.merged.fasta  > SeqData RO
├── DBB.merged.motus.tsv > discard
├── DBB.merged.unfiltered_fasta > discard
├── fastp.html > SeqData RO
├── final.contigs.fa > Unknown (either SeqData ROC or DataProducts ROC)
├── functional-annotation > include
│   ├── DBB.merged_CDS.I5.tsv.chunks > discard
│   ├── DBB.merged_CDS.I5.tsv.gz > include
│   ├── DBB.merged.hmm.tsv.chunks > discard
│   ├── DBB.merged.hmm.tsv.gz > include
│   ├── DBB.merged.summary.go > include
│   ├── DBB.merged.summary.go_slim > include
│   ├── DBB.merged.summary.ips > include
│   ├── DBB.merged.summary.ko > include
│   ├── DBB.merged.summary.pfam > include
│   ├── stats > include
│   │   ├── go.stats > include
│   │   ├── interproscan.stats > include
│   │   ├── ko.stats > include
│   │   ├── orf.stats > include
│   │   └── pfam.stats > include
│   └── temp > discard
├── merged_qc > SeqData RO
│   ├── GC-distribution.out.sub-set > SeqData RO
│   ├── GC-distribution.out.sub-set_bin > SeqData RO
│   ├── GC-distribution.out.sub-set_pcbin > SeqData RO
│   ├── nucleotide-distribution.out.sub-set > SeqData RO
│   ├── seq-length.out.sub-set > SeqData RO
│   ├── seq-length.out.sub-set_bin > SeqData RO
│   ├── seq-length.out.sub-set_pcbin > SeqData RO
│   └── summary.out
├── qc_summary > discard
├── qc_summary_2 > discard
├── RNA-counts > include
├── sequence-categorisation
│   ├── 5_8S.fa.gz > include
│   ├── alpha_tmRNA.RF01849.fasta.gz > include
│   ├── Bacteria_large_SRP.RF01854.fasta.gz > include
│   ├── Bacteria_small_SRP.RF00169.fasta.gz > include
│   ├── cyano_tmRNA.RF01851.fasta.gz > include
│   ├── LSU.fasta.chunks > discard
│   ├── LSU.fasta.gz > include
│   ├── LSU_rRNA_archaea.RF02540.fa.gz > include
│   ├── LSU_rRNA_bacteria.RF02541.fa.gz > include
│   ├── LSU_rRNA_eukarya.RF02543.fa.gz > include
│   ├── Metazoa_SRP.RF00017.fasta.gz > include
│   ├── Protozoa_SRP.RF01856.fasta.gz > include
│   ├── RNase_MRP.RF00030.fasta.gz > include
│   ├── RNaseP_bact_a.RF00010.fasta.gz > include
│   ├── RNaseP_nuc.RF00009.fasta.gz > include
│   ├── SSU.fasta.chunks > discard
│   ├── SSU.fasta.gz > include
│   ├── SSU_rRNA_archaea.RF01959.fa.gz > include
│   ├── SSU_rRNA_bacteria.RF00177.fa.gz > include
│   ├── SSU_rRNA_eukarya.RF01960.fa.gz > include
│   ├── tmRNA.RF00023.fasta.gz > include
│   ├── tRNA.RF00005.fasta.gz > include
│   └── tRNA-Sec.RF01852.fasta.gz > include
└── taxonomy-summary
    ├── LSU
    │   ├── DBB.merged_LSU.fasta.mseq.gz
    │   ├── DBB.merged_LSU.fasta.mseq_hdf5.biom
    │   ├── DBB.merged_LSU.fasta.mseq_json.biom
    │   ├── DBB.merged_LSU.fasta.mseq.tsv
    │   ├── DBB.merged_LSU.fasta.mseq.txt
    │   └── krona.html
    └── SSU
        ├── DBB.merged_SSU.fasta.mseq.gz
        ├── DBB.merged_SSU.fasta.mseq_hdf5.biom
        ├── DBB.merged_SSU.fasta.mseq_json.biom
        ├── DBB.merged_SSU.fasta.mseq.tsv
        ├── DBB.merged_SSU.fasta.mseq.txt
        └── krona.html

10 directories, 88 files

```

```
$ du -hs ./*
14G	./HWLTKDRXY.UDI210-results.tar.bz2
4.0K	./prov
54G	./results
12K	./run.yml
1.8T	./tmp
```

Intermediate files:
    a) cleaned, trimmed, reads in uncompressed fasta file for each direction:
    DBB_AAADOSDA_1_1_HWLTKDRXY.UDI210_clean.fastq.trimmed.fasta
    DBB_AAADOSDA_1_2_HWLTKDRXY.UDI210_clean.fastq.trimmed.fasta
    2.3GB each

    b) merged reads, unfiltered in uncompressed fastq
    DBB.merged.unfiltered_fasta
    21G

    b) Merged reads in uncompressed fasta - these should be published
    as they are the data the taxonomic inventories and functional
    annotations are done on.
    DBB.merged.fasta
    12G

    d) Merged coding nucleotide sequences in uncompressed fasta
    DBB.merged_CDS.ffn
    4.9G

    e) Merged coding peptide sequences in uncompressed fasta
    DBB.merged_CDS.faa
    4.9G

    f) MegaHit assembled contigs uncompressed fasta
    Do we even want to calculate these? I think so, for F-E
    final.contigs.fa
    123M
