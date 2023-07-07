.PHONY: start
# Automate first install
start:
	@echo ">>> Starting project"
	@echo " \n >>> Creating directorys"
	@mkdir tmp/
	@mkdir tmp/pictures
	@echo ">>> Creating Venv"
	@python3 -m venv venv
	@source venv/bin/activate
	@pip3 install -r requirements.txt
	@cp env.config env


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


.PHONY: phrase
# update phrase
phrase:
	@echo ">>> Updating env phrase..."
	@python3 src/helpers/env_update.py -t "phrase"


.PHONY: section
# update section
section:
	@echo ">>> Updating env section..."
	@python3 src/helpers/env_update.py -t "section"



.PHONY: months
# update months
months:
	@echo ">>> Updating env months..."
	@python3 src/helpers/env_update.py -t "months"