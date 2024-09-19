'''
Section 3: illustration of code on Temperature dataset

'''
# Load data
from PyTimeVar.datasets import temperature
import numpy as np
data = temperature.load(
    regions=['World'], start_date='1961', end_date='2023')
vY = data.values
mX = np.ones_like(vY)

# set seed
np.random.seed(123)

# illustrate LLR
from PyTimeVar import LocalLinear
model = LocalLinear(vY, mX)
betaHatLLR = model.fit()

# print summary
model.summary()

# plot trend and data
model.plot_predicted(tau=[0.4,0.8])

# plot confidence bands using LBWB
S_LB, S_UB, P_LB, P_UB = model.confidence_bands(bootstrap_type='LBWB', Gsubs=None, plots=True)

# auxiliary LLR model to illustrate kernel, bandwidth selection, and tau
model2LLR = LocalLinear(vY, mX, kernel='Gaussian', bw_selection='lmcv_8')
beta_hat_model2 = model2LLR.fit()

# illustrate boosted HP filter
from PyTimeVar import BoostedHP
bHPmodel = BoostedHP(vY, dLambda=1600, iMaxIter=100)
bHPtrend, bHPresiduals = bHPmodel.fit(
    boost=True, stop="adf", dAlpha=0.05, verbose=False)
bHPmodel.summary()
bHPmodel.plot()

# illustrate power-law trend
from PyTimeVar import PowerLaw
PwrLaw = PowerLaw(vY, n_powers=1)
pwrTrend, pwrGamma = PwrLaw.fit()
PwrLaw.summary()
PwrLaw.plot()

# auxiliary power-law model to illustrate options
vgamma0 = np.arange(0, 0.1, 0.05)
options = {'maxiter': 5E5, 'disp': False}
bounds = ((0,0),(-0.4, 9), )
auxPwr = PowerLaw(vY, n_powers=2, vgamma0=vgamma0, bounds=bounds, options=options)
auxPwrTrend, auxPwrGamma = auxPwr.fit()
auxPwr.summary()

# illustrate Kalman smoother
from PyTimeVar import Kalman
kalmanmodel = Kalman(vY=vY)
[kl_filter, kl_predictor, kl_smoother] = kalmanmodel.fit('all')
kalmanmodel.plot(individual=False)

# # illustrate GAS model
from PyTimeVar import GAS
N_gasmodel = GAS(vY=vY, mX=mX, method='gaussian', niter=10)
N_GAStrend, N_GASparams = N_gasmodel.fit()
N_gasmodel.plot()


# from PyTimeVar.datasets import co2
# import numpy as np
# data = co2.load(
#     regions=['Austria'], start_date='1900', end_date='2023')
# vY = data.values
# mX = np.ones_like(vY)

# from PyTimeVar import Kalman
# kalmanmodel = Kalman(vY=vY)
# [kl_filter, kl_predictor, kl_smoother] = kalmanmodel.fit('all')
# kalmanmodel.plot(individual=True, tau=[0.1, 0.5])
# kalmanmodel.summary()

