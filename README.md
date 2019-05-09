# Avalanche hazard prediction
### Supervised learning and prediction of terrain-specific avalanche hazard levels.

The approach is based on the following datasets:
- a collection of events with (n~500) and without (n > 2000) reported avalanche release
- spatially interpolated timeseries of SLF danger bulletins
- a digital surface model from which information about the local terrain are calculated

It explores a number of classification algorithms in view of a minimization of false negative rates while keeping the true positive rate as high as possible.

For a description of the projects current state, please open the Jupyter notebook "learning_from_bulletins.ipynb"
