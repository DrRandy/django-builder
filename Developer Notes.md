# Setup 

## Assumptions about the workspace

In addition to the installations posted in `requirements.txt`, the environment also should have 
chromedriver installed. This is so that robot tests can be run on it, as described in 
https://pypi.org/project/robotframework-djangolibrary/

I'm thinking that the chromedriver executable could be included in the GitHub repository but that would 
add 10 MB to the download, and I would have to figure out how to add it to PATH with each run. But that 
might make the most sense in the long run if it is going to be self-contained. 