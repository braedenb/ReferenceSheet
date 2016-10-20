all: reference.py reference.java

reference.py:
	find . -name "*.py" | grep -v reference.py | xargs cat > reference.py

reference.java:
	find . -name "*.java" | grep -v reference.java | xargs cat > reference.java

clean:
	rm -rf reference.py reference.java
