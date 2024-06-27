import os
import pydicom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imsave

def load_dicom_files(directory):
    """Load all DICOM files from the specified directory and its subdirectories."""
    dicom_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".dcm"):
                dicom_files.append(os.path.join(root, file))
    return dicom_files

def is_gd_enhanced(dicom_file):
    """Check if a DICOM file contains Gd-enhanced lesions based on pixel intensity."""
    try:
        ds = pydicom.dcmread(dicom_file)
        pixel_array = ds.pixel_array
        # Simple thresholding to detect Gd-enhanced lesions (this is a placeholder; adjust based on actual criteria)
        threshold = np.mean(pixel_array) + 3 * np.std(pixel_array)
        return np.any(pixel_array > threshold)
    except Exception as e:
        print(f"Error reading pixel data from {dicom_file}: {e}")
        return False

def save_images(files_by_shape, output_directory):
    """Save DICOM images as JPEG/PNG files."""
    if not files_by_shape:
        print("No relevant DICOM files found.")
        return
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for shape, files in files_by_shape.items():
        if not files:
            continue
        
        for i, dicom_file in enumerate(files):
            ds = pydicom.dcmread(dicom_file)
            pixel_array = ds.pixel_array
            # Normalize pixel values to range from 0 to 255
            pixel_array_normalized = 255 * (pixel_array - np.min(pixel_array)) / (np.max(pixel_array) - np.min(pixel_array))
            pixel_array_normalized = pixel_array_normalized.astype(np.uint8)
            # Save the image
            output_file = os.path.join(output_directory, f"{shape}_{i}.png")
            imsave(output_file, pixel_array_normalized, cmap='gray')
            print(f"Saved image {output_file}")

def scan_contains_gd_enhanced(scan_type):
    """Determine if a scan type is known to be associated with Gd-enhanced scans."""
    return "FLAIR" in scan_type or "T2" in scan_type

def get_relevant_dicom_files(directory):
    """Get DICOM files from relevant subdirectories and check for Gd-enhanced lesions."""
    relevant_files = {}
    for root, subdirs, _ in os.walk(directory):
        for subdir in subdirs:
            subdir_path = os.path.join(root, subdir)
            dicom_files = load_dicom_files(subdir_path)
            if dicom_files:
                ds = pydicom.dcmread(dicom_files[0])
                if 'SeriesDescription' in ds and scan_contains_gd_enhanced(ds.SeriesDescription):
                    for dicom_file in dicom_files:
                        if is_gd_enhanced(dicom_file):
                            ds_temp = pydicom.dcmread(dicom_file)
                            shape = ds_temp.pixel_array.shape
                            if shape not in relevant_files:
                                relevant_files[shape] = []
                            relevant_files[shape].append(dicom_file)
    return relevant_files

def main(input_directory, output_directory):
    print(f"Scanning directory: {input_directory}")
    relevant_files_by_shape = get_relevant_dicom_files(input_directory)
    save_images(relevant_files_by_shape, output_directory)
    print(f"Processing complete. Images saved in {output_directory}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process DICOM files for Gd-enhanced lesions.')
    parser.add_argument('--input_directory', type=str, required=True, help='Directory containing DICOM files')
    parser.add_argument('--output_directory', type=str, default='results', help='Directory to save output images')
    
    args = parser.parse_args()
    main(args.input_directory, args.output_directory)
