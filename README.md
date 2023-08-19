# python-data-demo

## Environment with Virtualenv
```
(base) >> python3 -m pip install --user -U virtualenv
(base) >> python3 -m virtualenv pure_env
(base) >> source pure_env/bin/activate
...
(pure_env) >> deactivate
```

## Environment with Conda
Miniconda is enough for most of the cases.

```
(base) >> conda create -n pure_env
(base) >> conda env remove --name test_env 
```

```
(base) >> conda env list
(base) >> conda env create -f tensorflow-apple-metal.yml -n tensorflow
(base) >> conda activate tensorflow
(tensorflow) >> python -m ipykernel install --user --name tensorflow --display-name "Python (tensorflow)"
(tensorflow) >> conda env list
(tensorflow) >> conda deactivate
```

tensorflow-apple-metal.yml:
```
name: tensorflow
channels:
  - apple
  - conda-forge
dependencies:
    - python=3.10
    - pip>=19.0
    - jupyter
    - scikit-learn
    - scipy
    - pandas
    - pandas-datareader
    - matplotlib
    - pillow
    - tqdm
    - requests
    - h5py
    - pyyaml
    - flask
    - boto3
    - ipykernel
    - pip:
        - tensorflow-macos
        - tensorflow-metal
        - bayesian-optimization
        - gym
        - kaggle
```

## Jupyter Notebook
### Debug
```
>> jupyter notebook --debug
```

### Install
```
>> !python -m pip install tensorflow
```
The ! at the beginning of the command is used to execute shell commands within the notebook environment.

## Other Notes
### Module platform
```
import platform
print(platform.platform())
```