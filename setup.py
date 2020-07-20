  
from setuptools import setup, find_packages

setup(
  name="bezier_decay", 
  version="0.1.0",
  author="Leon Shams",
  description="A simple program for creating bezier curves for complex decay.", 
  url='https://github.com/schaall/Bezier-Decay.git',
  author='Leon Shams',
  license='MIT',
  packages=find_packages(),
  python_requires='>=3.6'
  entry_points={
        "console_scripts": [
            "bezier_decay = bezier_decay:bezier_decay",
        ]
    }
)
