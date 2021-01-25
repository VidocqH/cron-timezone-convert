import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crontztrans", # Replace with your own username
    version="0.0.1",
    author="Vidocq",
    author_email="vidocqho@gmail.com",
    description="Change crontab between two timezones.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vidocqh/crontzconvert",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)