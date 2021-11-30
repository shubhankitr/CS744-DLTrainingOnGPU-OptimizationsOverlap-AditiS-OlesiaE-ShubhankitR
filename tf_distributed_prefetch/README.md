### Environment Setup
Ubuntu 20.04.3 LTS, 1 x NVIDIA Tesla K80, 150 GB SSD <br/>
sudo apt-get install aptitude <br/>
https://markjay4k.github.io/Install-Tensorflow/, https://www.youtube.com/watch?v=2SYh9XE00FA <br/>
"sudo lshw -C display" shows if driver had been loaded for the card <br/>
"dkms status nvidia" and "uname -r" should match  <br/>
"cat /usr/local/cuda/version.txt" -> "CUDA Version 11.0.207" <br/>
"pip install tensorflow==2.4" <br/>
aptitutude cuda, then remove as in instructions <br/>
cd tensorflow -> source venv/bin/activate

