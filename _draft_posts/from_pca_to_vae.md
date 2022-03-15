@def title = "From PCA to VAE"
@def date = Date(2020, 12, 06)
@def tags = ["syntax", "code"]
@def description = "The classical PCA and contemporary VAE are closely related. Here we dive into this connection."

## From PCA to VAE

[Principal components analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) (PCA) is a dimensionality reduction technique that aims to preserve variability in the data. A Variational Autoencoder (VAE) \citep{kingma2014} is a deep learning approach to, among other things, generate novel images of handwritten digits and [celebrities](https://github.com/yzwxx/vae-celebA). So how are these two models related?

### Exploration of PCA
<!-- https://www.cs.cmu.edu/~avrim/598/chap3only.pdf -->
To begin, let's explore PCA.
We assume we have a dataset $\mathcal{D} = \{x_i\}_{i=1}^N$, where $x_i \in \mathbb{R}^d$.
In the case of scRNA-seq data, each dimension would correspond to one gene.
For simplicity, we assume our data have been mean-centered, i.e., $\mathbb{E}[x_i] = 0$.
PCA learns a sequence of unit vectors such that:
<!-- We assume these data points were generated independently and identically from some distribution $p(x)$.  -->

1. The vectors are mutually orthogonal
2. The squared distance of points to lines in direction of vectors is minimzed

Let us unpack this. To find the first principal component, we solve the following optimization problem.

$$\min_{u: \|u\|_2 = 1} \frac{1}{N}\sum_{i=1}^N \|x_i - (u^\top x_i)u\|_2^2$$

Another interpretation of PCA is that it projects the data onto lines (components) such that the variance of the resulting projected points is maximized. To see this consider


<!-- 1. PCA is an autoencoder
2. PCA has a probabilistic analog
3. A few tweaks of pPCA leads to VAE -->

```python
code_test = 1
```


## References
\biblabel{kingma2014}{Kingma et al. (2014)}
Kingma, D. P., & Welling, M. (2014).
Auto-encoding variational bayes.
ICLR 2014