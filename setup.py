from setuptools import setup, find_packages

setup(
    name='testpackage-qkit',
    version='1.0.0',
    description='qkit test packaging deployment',
    install_requires=[
        # "pyqtgraph",
        # "jupyterlab",
        # "ipywidgets",
        # "h5py",
        # "pandas",
        # "numpy",
        # "zmq"
        "zerorpc",
        "qgrid",

        "numpy==1.24.2",
        "scipy==1.10.1",

        "jupyterlab==3.6.3",
        "jupyterlab-templates==0.4.0",
        "ipywidgets==8.0.6",

        "h5py==3.8.0",
        "pyqt5==5.15.9",
        "pyqtgraph==0.13.3",
        "PyVISA==1.13.0",
        "PyVISA-py==0.6.3",
        "zhinst==23.2.4",
        "pyzmq==25.0.2",

        "matplotlib==3.7.1",
        "uncertainties==3.1.7"


    ],
    packages=find_packages(
        include="qkit"
        )
)
