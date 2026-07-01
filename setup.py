from setuptools import setup, find_packages

# Read the README for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="neonui",
    version="0.1.0",
    author="Vivi",
    author_email="bistighosh16@gmail.com",
    description="Beautiful, ready-to-use Streamlit components with neon aesthetics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bistighosh16/neonui",
    packages=find_packages(exclude=["tests*", "demo*", "examples*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
    ],
    keywords="streamlit components ui neon glassmorphism themes purple aesthetic",
)