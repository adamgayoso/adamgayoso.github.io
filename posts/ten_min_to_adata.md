@def title = "5, maybe 10 minutes to AnnData"
@def date = Date(2021, 5, 31)
@def tags = ["syntax", "code"]
@def description = "A beginner's guide to the AnnData package for storage of single-cell omics data."

~~~
<h1>{{ title }}</h1>
~~~

\newcommand{\pycode}[2]{
```julia:!#1
#hideall
using PyCall
pyimport("sys")."stdout" = PyTextIO(stdout)
lines = replace("""!#2""", r"(^|\n)([^\n]+)\n?$" => s"\1res = \2")
py"""
$$lines
"""
results = py"res"
if ~isnothing(results)
    println(results)
end
```
```python
#2
```
}

\pycode{py1}{
import os # hide
output = "_assets/posts/ten_min_to_adata/code/" # hide
os.makedirs(output, exist_ok=True) # hide
}


<!-- pyimport_conda("anndata", "anndata", "conda-forge") -->


I regularly use [Scanpy](https://scanpy.readthedocs.io) to analyze single-cell genomics data.
Scanpy's functionality heavily depends on the data being stored in an [AnnData](https://anndata.readthedocs.io/en/latest/) object, which provides Scanpy a systematic way of storing and retrieving intermediate analysis results, like principal components scores, [UMAP](https://umap-learn.readthedocs.io/) embeddings, cluster labels, etc.
While the Scanpy documentation site has [tutorials](https://scanpy.readthedocs.io/en/stable/tutorials.html) covering common use cases, there remains a lack of tutorials for AnnData specifically. Here I cover the basics.

## Why AnnData?

AnnData ("Annotated Data") is specifically designed for tabular data. By this I mean that we have $N$ observations (typically cells), each of which can be represented as $d$-dimensional vectors, where each dimension corresponds to a variable or feature (typically a gene). Both the rows and columns of this $N \times d$ matrix are special in the sense that they are indexed. In scRNA-seq, each row corresponds to a cell with a barcode, and each column corresponds to one gene. Furthermore, for each cell and each gene we might have additional metadata, like donor information for each cell or alternative gene symbols for each gene.
Finally, we might have other unstructured metadata like miscellaneous arrays that are used to analyze the dataset.
Without going into every fancy Python-based data structure, you'll have to take my word that no other alternative really exists that:

1. Handles sparsity
1. Handles unstructured data
1. Handles observation- and feature-level metadata
1. Is user-friendly

Perhaps [xarray](https://xarray.pydata.org/en/stable/) is the closest in terms of functionality,

\pycode{py1}{
import anndata
import numpy as np
counts = np.random.poisson(1, size=(100, 2000))
adata = anndata.AnnData(counts)
df = adata.to_df()
print(df)
}
\codeoutput{py1}

\pycode{py1}{
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter([0, 1], [1, 0], c="blue")
fig.savefig(os.path.join(output, "test.svg"), transparent=True) # hide
}

\fig{test}

~~~
<hr>
~~~
