import os
import datetime
from matplotlib import pyplot
import numpy
import sys
sys.path.append('../..')
from qubic.qubic import experiment
from qubic.qcvv.plot import plot
from qubic.qcvv.fit import fit
from qubic.qcvv.tcr import c_tcr

t0=datetime.datetime.now()
qubitid=['Q1','Q2']
qubitid=['Q0','Q1']
qubitid=['Q3','Q2']
tcr=c_tcr(qubitid=qubitid,calirepo='submodules/qchip')#,debug=2)
tcrlist=numpy.arange(80e-9,640e-9,8e-9)
repeat=1
if 1:
	ampcr=[0.5]#numpy.arange(0.1,1.0,0.1)
	rcrtgt=numpy.zeros(len(ampcr))
	rcrctl=numpy.zeros(len(ampcr))
#	pyplot.figure('cr')
	pyplot.ion()
	for ia,amp in enumerate(ampcr):
		tcr.seqs(tcrlist=tcrlist,repeat=repeat,amp=amp)
		tcr.run(50,combineorder=qubitid)
		result=tcr.fit()
		rcrtgt[ia]=result[qubitid[1]]['amp']
		rcrctl[ia]=result[qubitid[0]]['amp']
		tcr.plot(plotfit=True)
		pyplot.draw()
		print(ia,amp,rcrtgt[ia],result[qubitid[1]]['firstmaxt'],max(tcr.r[qubitid[1]]['1']))
		pyplot.pause(0.1)
	pyplot.ioff()
#	pyplot.figure('rcr')
#	pyplot.plot(ampcr,rcrtgt)
#	pyplot.plot(ampcr,rcrctl)
#	print(ampcr,rcrtgt,rcrctl)
	pyplot.show()
#	print('tcr',result)
#	pyplot.show()
if 0:
	tcrsel=288e-9#max(numpy.ceil(result[qubitid[1]]['firstmaxt']/16e-9)*16e-9,256e-9)
	print(tcrsel)
	updatedict=tcr.optimize(nsample=100,tcr=tcrsel,plot=True,nsteps=3,acenter=0.2,aspan=0.1)
	print(updatedict)
	tcr.opts['qchip'].updatecfg(updatedict,'cali/qubitcfg_X6Y3.json')
if 0:
	updatedict=tcr.optimize(nsample=100,tcr=200e-9,plot=True,nsteps=5,acenter=0.7,aspan=0.4)
	print(updatedict)
	tcr.opts['qchip'].updatecfg(updatedict,'cali/qubitcfg_X6Y3.json')
if 0:
	tcr.scanacr(nsample=100,repeat=1,ampchange=numpy.linspace(0,1,40),tcr=288e-9,plot=True)
#		tcr.scanacr(nsample=100,repeat=2,ampchange=numpy.linspace(0,1,40),tcr=256e-9,plot=True)
#	else:
if 0:
	acrs=numpy.linspace(0.3,1.0,10)
	tcrmins=numpy.zeros(len(acrs))
	pyplot.ion()
	fig=pyplot.figure('each')
	for iacr,amp in enumerate(acrs):
		tcr.seqs(tcrlist=tcrlist,repeat=1,amp=amp)
		tcr.run(50,combineorder=qubitid)
		result=tcr.fit()
		print('tcramp',amp,result)
		pyplot.figure('each')
		tcr.plot(plotfit=True)
#			pyplot.show()
		tcrmins[iacr]=numpy.ceil(result[qubitid[1]]['period']/2/16e-9)*16e-9
	pyplot.ioff()
	fig=pyplot.figure()
	pyplot.plot(acrs,tcrmins)
	pyplot.show()
	print('tcrmin',tcrmins)
	tcrsel=float(input('tcr'))
	updatedict=tcr.optimize(nsample=100,tcr=tcrsel,plot=True,nsteps=2,acenter=0.7,aspan=0.4)
	print(updatedict)
	tcr.opts['qchip'].updatecfg(updatedict,'cali/qubitcfg_X6Y3.json')

	t1=datetime.datetime.now()
	print('tcr time: ', t1-t0)
	sys.stdout.flush()
pyplot.show()
