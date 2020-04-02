#Try to use setuptools if present. If not then python_requires,
#install_requires and setup_requires will be ignored
try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(
    name="taco_vis",
    version="1.0",
    description="Torsional Axisymmetric Core Oscillation Visualiser",
    author="Sam Greenwood",
    author_email="ee12sg@leeds.ac.uk",
    url="https://github.com/sam-greenwood/taco_vis",
    py_modules=["taco_vis"],
    python_requires='>=3.5',
    install_requires=['numpy','matplotlib'],
    setup_requires=['numpy','matplotlib'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
    ],
)
