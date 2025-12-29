from setuptools import setup, find_packages

setup(
    name="prompt_portfolio",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=6.0",
        "requests>=2.31.0",
        "openai>=1.0.0",
        "pandas>=2.1.0",
        "numpy>=1.26.0",
        "jsonschema>=4.21.0"
    ],
    entry_points={
        "console_scripts": [
            "run_single_prompt=02_prompt_execution.runners.run_single_prompt:main",
            "run_prompt_chain=02_prompt_execution.runners.run_prompt_chain:main"
        ]
    },
    python_requires=">=3.11",
    author="EvoLux Digital",
    description="Reproducible environment for prompt engineering portfolio",
)
