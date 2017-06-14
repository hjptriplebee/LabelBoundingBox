# Label_BoundingBox
A tool for labeling bounding boxes of training images. It is based on BBox-Label-Tool and supports multi-class labeling. Here is a demo:

<img src="https://raw.githubusercontent.com/hjptriplebee/Label_BoundingBox/master/demo.jpg" width = "850" height = "600" alt="demo" />

# Requirement
- Python (2 and 3 is all ok, 2 need a little change)
- OpenCV (It isn't necessary, if you only use labeling function. OpenCV is only for getFrameFromVideo.py)
- tkinter
- PIL

# Usage
## for basic bbox-label-tool:
- Put image in the folder which is under "Images"
- Start label-tool with "python3 main.py"
- Input "Image Dir" which is the name of your folder under "Images"
- click "load" and you can label images now!
- To create a new bounding box, left-click to select the first vertex. Moving the mouse to draw a rectangle, and left-click again to select the second vertex.
- To cancel the bounding box while drawing, just press "<ESC>"
- To delete a existing bounding box, select it from the listbox, and click 'Delete'.
- To delete all existing bounding boxes in the image, simply click 'ClearAll'.
- After finishing one image, click 'Next' to advance. Likewise, click 'Prev' to reverse. You can press "<Left>" and "<Right>" Or input the index and click 'Go' to navigate to an arbitrary image instead.** The labeling result will be saved if and only if the 'Next' button is clicked.**
- label files are stored in "Labels" folder

## for multi-class labeling:
- Write down your classes in "class.txt"
- Start label-tool and select class at the top-right corner.***remember to click "ConfirmClass"***
- After clicking "ConfirmClass", you can label different classes with different colors.

## for get Frame from Video:
It isn't user-friendly. If you want to use it, I recommend you to read source code carefully!