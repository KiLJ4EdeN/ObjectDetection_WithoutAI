# ObjectDetection_WithoutAI

<a href="https://github.com/KiLJ4EdeN">
    <img src="https://github.com/KiLJ4EdeN/ObjectDetection_WithoutAI/blob/master/logo/logo.PNG" title="logo" align="right" height="200" />
</a>

 [![NO_AI!](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)%5D(https://github.com/sindresorhus/awesome#readme)](https://github.com/KiLJ4EdeN/)
[![License](https://img.shields.io/github/license/KiLJ4EdeN/ObjectDetection_WithoutAI)](https://img.shields.io/github/license/KiLJ4EdeN/ObjectDetection_WithoutAI) [![Version](https://img.shields.io/github/v/tag/KiLJ4EdeN/ObjectDetection_WithoutAI)](https://img.shields.io/github/v/tag/KiLJ4EdeN/ObjectDetection_WithoutAI) [![Code size](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/ObjectDetection_WithoutAI)](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/ObjectDetection_WithoutAI) [![Repo size](https://img.shields.io/github/repo-size/KiLJ4EdeN/ObjectDetection_WithoutAI)](https://img.shields.io/github/repo-size/KiLJ4EdeN/ObjectDetection_WithoutAI) [![Issue open](https://img.shields.io/github/issues/KiLJ4EdeN/ObjectDetection_WithoutAI)](https://img.shields.io/github/issues/KiLJ4EdeN/ObjectDetection_WithoutAI)
![Issue closed](https://img.shields.io/github/issues-closed/KiLJ4EdeN/ObjectDetection_WithoutAI)


## Prerequisites:

1 - Python

2 - Matplotlib

3 - Skimage

4 - bbox

5 - numpy

# To see an example usage:

1 - Clone the repo

2 - Select the input and template images on this lines:
```python
image = imread('examples/2.jpg', as_gray=False)
# load template and use the biggest box in it.
template = imread('examples/ref2.jpg', as_gray=True)
```

3 - Run the script:

```bash
python detect.py
```

Input Image:
![](https://github.com/KiLJ4EdeN/ObjectDetection_WithoutAI/blob/master/ObjectDetection_WithoutAI/examples/2.jpg)

Template Image:
![](https://github.com/KiLJ4EdeN/ObjectDetection_WithoutAI/blob/master/ObjectDetection_WithoutAI/examples/ref2.jpg)

Output:
![](https://github.com/KiLJ4EdeN/ObjectDetection_WithoutAI/blob/master/ObjectDetection_WithoutAI/examples/output2.png)


## Methodology: 

In this technique a template of the desired object is chosen.
Then a template area with a certain boundary in defined to search for optimal regions. For the analysis the input image is converted to gray-scale and then edges are extracted using skimage.feature.canny. Then the regions in the image are classified with skimage.measure.label using the connectivity method. Afterwards the derived regions are compared with the one from the template using the defined boundary. Lastly, to get more significant results, overlapping bounding-boxes are removed if they have 60% or more union percentage.
 
