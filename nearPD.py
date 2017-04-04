import numpy as np
import warnings

def nearestSPD(A,testPD=False,ModIfNotPD=False):
#########################################################################################
#	This is a python implementation of the Matlab code by John D'Errico		#
#				that can be found at:					#
#	https://www.mathworks.com/matlabcentral/fileexchange/42885-nearestspd		#
#########################################################################################
#											#
# nearestSPD - the nearest (in Frobenius norm) Symmetric Positive Definite matrix to A	#
#											#
# From Higham: "The nearest symmetric positive semidefinite matrix in the		#
# Frobenius norm to an arbitrary real matrix A is shown to be (B + H)/2,		#
# where H is the symmetric polar factor of B=(A + A')/2."				#
#											#
# http://www.sciencedirect.com/science/article/pii/0024379588902236			#
#											#
# arguments: (input)									#
#  A - 	square matrix, which will be converted to the nearest Symmetric			#
#    	Positive Definite Matrix.							#
#											#
# Arguments: (output)									#
#  Ahat - The matrix chosen as the nearest SPD matrix to A.				#
#########################################################################################

	row=A.shape[0]
	col=A.shape[1]

	if row != col:
		warnings.warn('Matrix A must be square')
		return

	B=0.5*(A+A.T)
	U, S, Vt = np.linalg.svd(B)
        V = Vt.T
	H= V.dot( np.diag(S).dot(V.T) )
	Ahat=0.5*(B+H)
	Ahat=0.5*(Ahat+Ahat.T)
	
	if testPD is False:
		return Ahat
	else:
	#If testPD=True, will test if Ahat is positive definite by trying to Cholesky decomposed. 
	#If not, tweak the matrix
		p=1
		k=0.
		while p!=0:
			try:
				L=np.linalg.cholesky(Ahat)
				p=0
				return Ahat,True
			except np.linalg.linalg.LinAlgError:
				
				if ModIfNotPD is False:
					p=0
					return Ahat,False
				else:
				#Ahat is not pos. def. adding diagonal terms
				#might be costly since calculating eigenvalues every time 
					k+=1.
					mineig=np.min(np.linalg.eigvalsh(Ahat))
					Ahat=Ahat+(-mineig*k**2+np.spacing(mineig))*np.identity(row)
