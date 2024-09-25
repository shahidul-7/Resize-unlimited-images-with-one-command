Here's a sample README section for your GitHub repository explaining how to use the `multi-resize.py` script to resize images. You can paste this directly into your `readme.md` file:

---

## Resize Images Using `multi-resize.py`

With this Python script, you can resize an unlimited number of images. The resized images will have a fixed width of **500px**, and the height will be adjusted automatically to maintain the original aspect ratio.

### Instructions

1. **Create the necessary folders**:
   - Inside your project directory, create a folder called `Images`.
   - Inside the `Images` folder, create a subfolder called `sample`.
   - Place all the `.jpg` images you want to resize inside the `sample` folder.

2. **Download the script**:
   - Copy the `multi-resize.py` file into the `Images` folder.

3. **Run the script**:
   - Open a terminal or command prompt in the `Images` folder and run the following command:
     ```bash
     python multi-resize.py
     ```
   - The script will read all `.jpg` images in the `sample` folder, resize them, and save the resized versions in the same folder with the prefix `resized_`.

### Example Folder Structure

```
Project/
│
├── Images/
│   ├── multi-resize.py
│   └── sample/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── resized_image1.jpg (after running the script)
│       └── resized_image2.jpg (after running the script)
```

### Dependencies

Make sure you have the necessary libraries installed. You can install OpenCV using the following command:

```bash
pip install opencv-python
```

---

Feel free to modify it as necessary for your project!
