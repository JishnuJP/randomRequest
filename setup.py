import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='random_request',  
     version='0.1',
     scripts=['randomRequest'] ,
     author="Jishnu Jayaprakash",
     author_email="jishnujprksh007@gmail.com",
     description="A python wrapper for proxy-list api for generating random proxy and a tool to generate random User-Agent",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/JishnuJP/random_request",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
