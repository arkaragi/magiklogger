from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="magik_logger",
    version="1.0.0",  # Update this for subsequent versions
    author="Aristotelis Karagiannis",
    description="MagikLogger: A versatile, intuitive, and high-performance Python logging "
                "solution for magical debugging experiences and general application logging.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arkaragi/magik_logger",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
    install_requires=[
        "coloredlogs == 15.0.1",
        "humanfriendly == 10.0"
    ],
    keywords="logging, logger, development, utility",
    license="MIT",
    include_package_data=True,
)