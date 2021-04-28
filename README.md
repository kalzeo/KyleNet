<!-- PROJECT LOGO -->
<br />
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/5749422/113945678-b50dcd00-97fe-11eb-8846-71f9c9758784.png">
  <h3 align="center">KyleNet</h3>
  <p align="center">
    For experimental purposes only
    <br />
    <a href="https://github.com/kalzeo/KyleNet/issues">Report Bug</a>
    ·
    <a href="https://github.com/kalzeo/KyleNet/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
KyleNet is a CNN model that was developed to classify COVID-19 in CXRs and CT scans as part of a BSc (Hons) project.
<br>
<br>
It is only intended to be used as an experimental framework, not a clinical diagnostic tool.

ℹ️ The experimental dataset + models have been moved to Kaggle and can be found [here.](https://www.kaggle.com/kylemcpherson/kylenet-experimental-dataset)

### Built With

* Python 3.8

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* [Python 3.6 - 3.8](https://www.python.org/downloads/)
* [Windows 7 or later (64-bit)](https://www.microsoft.com/en-gb/software-download/)
* [Microsoft Visual Studio 2019](https://visualstudio.microsoft.com/downloads/)
* [NVIDIA GPU Drivers v450.x or higher](https://www.nvidia.com/Download/index.aspx)
* [NVIDIA CUDA Toolkit v11.0](https://developer.nvidia.com/cuda-11.0-update1-download-archive)
* [NVIDIA cuDNN SDK v8.1.1 for CUDA v11.0](https://developer.nvidia.com/rdp/cudnn-archive)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kalzeo/KyleNet.git
   ```
2. Install Python libraries
   ```sh
   pip install -r requirements.txt
   ```
   
<!-- USAGE EXAMPLES -->
## Usage
After you've downloaded the prerequisites and completed the necessary installation steps, go to the [root](https://github.com/kalzeo/KyleNet/) folder and run the following command to start the application.<br>
```sh
   streamlit run streamlit_app.py
   ```
Additionally, the UI can be viewed online here: https://share.streamlit.io/kalzeo/kylenet/main/
   <br>
   <br>
  <img align="left" src="https://user-images.githubusercontent.com/5749422/113944563-a1f9fd80-97fc-11eb-86ee-70ca578f914d.png" alt="Upload images">
  <p>Images can be uploaded to the framework using the file uploader in the sidebar to receive results within a couple of seconds.</p>
  <br><br><br><br><br>
  <img align="left" src="https://user-images.githubusercontent.com/5749422/113945145-a2df5f00-97fd-11eb-92e2-2da0beea3e77.png" alt="View images">
  <p>Easily switch between different images that have been uploaded using the dropdown menu.</p>
  <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kalzeo/KyleNet/issues) for a list of proposed features (and known issues).

<!-- LICENSE -->
## License
Distributed under the GNU General Public License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Kyle McPherson - [Linkedin](https://www.linkedin.com/in/kyle-mcpherson-488b99182/)<br>
Project Link: [https://github.com/kalzeo/KyleNet](https://github.com/kalzeo/KyleNet)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Dr. Eyad Elyan](https://orcid.org/0000-0002-8342-9026)
