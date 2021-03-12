parse: out.txt
	python3 parse.py
	python3 parse2.py
.PHONY: clean
clean: 
	del *.csv 