import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flaxx",
    version="0.0.2",
    author="Timothy Ford",
    author_email="timefordrums@gmail.com",
    description="A unified platform for data transmission and expression on the async Python stack and common mobile "
                "platforms for rapid, seamless, no-compromise development.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timwford/flax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)