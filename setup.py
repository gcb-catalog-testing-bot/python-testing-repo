from setuptools import setup, find_packages

setup(
    name="python-app-by-setuptools",
    version="3.0.0",
    description="A sample Python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="A. Random Developer",
    author_email="author@example.com",
    maintainer="A. Great Maintainer",
    maintainer_email="maintainer@example.com",
    license="MIT",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Reports": "https://github.com/pypa/sampleproject/issues",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "http://saythanks.io/to/example",
        "Source": "https://github.com/pypa/sampleproject/",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sample setuptools development",
    packages=find_packages(),
    install_requires=[
        "peppercorn",
    ],
    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    entry_points={
        "console_scripts": [
            "sample=sample:main",
        ],
    },
    package_data={
        "sample": ["*.dat"],
    },
    python_requires=">=3.7",
)
