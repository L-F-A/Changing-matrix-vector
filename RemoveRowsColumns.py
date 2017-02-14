import numpy as np

def RemoveRowsColumns(A,ind_r=None,ind_c=None):
#########################################################################################
#      Function that removes rows and columns specified by ind_r and ind_c		#
#											#
#	A     :  Original matrix							#
#	ind_r :  indices of the rows one wants to remove. ex: Remove rows 2 and 4	#
#        	 ind_r = [2,4] none ind_r = None					#
#	ind_c :  indices of the colums one wants to remove. ex: Remove columns 2 and 4	#
#        	 ind_c = [2,4] none ind_c = None					#
#########################################################################################

	if   (ind_c is None) and (ind_r is None):
		return A
	elif (ind_c is None) and (ind_r is not None):
		return np.delete(A,ind_r,0)
	elif (ind_r is None) and (ind_c is not None):
		return np.delete(A,ind_c,1)
	else:
		Btemp = np.delete(A,ind_r,0)
		return np.delete(Btemp,ind_c,1)
