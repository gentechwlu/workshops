# Sample Challenges
You can find the two challenges we looked at in the workshop here. Each has file has multiple implementations that give us the same output. You can find the question as a docstring at the top of the file. We suggest that you read it and attempt solving the problem on your own before going through the different solutions.

# Tests
### Unit Tests using unittest
For running tests on all implementations of both questions, simply run the `tests.py` file. 
Alternatively, you can run the following command in the terminal(macOS) or command prompt(Windows):
```
python3 -m unittest tests
```

### Testing manually
You can also test each file/implementation by creating a python file:
```python3
# Example using longestSequence
from Questions.longest_sequence import longestSequence

if __name__ == "__main__":
    lyst = [3,5,6,2,3,4,5]
    output = longestSeqeuence(lyst)
    print(output)
```
