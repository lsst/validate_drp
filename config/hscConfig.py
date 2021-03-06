# We do not have transmission curves attached to our validation repos yet
config.processCcd.isr.doAttachTransmissionCurve = False
# these commissioning data do not have the correct header info to apply the stray light correction
config.processCcd.isr.doStrayLight = False
# Run meas_modelfit to compute CModel fluxes
# Not strictly necessary as it's imported in obs_subaru by default but better to be safe
import lsst.meas.modelfit
config.processCcd.calibrate.measurement.plugins.names |= [
    "modelfit_DoubleShapeletPsfApprox", "modelfit_CModel"]
config.processCcd.calibrate.measurement.slots.modelFlux = 'modelfit_CModel'
