# pdf-binocular

> [!WARNING]  
> Author is not responsible for consequences of your usage of this script for your eyes, 
> vision and health. You can use it at your own risk or probably have a consultation with
> a doctor first.


## Rationale

When reading a book for some time eyes can become tired.

The one reason of that can be that eyes are looking inward, and the muscles are strained.

This script duplicates content of every PDF page making the page wider, 
so both eyes can look at theirs own content without muscles strain for looking inward -
eyes are in position like when they are looking at something at the distance.

Usually the distance between the pupils is around 6-7 centimeters.
Thus make sure that the half width of generated PDF page has the same size.
Usually E-reader or smartphone in horizontal orientation can be adjusted to make this proportion.
There are also some parameters in the script that can help.

## Parameters
```
generate_pdf(file_name, postfix="_binocular", crop_v=0, crop_h=0, gap=0)
```
`file_name` - PDF file path

`postfix` - string postfix that will be added to resulted PDF file name

`crop_v` - crop page on top and bottom

`crop_h` - crop page on left and right sides

`gap` - crop interval between two initial pages on one PDF page

Some PDF books can have wide paddings on left/right or top/bottom, to reduce them, 
`crop_v` and `crop_h` parameters can be used.

Also `gap` parameter can be used to reduce or increase gap between left/right contents on the page.

## Usage 

Install `pypdf`
``` 
pip install pypdf
```

Update PDF file name in the script and run it.
