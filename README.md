<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.alamy.com%2Fstock-photo%2Fvms-logo-design.html&psig=AOvVaw1lq22bPbi_10XIFkjvki3V&ust=1701805812696000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCODVverG9oIDFQAAAAAdAAAAABAE" alt="Project logo"></a>
</p>

<h3 align="center">Vendor Management System</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.
    <br> 
</p>

## 📝 Table of Contents

- [Features](#features)
- [Prerequisites](#features)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 Features <a name = "features"></a>

- **User Authentication:** Secure login and authentication system for authorized access.
- **Vendor Management:** Add, edit, and delete vendor information with ease.
- **Performance Metrics:** Real-time performance metrics to evaluate vendor effectiveness.
- **Django Framework:** Utilizes the Django web framework for robust and scalable development.
- **Docker Integration:** Easy deployment and containerization with Docker.

## 🧐 Prerequisite <a name = "prerequisite"></a>

Ensure you have the following installed before running the application:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/downloads)


## 🏁 Getting Started <a name = "getting_started"></a>

To get started we have to clone the project repository on our local machine using following commands on your terminal/cmd :
```bash
git clone https://github.com/sumeetptl/vms.git

```
Change current directory to project directory on your terminal:
```bash
cd vms
```
Next, we will see installation step for this project.



### Installing

A step by step series of examples that tell you how to get a development env running.

Create a virtual environment for our project dependancy

```bash
python3 -m venv "your-virtual-envirnoment-name"
```
Activate virtual environment using following command

```bash
. your-virtual-environment\\bin\\activate 
```
Now let's install dependancies using following command

```bash
pip install -r requirements.txt
```
Not we have our project dependancies installed, let's get into running actual project on your local system.

Making migrations files for our database
```bash
python manage.py makemigrations
```
Now migrate those files to database
```bash
python manage.py migrate
```

Creating a superuser to access admin panel
```bash
python manage.py createsuperuser
```
This will prompt in your terminal to provide username, email and password for your superuser.

Running your project in your local machine 
```bash
python manage.py runserver
```
If you see following prompt on your terminal,
<pre class="code_syntax" style="color:#000000;background:#ffffff;"><span class="line_wrapper">Watching <span style="color:#800000; font-weight:bold; ">for</span> <span style="color:#400000; ">file</span> changes <span style="color:#800000; font-weight:bold; ">with</span> StatReloader</span>
<span class="line_wrapper">Performing system checks<span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper">System check identified no issues <span style="color:#808030; ">(</span><span style="color:#008c00; ">0</span> silenced<span style="color:#808030; ">)</span><span style="color:#808030; ">.</span></span>
<span class="line_wrapper">December <span style="color:#008c00; ">05</span><span style="color:#808030; ">,</span> <span style="color:#008c00; ">2023</span> <span style="color:#44aadd; ">-</span> <span style="color:#008c00; ">10</span><span style="color:#808030; ">:</span><span style="color:#008c00; ">56</span><span style="color:#808030; ">:</span><span style="color:#008c00; ">29</span></span>
<span class="line_wrapper">Django version <span style="color:#008000; ">5.0</span><span style="color:#808030; ">,</span> using settings <span style="color:#0000e6; ">'vms.settings'</span></span>
<span class="line_wrapper">Starting development server at http<span style="color:#808030; ">:</span><span style="color:#44aadd; ">//</span><span style="color:#008000; ">127.0</span><span style="color:#808030; ">.</span><span style="color:#008000; ">0.1</span><span style="color:#808030; ">:</span><span style="color:#008c00; ">8000</span><span style="color:#44aadd; ">/</span></span>
<span class="line_wrapper">Quit the server <span style="color:#800000; font-weight:bold; ">with</span> CONTROL<span style="color:#44aadd; ">-</span>C<span style="color:#808030; ">.</span></span></pre>
Congratulations you've succesfully installed and deployed your project on your local machine.
You can access the following using given urls:
Admin:
http://127.0.0.1:8000/admin/
To access api documentation:
http://127.0.0.1:8000/api/swagger-ui/#/


## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
