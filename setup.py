  
from setuptools import setup, find_packages

setup(
  name="bezier_decay", 
  version="0.1.0",
  description="A simple program for creating bezier curves for complex decay.", 
  url='https://github.com/schaall/Bezier-Decay.git',
  author='Leon Shams',
  license='MIT',
  packages=find_packages(),
  install_requires=["matplotlib", "numpy"],
  python_requires='>=3.6',
  entry_points={
        "console_scripts": [
            "bezier_decay = bezier_decay:bezier_decay",
        ]
    }
)
