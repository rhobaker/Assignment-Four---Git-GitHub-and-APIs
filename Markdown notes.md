# What is a markup language?
A markup language is structured text-encoding system that includes symbols within a text document to control how it will be formatted when it is printed or displayed on a screen.


## What is Markdown?
Markdown is an easy-to use markup language.  Symbols are added to a plaintext file in order to tell the computer how to format it.\
It is used in GitHub to write README files.

## The most important syntax elements in Markdown

### <u>Comments</u>
Lines of comments can be included that will not be rendered or displayed.
They are written with a **\<\!--** at the beginning and a **--\>** at the end.

E.g. \<\!-- This is a comment --\>

### <u>Headings</u>
Headings are indicated with the use of one to six **hash tags** followed by a space, the number indicating their importance.\
These are similar to h1-h6 tags in HTML.\
E.g. \# This is a heading!

### <u>New Lines</u>
To start a **new line**, put a \\ at the end of the line.\
If this isn't done, there will not be a line break.

To create a new **paragraph** of text, make sure there is a blank line between the blocks of text.\
This is the first paragraph.

This is the second paragraph.

### <u>Text styling</u>
There are a number of ways to style text:

*Italic text* is formatted by placing it between two *'s.\
**Bold text** is formatted by placing it between two **'s.\
***Bold and italic text*** is formatted by placing it between two ***'s.\
<u>Underlined text</u> is formatted by placing it between \<u\> tags.\
<sub>Subscript text</sub> is formatted by placing it between \<sub\> tags.\
<sup>Superscript text</sup> is formatted by placing it between \<sup\>tags.


### <u>Links</u>
A link is inserted by putting the link text in square brackets [].\
The URL is then put inside parentheses ().

E.g. \[BBC news\]\(bbc.co.uk\news)\
[BBC news](bbc.co.uk/)


### <u>Ordered Lists</u>
To format a numbered list, then precede each entry with a number:

E.g.\
\1. Paul\
\2. John\
\3. Ringo\
\4. George


1. Paul
2. John
3. Ringo
4. George

It will be automatically formatted with indents.

### <u>Unordered Lists</u>
To make an unordered list, then precede each entry with a +, * or a -.

E.g.\
\- Mick\
\- Keith\
\- Brian\
\- Ronnie

- Mick
- Keith
- Brian
- Ronnie

It will be automatically formatted with indents.

### <u>Quoting code</u>
Code can be quoted by using three back-tics (\```), before and after the code.\
It can then be formatted into blocks, which will be in a separate box when rendered on the screen.\
E.g.
\`\`\`
def(my_function):\
   return("Hello World!)
\`\`\`

```
def(my_function):
   return("Hello World!)
```

### <u>Images</u>
An image can be included by starting with a ! and then putting the alternative text in square brackets [].\
The URL is then put into parentheses () as for other links.

E.g. \!\[Purple Flower\]\(https://images.freeimages.com/images/large-previews/39a/spring-1377434.jpg?fmt=webp&h=350\)\


![Purple Flower](https://images.freeimages.com/images/large-previews/39a/spring-1377434.jpg?fmt=webp&h=350)
