import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crontzconvert", # Replace with your own username
    version="0.1.0",
    author="Vidocq",
    author_email="vidocqho@gmail.com",
    description="Change crontab between two timezones.",
    py_modules=['crontzconvert'],
    install_requires=['pytz'],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vidocqh/cron-timezone-convert",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)