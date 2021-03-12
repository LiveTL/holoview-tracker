parse: out.txt
	python3 parse.py
	python3 parse2.py
collect: test.py
	python3 test.py
.PHONY: clean
clean: 
	del *.csv 