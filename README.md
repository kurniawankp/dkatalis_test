# Dkatalis Technical Test

This is an instruction to run this program.


## General Instruction

To use this code, you can use this following instruction

I recommend to use virtual environment

* install required package by using requirements.txt

    ```bash
    pip install -r requirements.txt
    ```
* create folder data and put all csv file into data/ folder
## Task 1
* open jupyter lab

    ```bash
    jupyter-lab
    ```
* open database.json and fill the credential information with yours.

    ```bash
    {
        "POSTGRES_USER":"your_database_user",
        "POSTGRES_PASSWORD":"your_database_password",
        "POSTGRES_DB":"your_database_name",
        "POSTGRES_SCHEMA":"your_database_schema",
        "POSTGRESS_HOST":"your_database_host"
    }
    ```
* change master_folder path in jupyter-lab with your current path

    ```bash
    master_folder = 'your/current/path'
    ```
## Task 2
* Change master_folder value in line 17 with your current path

    ```bash
    master_folder = 'your/current/path'
    ```
* open terminal and type this command

    ```bash
    python app.py
    ```
## Task 3
* open task_3.txt
