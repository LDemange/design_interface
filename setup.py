from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='design_interface',
      version="0.0.9",
      description="Design Interface",
      license="MIT",
      author="L.D.",
      author_email="demange.louis@hotmail.fr",
      url="https://github.com/LDemange",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
