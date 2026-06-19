import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="text-summarizer",
    version="0.0.0",
    author="prince",
    author_email="your.email@example.com",
    description="A simple text summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prince13045/Text-Summarizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)