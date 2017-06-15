try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = "ExpDat",
      version = "0.1",
      packages = ["ExpMap"],
      package_dir = {"ExpMap":"ExpMap"},
      )
