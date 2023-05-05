# Getting started with single-cell genomics

```{article-info}
:date: May 31, 2021
:read-time: 5-10 min read
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

```{admonition} Update (May 4, 2023)
I now recommend the sc-best-practices [book](https://www.sc-best-practices.org/preamble.html) for a more comprehensive set of resources.
```

I started working with single-cell RNA-sequencing (scRNA-seq) data in 2016 during my Master's. As the field was rapidly proliferating at the time, there were a lack of resources available to quickly learn about how single-cell data are generated as well as best practices for how it should be analyzed. As single-cell genomics has become more routine, there are now so many resources that it can be hard to know where to start. Here I provide some of my favorite resources that I regularly share with undergraduates and new PhD students. This intentionally short list of resources is intended to quickly acclimate those with computational backgrounds; however, they are all of general interest. I will continue to update this post as new material becomes available. For a more comprehensive set of resources, I recommend [Ming Tang's](https://twitter.com/tangming2005) [analysis notes](https://github.com/crazyhottommy/scRNAseq-analysis-notes).

## Overview of single-cell genomics
These videos provide a high-level overview of many popular biological questions that can be answered with single-cell data, as well as some description of the underlying technologies.

### Videos


<div class="responsive-youtube">
<iframe width="560" height="315" src="https://www.youtube.com/embed/PRjX3-m16cw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<br>
<div class="responsive-youtube">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Mt1BbuW75qc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This last video is from the [Stat 115](https://canvas.harvard.edu/courses/39391) course at Harvard, which is fully available online, and goes more in depth with single-cell technologies.

<div class="responsive-youtube">
<iframe width="560" height="315" src="https://www.youtube.com/embed/PFG_SKpM5OI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


### Papers

- Wagner, A., Regev, A., & Yosef, N. (2016). Revealing the vectors of cellular identity with single-cell genomics. Nature biotechnology, 34(11), 1145-1160. [[Paper]](https://www.nature.com/articles/nbt.3711)
- Regev, A., Teichmann, S. A., Lander, E. S., Amit, I., Benoist, C., Birney, E., ... & Yosef, N. (2017). Science forum: the human cell atlas. Elife, 6, e27041. [[Paper]](https://elifesciences.org/articles/27041)

## Data analysis

The development of computational methods for single-cell genomics data has become very popular in the computational biology/applied stats/applied machine learning fields. In fact, there are about two new scRNA-seq computational methods for every three studies (with new data) published ([source](https://twitter.com/sinabooeshaghi/status/1357434610750136321?s=20)). These methods [overwhelmingly](https://www.scrna-tools.org/analysis) target a core set of tasks, and most are designed to handle the technical characteristics of these data.

### Papers

- Luecken, M. D., & Theis, F. J. (2019). Current best practices in single‐cell RNA‐seq analysis: a tutorial. Molecular systems biology, 15(6), e8746. [[Paper]](https://www.embopress.org/doi/full/10.15252/msb.20188746)
- Lähnemann, D., Köster, J., Szczurek, E., McCarthy, D. J., Hicks, S. C., Robinson, M. D., ... & Schönhuth, A. (2020). Eleven grand challenges in single-cell data science. Genome biology, 21(1), 1-35. [[Paper]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-1926-6)
- Amezquita, R. A., Lun, A. T., Becht, E., Carey, V. J., Carpp, L. N., Geistlinger, L., ... & Hicks, S. C. (2020). Orchestrating single-cell analysis with Bioconductor. Nature methods, 17(2), 137-145. [[Paper]](https://www.nature.com/articles/s41592-019-0654-x) [[Online book]](https://bioconductor.org/books/release/OSCA/) (*caveat: I would first focus on the motivation sections and not the code sections of the online book.*)

### Software and tutorials

A lot of high quality open-source software has been developed just for single-cell data analysis. I am biased as I mostly use Python and therefore only present Python packages here. I assume that R is the more popular language for single-cell data analysis due to [Seurat](https://satijalab.org/seurat/); however, given the power of Python-based machine learning frameworks like [PyTorch](https://pytorch.org/), [Jax](https://github.com/google/jax), and [Tensorflow](https://www.tensorflow.org/), along with datasets that regularly approach >100,000 cells, I believe Python has a brighter future in the field. That said, for now, many common analyses can be done with either language, though certain tasks may require language-specific packages. Therefore, it's also beneficial to understand popular data structures in both languages and how to convert between them (perhaps described in another tutorial). Also, in Python, all packages use the cell by genes orientation for the data, while in R it's genes by cells.

- [Scanpy](https://scanpy.readthedocs.io/en/stable/) and its [basic tutorial](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html). Scanpy underlies most Python-based single-cell analyses and for good reason. It uses the [AnnData](https://anndata.readthedocs.io/en/latest/) data structure for storing the data, which has become the most widely accepted input to other Python-based methods. It also provides nice plotting functions for exploratory analysis. Familiarity with the Scanpy workflow is essential.
- [scvi-tools](https://scvi-tools.org/), which I help develop, provides access to [many](https://scvi-tools.org/get_started#single-cell-omics-data-analysis) popular probabilistic models for single-cell genomics as well as an interface to build novel probabilistic/deep learning models using [PyTorch](https://pytorch.org/), [PyTorch Lightning](https://www.pytorchlightning.ai/), and [Pyro](https://pyro.ai/). I present a Scanpy/scvi-tools tutorial [here](https://ccbskillssem.github.io/pages/scanpy_scvi_tools/), with corresponding [video](https://youtu.be/EKTg9NV5hEA).
- [cellxgene](https://chanzuckerberg.github.io/cellxgene/) for interactive visualization.

## Tips and other considerations

- It's ok to be confused
- There's not always a good reason for why things are done the way they are (and this can make a good research direction!)
- While these resources represent a starting point, it's important to read publications that apply these computational techniques and technologies. At first, the papers will contain jargon that does not make sense, and that's ok.