import numpy as np

class RescaleVectors:
	def __init__(self):
		pass

	def Rescale(self,X,new_min,new_max):
	#Rescaling:
        #This function rescales values so that the vector in a matrix contains values in
        #the range new_min <= xx <= new_max

		SizeX = X.shape
                X_resc = np.ones(SizeX)
                pdim = SizeX[1]
		MinVec = []
		MaxVec = []
		MultFacVec = []
		for i in range(pdim):
			old_min = np.min(X[:,i])
			old_max = np.max(X[:,i])
			MinVec.append(old_min)
			MaxVec.append(old_max)
			mult_fac = (new_max-new_min)/(old_max-old_min)
			MultFacVec.append(mult_fac)
			X_resc[:,i] = mult_fac*(X[:,i]-old_min) + new_min;
		self.X = X_resc
		self.MIN = MinVec
		self.MAX = MaxVec
		self.MULTFACT = MultFacVec

	def Standardization(self,X):
	#Standardization: difference with mean value divided by the
        #standard deviation

		mean_p = []
    		std_p = []
		SizeX = X.shape
    		X_stand = np.ones(SizeX)
		pdim = SizeX[1]
    		for i in range(pdim):
        		avgp = np.mean(X[:,i])
        		stdp = np.std(X[:,i])
        		mean_p.append(avgp)
        		std_p.append(stdp)
        		X_stand[:,i] = (X[:,i] - avgp)/stdp
    			
		self.X = X_stand
		self.MEAN = mean_p
		self.STD = std_p
