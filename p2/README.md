# Logs Analysis

## About
3 questions are asked,which are answered from psql database.

## To Run
install the following-

- Python3
- VirtualBox
- Vagrant

### Setup
- after installing vagrant and virtualBox, go to the vagrant directory of the given zipped file using terminal.
- Launch Vagrant VM by running 'vagrant up', now you can the log in using 'vagrant ssh'.
- To load the data, use the command 'psql -d news -f newsdata.sql'.

### Execution
To execute the program, run 'python news_log.py' on the command line.