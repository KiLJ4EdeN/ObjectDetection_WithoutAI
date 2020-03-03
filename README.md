# ObjectDetection_WithoutAI

Methodology: Region labeling based on Canny features and Bounding-box Intersection over Union (IoU).
In this technique a template of the desired object is chosen. An example is shown below:

Then a template area with a certain boundary in defined to search for optimal regions. For the analysis the input image is converted to gray-scale and then edges are extracted using skimage.feature.canny. Then the regions in the image are classified with skimage.measure.label using the connectivity method. Afterwards the derived regions are compared with the one from the template using the defined boundary. Lastly, to get more significant results, overlapping bounding-boxes are removed if they have 60% or more union percentage. The final outputs are demonstrated below:
 


