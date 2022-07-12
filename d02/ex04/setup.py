import setuptools

setuptools.setup(
    name="my_minipack",
    version="1.0.0",
    author="bahaas",
    summary="Howto create a package in python.",
    homepage="None",
    author_email="GPLv3",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
