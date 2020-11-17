COMmon Bayesian Optimization Library ( COMBO )
========
This version is still beta. There might be problems in installing with other packages such as anaconda.

Bayesian optimization has been proven as an effective tool in accelerating scientific discovery.
A standard implementation (e.g., scikit-learn), however,
can accommodate only small training data.
COMBO is highly scalable due to an efficient protocol that employs
Thompson sampling, random feature maps, one-rank Cholesky update and
automatic hyperparameter tuning. Technical features are described in [our document](/docs/combo_document.pdf).


# Required Packages ############################
* Python 3.x.x
* numpy  >=1.10
* scipy  >= 0.16
* Cython >= 0.22.1
* mpi4py >= 2.0 (optional)


# Install ######################################
	1. Download or clone the github repository, e.g.
		> git clone https://github.com/tsudalab/combo3.git

	2. Run setup.py install
		> cd combo
		> python setup.py install

# Uninstall

	1. Delete all installed files, e.g.
		> python setup.py install --record file.txt
		> cat file.txt  | xargs rm -rvf


# Usage
After installation, you can launch the test suite from ['examples/grain_bound/tutorial.ipynb'](examples/grain_bound/tutorial.ipynb).

## License
This package is distributed under the MIT License.
