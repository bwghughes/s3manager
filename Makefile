clean:
	rm -r *.pyc

test:
	python test_s3manager.py

cov:
	./bin/coverage html test_s3manager.py