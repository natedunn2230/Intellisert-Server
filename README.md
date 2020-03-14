# Intellisert Server
#### Group 14
#### CEG-4981
Flask Server for handling requests to drive the Intellisert device.

### Running Locally
1. Install Virtualenv: `pip install virtualenv`
    * [Virtualenv](https://virtualenv.pypa.io/en/latest/) allows one to run an application with an isolated Python environment. When enabled, packages can be installed to a specific environment and programs can be executed within its scope. This prevents installing pip packages to the system's Python environment.
2. Navigate to Intellisert-Server/ and create a virtual python environment (named venv): `cd Intellisert-Server; virtualenv venv --python=python3.7` *(Install python3.7 if not installed)*
3. Enable the virtual environment: `source venv/bin/activate` *(should see (venv) on at beginning of terminal prompt when activated)*
    * To deactivate: `deactivate`
4. Install necessary packages: `pip install -r requirements.txt`
5. Run in development mode: `python run.py`
6. If operating through ssh, pull up your favorite browser and navigate to *Intellisert's-IP-address:5000* to hit the home endpoint of server. If operating directly on device, navigate to *0.0.0.0:5000*
### Running as a Service in Production
   * Follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) from DigitalOcean
