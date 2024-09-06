# DICOM-GPT Conversion: An AI-Assisted Tool for Analyzing MS Lesions in MRI Scans

## Welcome to the DICOM-GPT Conversion Tool
This Python-based tool enhances the analysis of MRI DICOM files, enabling automated lesion identification and a high-level interpretive report for patients with multiple sclerosis (MS). By converting MRI DICOM images into a format interpretable by AI models, such as OpenAI's ChatGPT, it provides personalized insights into lesion location and potential neurological impacts, making it a valuable aid for both patients and healthcare professionals.

## Purpose
DICOM-GPT Conversion is designed to bridge the gap between complex MRI data and accessible AI-assisted interpretations. By parsing MRI DICOM files, designed particularly for patients with multiple sclerosis, the tool extracts relevant images (e.g., those showing gadolinium-enhancing lesions) and converts them into a format that AI models can analyze. The goal is to simplify the process of identifying lesion locations and correlating them with functional deficits, potentially aiding neurologists in patient discussions and prognosis.
The initiative seeks to transform the use and accessibility of MRI in the field of neurological healthcare, emphasizing three key goals:
<ol>
<li><strong>Identifying Lesions and Isolating Potential Deficits:</strong>
<p>MRI is a powerful tool in diagnosing and monitoring neurological conditioans by detecting lesions and structural abnormalities in the brain and spinal cord. By leveraging advanced imaging techniques, we aim to more precisely identify the location, size, and activity of lesions, enabling a better understanding of their correlation with neurological deficits. This will allow clinicians to pinpoint areas of potential cognitive, sensory, or motor impairment, tailoring treatments more effectively to individual patients.</p>
</li>
<li><strong>Making MRI More Accessible to the Public:</strong>
<p>Access to MRI is often limited by high costs and geographic barriers, preventing timely diagnosis and intervention for many patients. We aim to reduce these barriers by promoting partnerships with healthcare providers, developing affordable options, and advocating for broader insurance coverage and public funding. This will democratize access to critical imaging technologies, ensuring that individuals across diverse socioeconomic backgrounds can benefit from early detection and personalized treatment strategies.</p>
</li>
<li><strong>Supporting ProsperNova's NeuroGenius Application for Functional Recovery:</strong>
<p>NeuroGenius is an innovative platform within ProsperNova that seeks to leverage fMRI and neurofeedback to promote targeted remyelination of affected lesions, going beyond traditional therapeutic outcomes. By using real-time neurofeedback, the application allows patients to interactively engage in neuroplasticity exercises, aimed at regenerating myelin in specific damaged areas. This targeted approach has the potential to enhance functional recovery after neurodegeneration, with the ultimate goal of achieving measurable improvements that can be confirmed by follow-up MRI scans. The integration of fMRI into NeuroGenius will offer unprecedented insights into both therapeutic progress and the physiological basis of functional recovery.</p>
</li>
</ol>
DICOM-Gpt-Conversion was originally based off of our MRI lesion-targetting system used in the active development of <a href="https://github.com/ProsperNova/NeuroGenius">NeuroGenius</a>. In the future, this software will, upon mapping lesions, output the possible deficits, and ask patients which lesion they wish to target using our remylination platform, which combines different forms of neurofeedback to attempt stimulated memyelination acrosss specific, targetted lesions.

## Features
<ul>
  <li>Cross-Platform Compatibility: Designed to run on any system that supports Python.</li>
  <li>Simple to Use: Easy to set up and run with minimal configuration.</li>
  <li>Efficient Conversion: Converts bulky DICOM files into manageable PNG or JPEG images.</li>
  <li>Focused Analysis: Specifically processes T2 and FLAIR sequences to identify Gd-enhanced lesions.</li>
</ul>

## Installation
Use the following guide to install, with the only prerequisite being Python. We're assuming you have some pre-requisite Python experience, which would make the experience much more seemless. With that said, the following steps have been tested in Windows, Linux (Ubuntu, Debian, CentOS, RHL), and macOS with ```brew``` already set up and configured.
<ol>
<li>Download the source code from this repo using the web interface, or clone to your computer using ```gh``` as follows:
```Cli
gh repo clone ProsperNova/DICOM-Gpt-Conversion
~~~
</li>
<li>Using python's pip, run the following command:
```Cli
pip install pydicom numpy matplotlib
```
This installs the following libraries for your python environment, and which the script depends on:
<ul>
<li><strong>pydicom</strong> for working with DICOM files.</li>
<li><strong>numpy</strong> for numerical computations.</li>
<li><strong>matplotlib</strong> for plotting and image visualization, including saving images with imsave.</li>
</ul>
</li>
</ol>
## Using ```dicom-gpt-conversion.py```
### Converting DICOM files
<ol>
<li>Extract the DICOM ZIP file, and find the relevant directory (```/dicom``` usually)</li>
<li>Create a destination directory (i.e. ```~/Documents/dicom-for-gpt```)</li>
<li>Make sure your terminal is pointed at the same folder as ```dicom_gpt_conversion.py```, and, using absolute paths for --input-drectory and --output-directory, run ```dicom_gpt_conversion.py --input_directory "dir" ----output_directory "dir"```
<li>ZIP the folder "output_directory" and upload it to your favorite AI!</li>
</ol>
### Tested Questions to use with the file:
`Help me identify lesions associated with [disease] and help me identify potential deficits`
`Given the specific deficits you noted, suggest activities that could help recover lost functionality`
`What treatment methods are thought to be most successful given my MRI history?`
## Relevant Conditons
Here's a comprehensive list of conditions where the DICOM GPT Conversion tool could be helpful, including multiple sclerosis and other related and unrelated neurological and medical conditions.
<p>This format is designed to be search-friendly and inclusive of a wide range of potential users:</p>
### Conditions Potentially Benefiting from DICOM GPT Conversion for MRI Lesion Analysis:
<ol>
<li><strong>Multiple Sclerosis</strong> (<i>MS</i>), including Relapsing-Remitting (<i>RRMS</i>), somewhat successful in Secondary Progressive (<i>SPMS</i>), would be somewhat successful in Primary Progressive (<i>PPMS</i>) with modification to detect old or non-enhancing lesions.
<p><strong>Description:</strong> An autoimmune disease that affects the central nervous system, causing lesions in the brain and spinal cord.</p>
<p><strong>How It Helps:</strong> This tool can identify and track demyelination, helping to evaluate disease progression and response to treatment.</p>
</li>
<li><strong>Stroke</strong> (<i>Ischemic Stroke</i> &amp; <i>Hemorrhagic Stroke</i>)
<p><strong>Description:</strong> A condition where blood flow to the brain is interrupted or a blood vessel ruptures, leading to brain damage.</p>
<p><strong>How It Helps:</strong> Identifies areas of brain damage, aiding in assessing severity and guiding rehabilitation.</p>
</li><strong>Traumatic Brain Injury (TBI)</strong>
<p><strong>Description:</strong> Damage to the brain caused by an external force, such as a blow to the head or a penetrating injury.</p>
<p><strong>How It Helps:</strong> Pinpoints trauma-induced lesions, useful for evaluating long-term cognitive or motor deficits.</p>
</li>
<li><strong>Parkinson's Disease</strong>
<p><strong>Description:</strong> A progressive neurological disorder affecting movement due to the degeneration of dopamine-producing neurons.</p>
<p><strong>How It Helps:</strong> Helps visualize structural changes in the brain, particularly in regions like the basal ganglia, which are critical for motor control.</p>
</li>
<li><strong>Alzheimer’s Disease and Other Dementias</strong>
<p><strong>Description:</strong> Neurodegenerative conditions that result in memory loss, cognitive decline, and personality changes.</p>
<p><strong>How It Helps:</strong> Highlights brain atrophy and regions affected by the disease, aiding in diagnosis and tracking progression.</p>
</li>
<li><strong>Brain Tumors</strong> (<i>Gliomas, Meningiomas, etc.</i>)
<p><strong>Description:</strong> Abnormal growths of tissue in the brain that can be benign or malignant.</p>
<p><strong>How It Helps:</strong> Locates tumors, tracks growth, and helps assess treatment response.</p>
</li>
<li><strong>Epilepsy</strong>
<p><strong>Description:</strong> A neurological disorder characterized by recurrent seizures, often due to abnormal brain activity.</p><p><strong>How It Helps:</strong> Identifies structural abnormalities or lesions that may trigger seizures, supporting surgical planning or medication management.</p>
</li>
<li><strong>Encephalitis</strong>
<p><strong>Description:</strong> Inflammation of the brain, often due to viral infection or increased susceptibility due to treatment of an autoimmune disorder.</p>
<p><strong>How It Helps:</strong> Detects areas of inflammation, helping to guide diagnosis and treatment of the underlying cause.</p>
</li>
<li><strong>Vasculitis</strong></p>
<p><strong>Description:</strong> Inflammation of blood vessels in the brain, which can lead to reduced blood flow and damage.</p>
<p><strong>How It Helps:</strong> Identifies brain regions affected by vascular inflammation, aiding in managing disease activity.</p>
</li>
<li><strong>Neuromyelitis Optica (NMO)</strong>
<p><strong>Description:</strong> A rare autoimmune disease that primarily affects the optic nerves and spinal cord, often mistaken for MS.</p>
<p><strong>How It Helps:</strong> Detects lesions specific to NMO, aiding in differentiating it from other demyelinating diseases like MS.</p>
</li>
<li><strong>Acute Disseminated Encephalomyelitis (ADEM)</strong>
<p><strong>Description:</strong> A brief but intense attack of inflammation in the brain and spinal cord, often following a viral infection or vaccination.</p>
<p><strong>How It Helps:</strong> Helps identify widespread lesions caused by inflammation, supporting prompt treatment.</p>
</li>
<li><strong>Cerebral Palsy</strong>
<p><strong>Description:</strong> A group of disorders affecting movement and muscle tone, often due to brain damage before or during birth.</p>
<p><strong>How It Helps:</strong> Visualizes structural brain abnormalities that contribute to motor and cognitive impairments.</p>
</li>
<li><strong>Hydrocephalus</strong>
<p><strong>Description:</strong> A condition where excess cerebrospinal fluid builds up in the brain, causing pressure and potentially leading to brain damage.</p>
<p><strong>How It Helps:</strong> Helps monitor ventricles and fluid accumulation, crucial for managing shunt placements and other treatments.</p></li>
<li><strong>Chiari Malformation</strong>
<p><strong>Description:</strong> A structural defect in the cerebellum, causing part of it to extend into the spinal canal.</p>
<p><strong>How It Helps:</strong> Identifies the extent of the malformation, helping plan surgeries or other interventions.</p>
</li>
<li><strong>Agenesis of the Corpus Callosum</strong>
<p><strong>Description:</strong> A rare congenital disorder where the corpus callosum, the structure connecting the two hemispheres of the brain, is partially or completely absent.</p>
<p><strong>How It Helps:</strong> Visualizes developmental abnormalities, aiding in understanding the potential impact on cognition and coordination.</p>
</li>
<li><strong>Brain Arteriovenous Malformations</strong> (<i>AVMs</i>)
<p><strong>Description:</strong> Abnormal connections between arteries and veins in the brain, which can cause bleeding or seizures.</p>
<p><strong>How It Helps:</strong> Identifies the size and location of AVMs, guiding surgical or radiosurgical interventions.</p>
</li>
<li><strong>Cavernous Malformations</strong>
<p><strong>Description:</strong> Abnormal clusters of blood vessels in the brain that can leak or bleed, leading to seizures or neurological deficits.</p>
<p><strong>How It Helps:</strong> Helps locate and assess the risk of hemorrhage or other complications.</p>
</li><strong>Amyotrophic Lateral Sclerosis</strong> (<i>ALS</i>)
<p><strong>Description:</strong> A progressive neurodegenerative disease affecting nerve cells in the brain and spinal cord, leading to muscle weakness and atrophy.</p>
<p><strong>How It Helps:</strong> Monitors structural changes in the brain and spinal cord to track disease progression.</p>
</li>
<li><strong>Huntington’s Disease</strong>
<p><strong>Description:</strong> A genetic disorder that causes the progressive breakdown of nerve cells in the brain, affecting movement, cognition, and behavior.</p>
<p><strong>How It Helps:</strong> Tracks degeneration in areas like the striatum, aiding in understanding symptom development and progression.</p>
</li>
<li><strong>Autoimmune Encephalitis</strong>
<p><strong>Description:</strong> A condition where the body’s immune system attacks healthy brain cells, often causing psychiatric and neurological symptoms.</p>
<p><strong>How It Helps:</strong> Identifies inflammation or lesions resulting from the immune attack, helping guide immunotherapy treatment.</p>
</li>
<li><strong>Radiation-Induced Brain Injury</strong>
<p><strong>Description:</strong> Brain damage caused by exposure to radiation, often as a side effect of cancer treatment.</p>
<p><strong>How It Helps:</strong> Monitors changes in brain tissue over time to assess the impact of radiation therapy.</p>
</li>
<li><strong>Vascular Dementia</strong>
<p><strong>Description:</strong> A type of dementia caused by reduced blood flow to the brain, often following strokes or other vascular conditions.</p>
<p><strong>How It Helps:</strong> Identifies regions of brain damage due to poor blood flow, aiding in diagnosis and treatment planning.</p>
</li>
<li><strong>Progressive Multifocal Leukoencephalopathy (PML)</strong>
<p><strong>Description:</strong> A rare, often fatal viral disease that affects the white matter of the brain, caused by the JC virus.</p>
<p><strong>How It Helps:</strong> Detects white matter lesions that are characteristic of PML, aiding in diagnosis and treatment response monitoring.</p>
</li>
<li><strong>Metastatic Brain Cancer</strong>
<p><strong>Description:</strong> Cancer that has spread to the brain from other parts of the body.</p>
<p><strong>How It Helps:</strong> Locates metastatic lesions, assesses their growth, and helps evaluate the effectiveness of treatments.</p>
</li>
<li><strong>Creutzfeldt-Jakob Disease</strong> (<i>CJD</i>)
<p><strong>Description:</strong> A rare, degenerative brain disorder caused by prion proteins, leading to rapid mental deterioration.</p>
<p><strong>How It Helps:</strong> Identifies abnormal brain changes linked to prion disease, aiding in early diagnosis and care management.</p>
</li>
</ol>
<hr><p>This tool, used in combination with ChatGPT for explanation and interpretation, may significantly assist clinicians and patients in understanding MRI findings across a wide range of conditions. This could easily be fine-tuned using privately-trained AIs like <a href="https://llama.meta.com/docs/llama-everywhere">Meta's LLaMa</a> and, while susceptible to potentially misleading results, thus far DICOM-GPT has worked quite well.</p>

## Results
Thus far, our testing has been validated by patient-reported deficits which are 1.) not reported to the AI,  but 2.) are confirmed by the AI, based only on interpretation of MRI data from DICOM-Gpt-conversion-generated files.

## For Clinicians
ProsperNova is a 501(c)(3) non-profit and is releasing this script under MIT license, meaning it's free to redistribute with accreditation given to the original source code. Please note: while this tool is indended to help medical practioners and patients, is is still an early work, and there is much work to be done. If you'd like to pitch in, whether by helping us conduct a clinical trial, or by giving the software a try on your patients, we'd love to hear all about it's accuracy or pitfalls.

## Contibutions

Contibutions are welcome! Please detail any improvements when you submit a  commit, or provide feedback in the "Issues" tab.

## Disclaimer
# Additional Resources
<a href="https://pydicom.github.io/pydicom/stable/index.html">pydicom Documentation</a>
<a href="https://numpy.org/devdocs/">NumPy Documentation</a>
<a href="https://matplotlib.org/stable/users/index.html">Matplotlib Documentation</a>

## DISCLAIMER
DICOM Gpt Conversion is <u>not</U> intended to replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider with any questions you may have regarding a medical condition. Use this tool as a supplementary resource and not as a sole basis for health evaluation or decision-making.
