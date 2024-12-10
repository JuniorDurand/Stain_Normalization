from setuptools import setup, find_packages

setup(
    name="stain_normalization",
    version="0.1.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wanghao14/Stain_Normalization",
    packages=find_packages("src"),           
    package_dir={"": "src"},                 
    install_requires=[                       
        "numpy",
        "patool",
        "spams-bin",
        "matplotlib"
    ],
    python_requires=">=3.5",
)
