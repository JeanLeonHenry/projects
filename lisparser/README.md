# lisparser

Goals :
1. parsing simple math expressions in Lisp
2. pretty printing them

## Goal 1
Given `"(+ (* 3 5) (/ 8 4))"` the program should output the result of $(3\times5)+(8/4)$, i.e. $17$.

## Goal 2
Given `"(+ (* 3 5) (/ 8 4))"` the program should output
```python
(+ (* 3 5)
   (/ 8 4)
)
```

## Notes
- Use [external lib](https://github.com/mar10/nutree/) to handle tree implementation ?
