## Weedout's Website


### Overview:
The Weedout website provides a user-friendly GUI for the Weedout package's preprocessing pipeline. Users answer brief questions about their preprocessing needs and upload their dataset. The site then processes the data and returns a zip file with the preprocessed CSV, along with a summary of applied techniques and functions.

https://www.weedout.tech/

### Tech Stack:
- Server : NGINX, Gunicorn, Flask
- Front-end : HTML, CSS, Bootstrap
- Deployment : EC2
- Testing : BDD (Behave)

### Commands to run locally:
- Clone the repo to your personal computer.
- ```bash
  # cd into the repo
  
  cd weedout-website
  
  #Install Requirements
  
  pip install requirements.txt
  
  ```
- ```bash
  # Run the Server Cmd Line
  
  python main.py

  ----- or ------

  make run
  
  ```



