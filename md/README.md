# Readme

## Introduction

This readme document give an idea of the capability of autodoc the autodocumentation python script.

Autodoc is a python script designed to take a special flavor of markdown and convert it into html documentation on the fly.

The requirements for autodoc were as follows:

* Easy to use.

* $\LaTeX$ support

* Updates to the html as you save.

* Easily managable navigation.

The script is simple and will not handle all the features which one may want.  Part of the reason for this is I wanted something that would work out of box with very little configuration.


## Features

### Latex support

Latex is supported both inline:

```
$\int x^2 dx$
```

$\int x^2 dx$, and on its own line:

```
$$\sum\_{i = 1}^3 \frac{i}{3}$$
```

$$\sum\_{i = 1}^3 \frac{i}{3}$$


### Tables

```
| Header 1 | Header 2 |
|----------|----------|
| Item 1   | Item 2   |
```

| Header 1 | Header 2 |
|----------|----------|
| Item 1   | Item 2   |


### Syntax highlighting

```
	```c
	#include <stdio.h>
	#include <stdlib.h>

	int main(int argc, char ** argv)
	{
		printf("Hello world");
	}
	```
```



```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv)
{
	printf("Hello world");
}
```


## Dependencies

- markdown2

```bash
pip install markdown2
```

- pygments

```bash
pip install pygments
```

## Getting started

There are two directories: `md` and `html`.

### html

The `html` file consists generated files a folder labeled `assets` containing the header (`header.html`) and footer (`footer.html`) used in generation, a folder labeled `css` for styling and a folder labeled `images` for any images in your project.  The only thing you should every have to touch is the `images` directory.

### md

autodoc will pick up any .md files in the `md` directory and create a corresponding .html file in the `html` directory.

### Navigation

Inside of the `md` directory is a file titled `navigation`.  This file contains all of the information for generating the left navigation bar.  The format of lines in this file is:

```
<html file> <link name>
```

### Using autodoc.py

If you start autodoc.py without any arguments it will run indefinately, looking for changes to `.md` files in the `md` directory, and will create the corresponding `.html` files.  Outside of this there are a number of arguments which may be provided:

| Option      | Comment                       |
|-------------|-------------------------------|
| -h          | Show help information         |
| -v          | Show version information      |
| -f {file}   | Update html for file {file}   |
| -a          | Update html for all md files  |
