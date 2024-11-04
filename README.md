# What is the project?

A quick Python app that converts a csv in the below format into a PDF with a title on each page and the amount of blank
pages that have been specified in the csv file.

### Format Required:
Order, Topic, Pages

1,Variables,2

2,Lists,3

3,Functions,0

### Expected Output
In the above examples, you would get a PDF generated that has 3 titles; Variables, Lists and Functions. For each of
these pages you'll get the amount of pages specified minus 1 extra underneath it.
So you Variables, you'll have a title page (first page) plus one extra page.