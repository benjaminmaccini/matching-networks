# DRP20192
Matching Networks for One Shot Learning Applied to Music Genre Classification

## Dependencies
#### Anaconda
  Download [Anaconda](https://www.anaconda.com/download/)
  ```
      cd /tmp
      curl -O https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
      sha256sum Anaconda3-5.2.0-Linux-x86_64.sh
  ```
  Should get this
  ```
      09f53738b0cd3bb96f5b1bac488e5528df9906be2480fe61df40e0e0d19e3d48  Anaconda3-5.2.0-Linux-x86_64.sh
  ```
  Then run this:
  ```
      ./Anaconda3-5.2.0-Linux-x86_64.sh
  ```
#### PyTorch
  Find out about PyTorch [here](https://pytorch.org/)
  ```
      conda install pytorch-cpu torchvision-cpu -c pytorch
  ```
  There are options that allow for the use of [CUDA](https://developer.nvidia.com/cuda-zone) but I don't personally have NVIDIA, so, yeah not gonna use that.
  
## Env Setup
  How to set up your environment with conda to use the Spotify API. First follow the link below to get your CLIENT_ID and CLIENT_SECRET set up with Spotify.
  - https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app
  Next execute the following commands to get the environment set up with conda.
  ```
    conda env create -f environment.yml
    cd $CONDA_PREFIX
    touch ./etc/conda/activate.d/env_vars.sh 
    touch ./etc/conda/deactivate.d/env_vars.sh
    gedit ./etc/conda/activate.d/env_vars.sh
  ```
  Then add the following:
  ```
    #!/bin/sh

    export CLIENT_ID='your_info'
    export CLIENT_SECRET='your_info'
  ```
  And then do this for deactivate.d:
  ```
     #!/bin/sh

    unset CLIENT_ID
    unset CLIENT_SECRET
  ```
  Then get back to wherever you cloned this repo to and type:
  ```
    conda activate DRP20192
  ```
  
## Future/TODO
  - Use features from the audio_analysis endpoint (timbre, pitch, etc...)
  - Use metalabels for better human readability
  
## Resources
  - https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
  - https://pytorch.org/tutorials/
  - http://colah.github.io/posts/2015-08-Understanding-LSTMs/
  - https://arxiv.org/pdf/1606.04080v2.pdf
  - https://developer.spotify.com/documentation/web-api/reference/object-model/
  - https://www.musictheory.net/
  - https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/
  
