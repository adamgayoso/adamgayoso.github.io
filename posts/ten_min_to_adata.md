---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.1+dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 5, maybe 10 minutes to AnnData

```{article-info}
:date: November 13, 2021
:read-time: 5-10 min read
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

```{admonition} Update (May 4, 2023)
I now recommend the default AnnData [tutorial](https://anndata.readthedocs.io/en/latest/tutorials/notebooks/getting-started.html) and scverse [tutorial](https://scverse-tutorials.readthedocs.io/en/latest/notebooks/anndata_getting_started.html).
```


I regularly use [Scanpy](https://scanpy.readthedocs.io) to analyze single-cell genomics data.
Scanpy's functionality heavily depends on the data being stored in an [AnnData](https://anndata.readthedocs.io/en/latest/) object, which provides Scanpy a systematic way of storing and retrieving intermediate analysis results, like principal components scores, [UMAP](https://umap-learn.readthedocs.io/) embeddings, cluster labels, etc.
While the Scanpy documentation site has [tutorials](https://scanpy.readthedocs.io/en/stable/tutorials.html) covering common use cases, there remains a lack of tutorials for AnnData specifically. Here I cover the basics.

## Why AnnData?

AnnData ("Annotated Data") is specifically designed for tabular data. By this I mean that we have $N$ observations (typically cells), each of which can be represented as $d$-dimensional vectors, where each dimension corresponds to a variable or feature (typically a gene). Both the rows and columns of this $N \times d$ matrix are special in the sense that they are indexed. In scRNA-seq, each row corresponds to a cell with a barcode, and each column corresponds to one gene. Furthermore, for each cell and each gene we might have additional metadata, like (1) donor information for each cell, or (2) alternative gene symbols for each gene.
Finally, we might have other unstructured metadata like color palletes we are using for plotting.
Without going into every fancy Python-based data structure, you'll have to take my word that no other alternative really exists that:

1. Handles sparsity
1. Handles unstructured data
1. Handles observation- and feature-level metadata
1. Is user-friendly

## Initializing AnnData


<!-- Perhaps [xarray](https://xarray.pydata.org/en/stable/) is the closest in terms of functionality, -->

Let's start by building a basic AnnData object with some sparse count information, perhaps representing gene expression counts.

```{code-cell}
import anndata
import numpy as np
from scipy.sparse import csr_matrix
counts = csr_matrix(np.random.poisson(1, size=(100, 2000)))
adata = anndata.AnnData(counts)
adata
```

We see that AnnData provides a representation with summary stastics of the data The initial data we passed are accessible as a sparse matrix using `adata.X`.

```{code-cell}
adata.X
```

Now, we provide the index to both the `obs` and `var` axes using `.obs_names` (resp. `.var_names`).


```{code-cell}
adata.obs_names = [f"Cell_{i}" for i in range(adata.n_obs)]
adata.var_names = [f"Gene_{i}" for i in range(adata.n_vars)]
print(adata.obs_names[:10])
```

### Subsetting AnnData

These index values can be used to subset the AnnData, which provides a [view](https://falexwolf.de/blog/171223_AnnData_indexing_views_HDF5-backing/) of the AnnData object. We can imagine this to be useful to subset the AnnData to particular cell types or gene modules of interest. The rules for subsetting AnnData are quite similar to that of a Pandas DataFrame. You can use values in the `obs/var_names`, boolean masks, or cell index integers.

```{code-cell}
adata[["Cell_1", "Cell_10"], ["Gene_5", "Gene_1900"]]
```

## Adding aligned metadata

### Observation/Variable level
So we have the core of our object and now we'd like to add metadata at both the observation and variable levels. This is pretty simple with AnnData, both `adata.obs` and `adata.var` are Pandas DataFrames.

```{code-cell}
ct = np.random.choice(["B", "T", "Monocyte"], size=(adata.n_obs,))
adata.obs["cell_type"] = ct
adata.obs
```


We can also see now that the AnnData representation has been updated:
```{code-cell}
adata
```


### Subsetting using metadata

We can also subset the AnnData using these randomly generated cell types:

```{code-cell}
bdata = adata[adata.obs.cell_type == "B"]
bdata
```


## Observation/Variable level matrices

We might also have metadata at either level that has many dimensions to it, such as a UMAP embedding of the data. For this type of metadata, AnnData has the `.obsm/.varm` attributes. We use keys to identify the different matrices we insert. The restriction of `.obsm/.varm` are that `.obsm` matrices must length equal to the number of observations as `.n_obs` and `.varm` matrices must length equal to `.n_vars`. They can each independently have different number of dimensions.

Let's start with a randomly generated matrix that we can interpret as a UMAP embedding of the data we'd like to store, as well as some random gene-level metadata:
```{code-cell}
adata.obsm["X_umap"] = np.random.normal(0, 1, size=(adata.n_obs, 2))
adata.varm["gene_stuff"] = np.random.normal(0, 1, size=(adata.n_vars, 5))
adata.obsm
```

Again, the AnnData representation is updated.
```{code-cell}
adata
```

A few more notes about `.obsm/.varm`

1. The "array-like" metadata can originate from a Pandas DataFrame, scipy sparse matrix, or numpy dense array.
1. When using scanpy, their values (columns) are not easily plotted, where instead items from `.obs` are easily plotted on, e.g., UMAP plots.

## Unstructured metadata

AnnData has `.uns`, which allows for any unstructured metadata. This can be anything, like a list or a dictionary with some general information that was useful in the analysis of our data.

```{code-cell}
adata.uns["random"] = [1, 2, 3]
adata.uns
```

## Layers

Finally, we may have different forms of our original core data, perhaps one that is normalized and one that is not. These can be stored in different layers in AnnData. For example, let's log transform the original data and store it in a layer:

```{code-cell}
adata.layers["log_transformed"] = np.log1p(adata.X)
adata
```
### Outputting DataFrames

We can also ask AnnData to return us a DataFrame from one of the layers:

```{code-cell}
adata.to_df(layer="log_transformed").iloc[:, :5]
```


We see that the `.obs_names/.var_names` are used in the creation of this Pandas object.


## Wrapping up

AnnData has become the standard for single-cell analysis in Python and for good reason -- it's straightforward to use and faciliatates more reproducible analyses with it's key-based storage. It's even becoming easier to convert to the popular R-based formats for single-cell analysis. There is still a lot that I don't cover here. I do encourage looking through the AnnData [API docs](https://anndata.readthedocs.io/en/latest/) for more useful properties/methods.