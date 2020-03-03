import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage.io import imread
from skimage.measure import label, regionprops
from skimage.color import label2rgb, rgb2gray
from skimage import feature
from sci_utils import get_iou
import numpy as np
import bbox

# preprocessing and useful definitions.
threshold = 0.6
image = imread('img.jpg', as_gray=False)
# load template and use the biggest box in it.
template = imread('ref.jpg', as_gray=True)
template = feature.canny(template, sigma=2)
label_template = label(template, connectivity=2, background=0)
template_area = 0
for region in regionprops(label_template):
    if region.area > template_area:
        template_area = region.area
print(f' selected area is: {template_area}')
gray = rgb2gray(image)
edges = feature.canny(gray, sigma=2)
# plt.imshow(edges, cmap='gray')
if template_area <= 150:
    template_area = template_area + 50
    bd = 20
else:
    bd = 100
# label image regions
label_image = label(edges, connectivity=2, background=0)
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)
obj_count = 0
bboxes = []
bbox_dicts = []
final_boxes = []
for region in regionprops(label_image):
    # print(region.area)
    if region.area>=template_area-bd and region.area<=template_area+bd:
        # IoU
        bboxes.append(region)
        temp = region.bbox
        bbox_dict = {'x1': temp[0],
                     'x2': temp[2],
                     'y1': temp[1],
                     'y2': temp[3]}
        bbox_dicts.append(bbox_dict)

selected = []
for i, bbox_dict in enumerate(bbox_dicts):
    counter = 0
    for j, temp in enumerate(bbox_dicts):
        if j > i:
            iou = get_iou(bbox_dict, bbox_dicts[j])
            # print(iou)
            if iou >= threshold:
                counter += 1
    # print(f'bbox {i} has iou with {counter} boxes')
    if counter <= 0:
        selected.append(i)

for k, region in enumerate(bboxes):
    if k in selected:
        # draw rectangle around segmented areas
        minr, minc, maxr, maxc = region.bbox
        plt.text(minc, minr ,f'{obj_count + 1}', fontsize=12)
        obj_count += 1
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                    fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.savefig('output.png')
print(f'{obj_count} objects found')
plt.show()

