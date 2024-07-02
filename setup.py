from setuptools import setup, find_packages

setup(
    name="IndoMMLU",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[accelerate,
                      appdirs,
                      loralib,
                      bitsandbytes,
                      black
                      black[jupyter],
                      datasets,
                      git+https://github.com/huggingface/peft.git,
                      git+https://github.com/huggingface/transformers.git,
                      sentencepiece,
                      gradio],
    entry_points={
        "console_scripts": [
            "evaluate=evaluate:main",
            # Add other scripts here if needed
        ],
    },
    author="Fork",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/afrizal-HA/IndoMMLU/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
