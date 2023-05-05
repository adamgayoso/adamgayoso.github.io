Search.setIndex({"docnames": ["README", "_draft_posts/from_pca_to_vae", "blog", "index", "posts/single_cell_resources", "posts/ten_min_to_adata", "publications"], "filenames": ["README.md", "_draft_posts/from_pca_to_vae.md", "blog.md", "index.md", "posts/single_cell_resources.md", "posts/ten_min_to_adata.md", "publications.md"], "titles": ["&lt;no title&gt;", "From PCA to VAE", "Blog", "&lt;no title&gt;", "Getting started with single-cell genomics", "5, maybe 10 minutes to AnnData", "Publications"], "terms": {"sphinx": 0, "autobuild": 0, "_build": 0, "html": 0, "def": 1, "titl": 1, "date": 1, "2020": [1, 4, 6], "12": 1, "06": 1, "tag": 1, "syntax": 1, "code": [1, 4], "descript": [1, 4], "The": [1, 4, 5, 6], "classic": 1, "contemporari": 1, "ar": [1, 2, 4, 5], "close": 1, "relat": 1, "here": [1, 4, 5], "we": [1, 5], "dive": 1, "thi": [1, 4, 5], "connect": 1, "princip": [1, 5], "compon": [1, 5], "analysi": [1, 3, 5, 6], "i": [1, 2, 3, 4, 5, 6], "dimension": [1, 5], "reduct": 1, "techniqu": [1, 4], "aim": 1, "preserv": 1, "variabl": 1, "data": [1, 2, 3, 5, 6], "A": [1, 2, 4, 5, 6], "variat": [1, 6], "autoencod": [1, 6], "citep": 1, "kingma2014": 1, "deep": [1, 3, 4, 6], "learn": [1, 3, 4, 6], "approach": [1, 4], "among": 1, "other": [1, 5], "thing": [1, 4], "gener": [1, 3, 4, 5, 6], "novel": [1, 4], "imag": 1, "handwritten": 1, "digit": 1, "celebr": 1, "so": [1, 4, 5], "how": [1, 4], "two": [1, 4], "model": [1, 3, 4, 6], "To": 1, "begin": 1, "let": [1, 5], "": [1, 2, 4, 5], "assum": [1, 4], "have": [1, 5], "dataset": [1, 4], "mathcal": 1, "d": [1, 4, 5, 6], "x_i": 1, "_": 1, "1": [1, 3, 4, 5], "n": [1, 4, 5], "where": [1, 3, 4, 5], "mathbb": 1, "r": [1, 4, 5], "In": [1, 4, 5], "case": [1, 5], "scrna": [1, 4, 5], "seq": [1, 4, 5, 6], "each": [1, 5], "dimens": [1, 5], "would": [1, 4], "correspond": [1, 4, 5], "one": [1, 5], "gene": [1, 4, 5, 6], "For": [1, 4, 5], "simplic": 1, "our": [1, 3, 5], "been": [1, 4, 5], "mean": [1, 5], "center": [1, 3], "e": [1, 4, 5], "0": [1, 5], "sequenc": [1, 3, 4], "unit": 1, "vector": [1, 4, 5], "mutual": 1, "orthogon": 1, "squar": 1, "distanc": 1, "point": [1, 4], "line": 1, "direct": [1, 4], "minimz": 1, "u": [1, 5], "unpack": 1, "find": 1, "first": [1, 4], "solv": 1, "follow": 1, "optim": 1, "problem": 1, "min_": 1, "_2": 1, "frac": 1, "sum_": 1, "top": 1, "2": [1, 3, 4, 5], "anoth": [1, 4], "interpret": [1, 5, 6], "project": [1, 6], "onto": 1, "varianc": 1, "result": [1, 5], "maxim": [1, 6], "see": [1, 5], "consid": 1, "code_test": 1, "biblabel": 1, "kingma": 1, "et": 1, "al": 1, "2014": 1, "p": 1, "well": [1, 4, 5], "m": [1, 3, 4], "auto": 1, "encod": 1, "bay": [1, 6], "iclr": 1, "5": [2, 4], "mayb": 2, "10": [2, 4], "minut": 2, "anndata": [2, 4], "2021": [2, 4, 5, 6], "11": [2, 4], "13": [2, 5], "beginn": 2, "guid": 2, "packag": [2, 3, 4], "storag": [2, 5], "singl": [2, 3, 5, 6], "cell": [2, 3, 5, 6], "omic": [2, 3, 6], "get": 2, "start": [2, 3, 5], "genom": [2, 5], "05": 2, "31": [2, 4], "new": [2, 3, 4], "These": [2, 4, 5], "resourc": [2, 4], "wish": 2, "had": 2, "when": [2, 5], "enter": 2, "field": [2, 4], "adam": [3, 6], "gayoso": [3, 6], "phd": [3, 4], "candid": 3, "comput": [3, 4, 6], "biologi": [3, 4, 6], "uc": 3, "berkelei": 3, "adamgayoso": 3, "dot": 3, "edu": 3, "about": [3, 4, 5], "summer": 3, "2023": [3, 6], "research": [3, 4], "scientist": 3, "googl": 3, "deepmind": 3, "current": [3, 4], "am": [3, 4], "co": 3, "advis": 3, "aaron": [3, 6], "street": [3, 6], "nir": [3, 6], "yosef": [3, 4, 6], "dure": [3, 4], "my": [3, 4, 5], "develop": [3, 4], "an": [3, 4, 5, 6], "express": [3, 5, 6], "represent": [3, 5], "facilit": 3, "common": [3, 4, 5], "task": [3, 4], "us": [3, 4], "refin": 3, "understand": [3, 4], "heterogen": [3, 6], "cd8": 3, "t": [3, 4, 5], "context": 3, "acut": 3, "infect": 3, "also": [3, 4, 5], "creator": 3, "scvi": [3, 4], "tool": [3, 4], "which": [3, 4, 5], "python": [3, 4, 5, 6], "provid": [3, 4, 5, 6], "access": [3, 4, 5, 6], "implement": 3, "state": 3, "art": 3, "probabilist": [3, 4, 6], "build": [3, 4, 5], "block": 3, "rapidli": [3, 4], "befor": 3, "receiv": 3, "b": [3, 5], "oper": 3, "engin": 3, "manag": 3, "system": [3, 4, 6], "scienc": [3, 4, 6], "from": [3, 4, 5], "columbia": 3, "univers": 3, "rna": [3, 4, 6], "dana": [3, 6], "pe": [3, 6], "er": [3, 6], "lab": 3, "min": [4, 5], "read": [4, 5], "now": [4, 5], "recommend": [4, 5], "sc": 4, "best": 4, "practic": 4, "book": 4, "more": [4, 5], "comprehens": 4, "set": 4, "work": 4, "2016": 4, "master": 4, "As": 4, "wa": [4, 5], "prolifer": 4, "time": [4, 5], "were": 4, "lack": [4, 5], "avail": 4, "quickli": 4, "should": 4, "analyz": [4, 5], "ha": [4, 5], "becom": [4, 5], "routin": 4, "mani": [4, 5], "can": [4, 5], "hard": 4, "know": 4, "some": [4, 5], "favorit": 4, "regularli": [4, 5], "share": 4, "undergradu": 4, "student": 4, "intention": 4, "short": 4, "list": [4, 5], "intend": 4, "acclim": 4, "those": 4, "background": 4, "howev": 4, "thei": [4, 5, 6], "all": 4, "interest": [4, 5], "continu": 4, "post": 4, "materi": 4, "ming": 4, "tang": 4, "note": [4, 5], "high": [4, 6], "level": [4, 6], "popular": [4, 5], "biolog": 4, "question": 4, "answer": 4, "underli": 4, "technologi": 4, "last": 4, "stat": 4, "115": 4, "cours": 4, "harvard": 4, "fulli": 4, "onlin": 4, "goe": 4, "depth": 4, "wagner": 4, "regev": [4, 6], "reveal": 4, "cellular": 4, "ident": 4, "natur": [4, 6], "biotechnologi": [4, 6], "34": 4, "1145": 4, "1160": 4, "teichmann": [4, 6], "lander": 4, "amit": 4, "benoist": 4, "c": 4, "birnei": 4, "2017": 4, "forum": 4, "human": [4, 6], "atla": [4, 6], "elif": 4, "6": 4, "e27041": 4, "method": [4, 5, 6], "veri": 4, "appli": 4, "machin": [4, 6], "fact": 4, "everi": [4, 5], "three": 4, "studi": 4, "publish": 4, "sourc": 4, "overwhelmingli": 4, "target": 4, "core": [4, 5], "most": 4, "design": [4, 5], "handl": [4, 5], "technic": 4, "characterist": 4, "luecken": [4, 6], "f": [4, 5, 6], "j": [4, 6], "2019": [4, 6], "molecular": [4, 6], "15": 4, "e8746": 4, "l\u00e4hnemann": 4, "k\u00f6ster": 4, "szczurek": 4, "mccarthi": 4, "hick": 4, "robinson": 4, "sch\u00f6nhuth": 4, "eleven": 4, "grand": 4, "challeng": 4, "21": 4, "35": 4, "amezquita": 4, "lun": 4, "becht": 4, "carei": 4, "v": [4, 6], "carpp": 4, "l": [4, 6], "geistling": 4, "orchestr": 4, "bioconductor": 4, "17": 4, "137": 4, "145": 4, "caveat": 4, "focu": 4, "motiv": 4, "section": 4, "lot": [4, 5], "qualiti": 4, "open": 4, "just": 4, "bias": 4, "mostli": 4, "therefor": 4, "onli": 4, "present": [4, 6], "languag": 4, "due": 4, "seurat": 4, "given": 4, "power": 4, "base": [4, 5], "framework": 4, "like": [4, 5], "pytorch": 4, "jax": 4, "tensorflow": 4, "along": 4, "100": [4, 5], "000": 4, "believ": 4, "brighter": 4, "futur": 4, "That": 4, "said": 4, "analys": [4, 5], "done": 4, "either": [4, 5], "though": 4, "certain": 4, "requir": 4, "specif": [4, 5], "benefici": 4, "structur": [4, 5], "both": [4, 5], "convert": [4, 5], "between": 4, "them": 4, "perhap": [4, 5], "describ": 4, "orient": 4, "while": [4, 5], "scanpi": [4, 5], "its": 4, "basic": [4, 5], "good": [4, 5], "reason": [4, 5], "It": [4, 5], "store": [4, 5], "wide": 4, "accept": 4, "input": 4, "nice": 4, "plot": [4, 5], "function": [4, 5], "exploratori": 4, "familiar": 4, "workflow": 4, "essenti": 4, "help": 4, "interfac": 4, "lightn": 4, "pyro": 4, "cellxgen": 4, "interact": 4, "visual": 4, "ok": 4, "confus": 4, "There": [4, 5], "alwai": 4, "why": 4, "wai": [4, 5], "make": 4, "repres": [4, 5], "import": [4, 5], "public": 4, "At": 4, "contain": 4, "jargon": 4, "doe": 4, "sens": [4, 5], "novemb": 5, "default": 5, "tutori": 5, "scvers": [5, 6], "heavili": 5, "depend": 5, "being": 5, "object": 5, "systemat": 5, "retriev": 5, "intermedi": 5, "score": 5, "umap": 5, "embed": 5, "cluster": 5, "label": 5, "etc": 5, "document": 5, "site": 5, "cover": 5, "remain": 5, "annot": 5, "tabular": 5, "By": 5, "typic": 5, "featur": 5, "row": 5, "column": 5, "matrix": 5, "special": 5, "index": 5, "barcod": 5, "furthermor": 5, "might": 5, "addit": 5, "donor": 5, "inform": 5, "altern": 5, "symbol": 5, "final": 5, "color": 5, "pallet": 5, "without": 5, "go": 5, "fanci": 5, "you": 5, "ll": 5, "take": 5, "word": 5, "realli": 5, "exist": 5, "sparsiti": 5, "user": 5, "friendli": 5, "spars": 5, "count": 5, "numpi": 5, "np": 5, "scipi": 5, "csr_matrix": 5, "random": 5, "poisson": 5, "size": 5, "2000": 5, "adata": 5, "n_ob": 5, "n_var": 5, "summari": 5, "stastic": 5, "pass": 5, "x": 5, "100x2000": 5, "type": [5, 6], "class": 5, "int64": 5, "126612": 5, "element": 5, "compress": 5, "format": 5, "ob": 5, "var": 5, "ax": 5, "obs_nam": 5, "resp": 5, "var_nam": 5, "cell_": 5, "rang": 5, "gene_": 5, "print": 5, "cell_0": 5, "cell_1": 5, "cell_2": 5, "cell_3": 5, "cell_4": 5, "cell_5": 5, "cell_6": 5, "cell_7": 5, "cell_8": 5, "cell_9": 5, "dtype": 5, "valu": 5, "view": 5, "imagin": 5, "particular": 5, "modul": 5, "rule": 5, "quit": 5, "similar": 5, "panda": 5, "boolean": 5, "mask": 5, "integ": 5, "cell_10": 5, "gene_5": 5, "gene_1900": 5, "add": 5, "pretti": 5, "simpl": 5, "ct": 5, "choic": 5, "monocyt": 5, "cell_typ": 5, "cell_95": 5, "cell_96": 5, "cell_97": 5, "cell_98": 5, "cell_99": 5, "randomli": 5, "bdata": 5, "37": 5, "obsm": 5, "varm": 5, "attribut": 5, "kei": 5, "identifi": 5, "differ": 5, "insert": 5, "restrict": 5, "must": 5, "length": 5, "equal": 5, "number": 5, "independ": 5, "x_umap": 5, "normal": 5, "gene_stuff": 5, "axisarrai": 5, "again": 5, "few": 5, "arrai": 5, "origin": 5, "dens": 5, "easili": 5, "instead": 5, "item": 5, "g": 5, "un": 5, "allow": 5, "ani": 5, "anyth": 5, "dictionari": 5, "3": 5, "ordereddict": 5, "form": 5, "exampl": 5, "log": 5, "transform": 5, "log_transform": 5, "log1p": 5, "ask": 5, "return": 5, "to_df": 5, "iloc": 5, "gene_0": 5, "gene_1": 5, "gene_2": 5, "gene_3": 5, "gene_4": 5, "693147": 5, "609438": 5, "000000": 5, "386294": 5, "098612": 5, "creation": 5, "standard": 5, "straightforward": 5, "faciliat": 5, "reproduc": 5, "even": 5, "easier": 5, "still": 5, "don": 5, "do": 5, "encourag": 5, "look": 5, "through": 5, "api": 5, "doc": 5, "properti": 5, "preprint": 6, "transcript": 6, "dynam": 6, "veloc": 6, "philipp": 6, "weiler": 6, "mohammad": 6, "lotfollahi": 6, "dominik": 6, "klein": 6, "justin": 6, "hong": 6, "fabian": 6, "biorxiv": 6, "2022": 6, "paper": 6, "journal": 6, "articl": 6, "ecosystem": 6, "isaac": 6, "virshup": 6, "danila": 6, "bredikhin": 6, "luka": 6, "heumo": 6, "giovanni": 6, "palla": 6, "gregor": 6, "sturm": 6, "ilia": 6, "kat": 6, "mikaela": 6, "koutrouli": 6, "commun": 6, "bonni": 6, "berger": 6, "aviv": 6, "sarah": 6, "francesca": 6, "finotello": 6, "alexand": 6, "wolf": 6, "oliv": 6, "stegl": 6, "empir": 6, "differenti": 6, "pierr": 6, "boyeau": 6, "jeffrei": 6, "regier": 6, "michael": 6, "jordan": 6, "romain": 6, "lopez": 6, "proceed": 6, "nation": 6, "academi": 6, "press": 6, "tabula": 6, "sapien": 6, "multipl": 6, "organ": 6, "transcriptom": 6, "consortium": 6, "peakvi": 6, "chromatin": 6, "tal": 6, "ashuach": 6, "daniel": 6, "reidenbach": 6, "report": 6, "librari": 6, "galen": 6, "xing": 6, "valeh": 6, "valiollah": 6, "pour": 6, "amiri": 6, "katherin": 6, "wu": 6, "jayasuriya": 6, "edouard": 6, "mehlman": 6, "langevin": 6, "yine": 6, "liu": 6, "jule": 6, "samaran": 6, "gabriel": 6, "misrachi": 6, "achil": 6, "nazaret": 6, "oscar": 6, "clivio": 6, "chenl": 6, "xu": 6, "valentin": 6, "svensson": 6, "eduardo": 6, "da": 6, "veiga": 6, "beltram": 6, "vitalii": 6, "kleshchevnikov": 6, "carlo": 6, "talavera": 6, "lior": 6, "pachter": 6, "cell2loc": 6, "map": 6, "fine": 6, "grain": 6, "spatial": 6, "artem": 6, "shmatko": 6, "emma": 6, "dann": 6, "aivazidi": 6, "hamish": 6, "w": 6, "king": 6, "tong": 6, "li": 6, "rasa": 6, "elmentait": 6, "lomakin": 6, "veronika": 6, "kedlian": 6, "mika": 6, "sarkin": 6, "jain": 6, "jun": 6, "sung": 6, "park": 6, "lauma": 6, "ramona": 6, "elizabeth": 6, "tuck": 6, "anna": 6, "arutyunyan": 6, "roser": 6, "vento": 6, "tormo": 6, "moritz": 6, "gerstung": 6, "louisa": 6, "jame": 6, "omer": 6, "ali": 6, "bayraktar": 6, "refer": 6, "atlas": 6, "transfer": 6, "mohsen": 6, "naghipourfar": 6, "malt": 6, "matin": 6, "khajavi": 6, "maren": 6, "b\u00fcttner": 6, "marco": 6, "wagenstett": 6, "ziga": 6, "avsec": 6, "marta": 6, "interlandi": 6, "sergei": 6, "rybakov": 6, "misharin": 6, "joint": 6, "multi": 6, "totalvi": 6, "zo\u00eb": 6, "steier": 6, "kristoph": 6, "nazor": 6, "factor": 6, "via": 6, "bioinformat": 6, "character": 6, "fate": 6, "probabl": 6, "palantir": 6, "manu": 6, "setti": 6, "vaidota": 6, "kiseliova": 6, "jacob": 6, "levin": 6, "lina": 6, "mazuti": 6, "stress": 6, "adapt": 6, "respons": 6, "associ": 6, "carbapenem": 6, "resist": 6, "kpc": 6, "produc": 6, "klebsiella": 6, "pneumonia": 6, "sheila": 6, "sapper": 6, "lee": 6, "rilei": 6, "pathogen": 6, "2018": 6, "review": 6, "enhanc": 6, "scienti\ufb01c": 6, "discoveri": 6, "refere": 6, "workshop": 6, "quantifi": 6, "sampl": 6, "elham": 6, "azizi": 6, "mlcb": 6, "oral": 6, "surfac": 6, "protein": 6, "abund": 6, "detect": 6, "zero": 6, "inflat": 6, "spotlight": 6, "talk": 6}, "objects": {}, "objtypes": {}, "objnames": {}, "titleterms": {"from": 1, "pca": 1, "vae": 1, "explor": 1, "refer": 1, "blog": 2, "get": 4, "start": 4, "singl": 4, "cell": 4, "genom": 4, "updat": [4, 5], "mai": [4, 5], "4": [4, 5], "2023": [4, 5], "overview": 4, "video": 4, "paper": 4, "data": 4, "analysi": 4, "softwar": 4, "tutori": 4, "tip": 4, "other": 4, "consider": 4, "5": 5, "mayb": 5, "10": 5, "minut": 5, "anndata": 5, "why": 5, "initi": 5, "subset": 5, "ad": 5, "align": 5, "metadata": 5, "observ": 5, "variabl": 5, "level": 5, "us": 5, "matric": 5, "unstructur": 5, "layer": 5, "output": 5, "datafram": 5, "wrap": 5, "up": 5, "public": 6}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 8, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.intersphinx": 1, "sphinx.ext.todo": 2, "sphinx.ext.viewcode": 1, "sphinx": 57}, "alltitles": {"From PCA to VAE": [[1, "from-pca-to-vae"]], "Exploration of PCA": [[1, "exploration-of-pca"]], "References": [[1, "references"]], "Blog": [[2, "blog"]], "Getting started with single-cell genomics": [[4, "getting-started-with-single-cell-genomics"]], "Update (May 4, 2023)": [[4, null], [5, null]], "Overview of single-cell genomics": [[4, "overview-of-single-cell-genomics"]], "Videos": [[4, "videos"]], "Papers": [[4, "papers"], [4, "id1"]], "Data analysis": [[4, "data-analysis"]], "Software and tutorials": [[4, "software-and-tutorials"]], "Tips and other considerations": [[4, "tips-and-other-considerations"]], "5, maybe 10 minutes to AnnData": [[5, "maybe-10-minutes-to-anndata"]], "Why AnnData?": [[5, "why-anndata"]], "Initializing AnnData": [[5, "initializing-anndata"]], "Subsetting AnnData": [[5, "subsetting-anndata"]], "Adding aligned metadata": [[5, "adding-aligned-metadata"]], "Observation/Variable level": [[5, "observation-variable-level"]], "Subsetting using metadata": [[5, "subsetting-using-metadata"]], "Observation/Variable level matrices": [[5, "observation-variable-level-matrices"]], "Unstructured metadata": [[5, "unstructured-metadata"]], "Layers": [[5, "layers"]], "Outputting DataFrames": [[5, "outputting-dataframes"]], "Wrapping up": [[5, "wrapping-up"]], "Publications": [[6, "publications"]]}, "indexentries": {}})