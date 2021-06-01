# transpi

transpi is a translation tool.

### quick use

first `pip install transpi`, then:

```python
import transpi
result = transpi.trans("human")
print(result)

# or use different engine
result2 = transpi.trans("human", engine="bing")
print(result2)
```