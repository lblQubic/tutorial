from matplotlib import pyplot
import numpy
from qubic.qubic import experiment 
from qubic.qcvv.plot import plot
from qubic.qcvv.fit import fit
import scipy.optimize

qubitid=sys.argv[1]
dragalpha=c_dragalpha(qubitid=qubitid,calirepo='submodules/qchip')
if 0:
	dragalpha.seqs(alphas=numpy.arange(-0.2,0.2,0.01))
	dragalpha.run(400)
	print(dragalpha.fit())
else:
	updatedict=dragalpha.optimize(500)#,alphas=numpy.arange(-5,5,0.2)))
	print(updatedict)
	dragalpha.opts['qchip'].updatecfg(updatedict,'cali/qubitcfg_X6Y3.json')
fig1=pyplot.figure(figsize=(15,15))
sub=fig1.subplots(1,1)
dragalpha.plot(fig=sub)
pyplot.show()

