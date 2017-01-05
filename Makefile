FILES = a b c d e


help:
	@echo "Usage: 'make <target>' where <target> is one of:"
	@echo " help        print help"
	@echo " clean       remove sources"
	@echo " prepare     create sources from templates"
	@echo " parse       run Hightail parser in background"
	@echo " compete     'clean' && 'prepare' && 'parse'"
	@echo " train       create test sources"

.PHONY : help

clean:
	@rm src/*.cpp 2>/dev/null || true
	@rm src/*.py 2>/dev/null || true

.PHONY : clean

prepare:
	@for file in $(FILES); do cp lib/cpp/_template.cpp src/$$file.cpp; done
	@for file in $(FILES); do cp lib/py/_template.py src/$$file.py; done

.PHONY : prepare

parse:
	@(cd bin/ && java -jar Hightail-v0.9.4.jar)&

.PHONY : parse

compete: clean prepare parse
	@echo Good luck!

.PHONY : compete

train: clean
	@cp lib/cpp/_template.cpp src/main.cpp
	@cp lib/py/_template.py src/main.py

.PHONY : train
