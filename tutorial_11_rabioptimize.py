from matplotlib import pyplot
import sys
sys.path.append('../paraqasmqubic/submodules/qubic/src/')
from qubic.qcvv.rabioptimize import c_rabioptimize
calirepo='submodules/qchip'

rabioptimize=c_rabioptimize(qubitid=sys.argv[1],calirepo=calirepo,debug=3,gmixs=None,plot=True)
print(rabioptimize.optimize(nsample=50,disp=3))
pyplot.ioff()
pyplot.show()
