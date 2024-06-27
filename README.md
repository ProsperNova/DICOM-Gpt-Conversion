# Welcome: DICOM Gpt Conversion
A free tool that leverages python MRI DICOM extrapolation and filtering to allow interpretation by <a href="https://chat.openai.com/">OpenAI's ChatGPT</a>, creating personalized and highly targetted information for patients with multiple sclerosis brain lesions.

## Purpose

DICOM Gpt Conversion solves the relatively complex problem of uploading bulky DICOM files from a magnetic resonance imaging (MRI) scan to AI services like ChatGPT in a simple way. The script is designed to run on Python, making it cross-platform and relatively easy to use. 

Specifically, this script was designed to parse through DICOM images of a professional MRI scan, identify gadolinium-enhanced lesions, and create a light-weight version of the MRI data, with only images relevant to the diagnosis. The primary purpose is to facilitate the communication of DICOM imaging using python and image interpolation, looking to get personal results between lesion locations and identify specific deficits caused by autoimmune diseases such as multiple sclerosis.

## Results

Using DICOM Gpt Conversion, we were able to:

1.) Parse a MRI DICOM image,
2.) Compress the images into a ZIP archive, and,
3.) Upload the ZIP file to ChatGPT Model 4o, with instructions:
```OpenAI ChaptGPT Model 4o
I'm uploading these PNGs in a ZIP file. Could you please identify the specific brain regions and functionalities likely impacted by the MS lesions seen in these images?

Additionally, please run the following code to visualize the images:
```

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Define the path to the extracted images
extracted_images_path = "/mnt/data/extracted_images/"

# List the first few images to display
image_files = [os.path.join(extracted_images_path, f) for f in os.listdir(extracted_images_path) if f.endswith('.png')][:10]

# Display the selected images
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
for ax, img_path in zip(axes.flatten(), image_files):
    img = mpimg.imread(img_path)
    ax.imshow(img, cmap='gray')
    ax.axis('off')
    ax.set_title(os.path.basename(img_path))

plt.tight_layout()
plt.show()
```
4.) ChatGPT Model 4o had a 96% success rate in identifying multiple sclerosis lesions and both their effects on the patient and the nerulogical and psychological symptoms described.

## Installation

To get started, follow these steps to install the necessary dependencies:

```bash
# Ensure you have Python installed on your system (Python 3.6+ is recommended).
# Install the required Python packages using pip:
pip install pydicom numpy matplotlib
```
## Usage
Follow these steps to use the DICOM Gpt Conversion script:

### Obtaining the file to upload
1.) Clone this repository, or download it manually
```bash
git clone https://github.com/prospernova/dicom_gpt_conversion.git
cd dicom_gpt_conversion
```

2.) Download your MRI DICOM imaging file (Usually from your health care portal or, alternatively, from a third-party contractor like Ambra [This is usually a ZIP file]) and extract it.

3.) In a command-line environment, run:
```bash
python dicom_gpt_conversion.py --input_directory "path_to_your_dicom_files" --output_directory "results"
```
or, if python is "not found", you can try `python3`:
```bash
python3 dicom_gpt_conversion.py --input_directory "path_to_your_dicom_files" --output_directory "results"
```

4.) Compress the contents of `--output-directory` or `results/` into `results.zip`
### Uploading the file and getting ChatGPT to analyze it:
5.) Using Model 4o at minimum, upload the ZIP file and use the following prompt:
```Model 4o
I'm uploading these PNGs in a ZIP file. Could you please identify the specific brain regions and functionalities likely impacted by the MS lesions seen in these images?

Additionally, please run the following code to visualize the images:
```
```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Define the path to the extracted images
extracted_images_path = "/mnt/data/extracted_images/"

# List the first few images to display
image_files = [os.path.join(extracted_images_path, f) for f in os.listdir(extracted_images_path) if f.endswith('.png')][:10]

# Display the selected images
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
for ax, img_path in zip(axes.flatten(), image_files):
    img = mpimg.imread(img_path)
    ax.imshow(img, cmap='gray')
    ax.axis('off')
    ax.set_title(os.path.basename(img_path))

plt.tight_layout()
plt.show()
```
6.) Consider asking additional questions spcific to your prognosis, such as, `Given the specific deficits you noted, suggest activities that could help recover lost functionality` or `What treatment methods are thought to be most successful given my MRI history?`

7.) Enjoy access to ChatGPT-as-a-neurologist.

# Features
<ul>
  <li>Cross-Platform Compatibility: Designed to run on any system that supports Python.</li>
<li>Simple to Use: Easy to set up and run with minimal configuration.</li>
<li>Efficient Conversion: Converts bulky DICOM files into manageable PNG or JPEG images.</li>
<li>Focused Analysis: Specifically processes T2 and FLAIR sequences to identify Gd-enhanced lesions.</li>
</ul>

# Additional Resources
<a href="https://pydicom.github.io/pydicom/stable/index.html">pydicom Documentation</a>
<a href="https://numpy.org/devdocs/">NumPy Documentation</a>
<a href="https://matplotlib.org/stable/users/index.html">Matplotlib Documentation</a>

<b>DISCLAIMER:</b> DICOM Gpt Conversion is <u>not</U> intended to replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider with any questions you may have regarding a medical condition. Use this tool as a supplementary resource and not as a sole basis for health evaluation or decision-making.
