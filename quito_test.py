#from quito.quito_coverage import quito
from quito_gpu import quito
import time
start = time.time()
i = 0
quito('/home/xinyi/quito_ex3/as.ini')
end = time.time()

print(end - start)

