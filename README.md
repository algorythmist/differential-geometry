# Differential Geometry


## Setup

### Virtual Environment


#### Anaconda Environment

```commandline
conda activate computational-physics

conda install --file requirements.txt
```

Set up a virtual environment wihout Anaconda

```commandline
mkdir venv

python -m venv venv

source venv\Scripts\activate

pip install -r requirements.txt
```

### Start Jupyter

The first time, install the jupyter kernel

```commandline
ipython kernel install --name "differential-geometry" --user
```

Then start the notebook

```commandline
jupyter notebook
```

