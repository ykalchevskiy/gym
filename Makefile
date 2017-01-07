FILES = a b c d e


help:
	@echo "Usage: 'make <target>' where <target> is one of:"
	@echo " help        print help"
	@echo " clean       remove sources"
	@echo " prepare_cf  create sources from templates for CodeForces"
	@echo " prepare_cs  create sources from templates with cases"
	@echo " parse       run Hightail parser in background"
	@echo " compete_cf  'clean' && 'prepare_cf' && 'parse'"
	@echo " compete_cs  'clean' && 'prepare_cs'"
	@echo " train       create test sources"

.PHONY : help

clean:
	@rm src/*.cpp 2>/dev/null || true
	@rm src/*.py 2>/dev/null || true

.PHONY : clean

prepare_cf:
	@for file in $(FILES); do cp lib/cpp/_template.cpp src/$$file.cpp; done
	@for file in $(FILES); do cp lib/py/_template.py src/$$file.py; done

.PHONY : prepare_cf

prepare_cs:
	@for file in $(FILES); do cp lib/cpp/_template.cpp src/$$file.cpp; done
	@for file in $(FILES); do cp lib/py/_template_cases.py src/$$file.py; done

.PHONY : prepare_cs

parse:
	@(cd bin/ && java -jar Hightail-v0.9.4.jar)&

.PHONY : parse

compete_cf: clean prepare_cf parse
	@echo Good luck!

.PHONY : compete_cf

compete_cs: clean prepare_cs
	@echo Good luck!

.PHONY : compete_cs

train: clean
	@cp lib/cpp/_template.cpp src/main.cpp
	@cp lib/py/_template.py src/main.py

.PHONY : train
