Overview
========
This guide outlines all dependencies and steps required to set up the Airflow ETL Pipeline project on any new computer.

Prerequisites & Dependencies
============================

Step 1: Install Docker Desktop
-------------------------------
- Download Docker Desktop from https://www.docker.com/products/docker-desktop
- Install and run Docker Desktop
- Verify installation: `docker --version`

Step 2: Install Windows Subsystem for Linux (WSL)
--------------------------------------------------
- Open PowerShell as Administrator
- Run: `wsl --install` (installs WSL2 with Ubuntu by default)
- Restart your computer
- Verify installation: `wsl --version`

Step 3: Install Astro CLI
--------------------------
- Install Node.js from https://nodejs.org/ (LTS version recommended)
- Verify Node.js: `node --version` and `npm --version`
- Install Astro CLI: `npm install -g @astrojs/cli`
- Verify installation: `astro --version`

Step 4: Clone the Repository
-----------------------------
- Navigate to your desired directory
- Run: `git clone <repository-url>`
- Navigate into the project: `cd Airflow_ETL_pipeline`

Step 5: Initialize Astro Project
--------------------------------
- Run: `astro dev init`
- This initializes the Astro project structure

$ astro dev init
Initialized empty Astro project in D:\Project\Airflow-learning\Airflow_ETL_pipeline

Step 6: Write Code Logic
-------------------------
- Create DAGs in the `dags/` folder
- Write your ETL pipeline logic
- Test locally with `astro dev start`

Step 7: Common Astro CLI Commands & Their Purpose
--------------------------------------------------

**astro dev start**
- Purpose: Starts the Airflow development environment locally
- How it works: Initializes Docker containers for Scheduler, Webserver, and Postgres
- Access Airflow UI: http://localhost:8080
- Default credentials: Username: admin, Password: admin

**astro dev stop**
- Purpose: Stops all running Airflow development containers
- How it works: Gracefully shuts down the Docker services without removing volumes
- Use when: You want to pause development without losing data

**astro dev restart**
- Purpose: Restarts the Airflow development environment
- How it works: Stops all containers and starts them again
- Use when: You made changes to requirements.txt or Dockerfile and need to rebuild
- Equivalent to: Running `astro dev stop` followed by `astro dev start`

**astro dev logs**
- Purpose: View logs from running Airflow containers
- How it works: Streams live logs from the Scheduler, Webserver, and Postgres services
- Use when: Debugging DAG issues or monitoring task execution

**astro dev ps**
- Purpose: Shows the status of all running containers in the Airflow environment
- How it works: Displays container names, IDs, and status
- Use when: Checking if services are running properly

**astro deploy**
- Purpose: Deploys your Airflow project to Astronomer cloud
- How it works: Pushes your code to a remote Airflow environment
- Use when: Ready to move from local development to production

**Accessing Airflow Web UI**
- Local development: http://localhost:8080
- Default username: admin
- Default password: admin
- Features available: DAG monitoring, task logs, task scheduling, XCom data

Step 8: Typical Workflow
------------------------
1. Make changes to DAGs in `dags/` folder
2. Run `astro dev start` to start the environment
3. Access http://localhost:8080 to view the Airflow UI
4. Monitor DAG execution and logs
5. Make code updates as needed
6. Run `astro dev restart` if you modified configurations or dependencies
7. Use `astro dev stop` when finished working
