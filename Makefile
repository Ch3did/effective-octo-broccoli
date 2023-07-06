# TODO: Create an start to use in firts run

.PHONY: start
# Automate first install
start:
	@echo ">>> Starting project"
	@echo " \n >>> Creating directorys"
	@mkdir tmp/
	@mkdir tmp/pictures
	@echo ">>> Creating Venv"
	@python3 -m venv .venv
	@source .venv/bin/activate
	@pip3 install requirements.txt
	@cp env.credentials .env


.PHONY: run
# run process
run:
	@python3 tasks.py


.PHONY: folders
# create folders process
folders:
	@echo ">>> Creating dowload folders"
	@mkdir tmp/
	@mkdir tmp/pictures