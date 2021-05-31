@def title = "Blog"
@def hascode = true
@def date = Date(2020, 8, 31)

@def tags = ["syntax", "code"]

<!-- \newcommand{\title}[2]{~~~<span style="color:#1; font-weight: 800">#2</span><br>~~~} -->
\newcommand{\title}[2]{~~~<span style="font-weight: 750">#2</span><br>~~~}
\newcommand{\italic}[1]{_*!#1*_}
\newcommand{\bold}[1]{__!#1__}

~~~
<h1>Blog</h1>
<hr>
~~~

{{blogposts}}

~~~
<hr>
~~~