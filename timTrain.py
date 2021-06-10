
import numpy as np
from dataset import Dataset
from train import Trainer
from config import config
import warnings
warnings.filterwarnings("ignore")
import glob
import warnings
warnings.filterwarnings('ignore')

use_cpu = config.use_cpu

print("Parameters defined in config.py:")
for par, val in config.items():
    if not type(config[par]) == type(config):
        print('    {:<30}   {:}'.format(par,val))

print("PSF related: ")
for par, val in config.PSF.items():
    print('    {:<30}   {:<30}'.format(par,val))
    
print("Training related: ")
for par, val in config.TRAIN.items():
    print('    {:<30}   {:<30}'.format(par,val))
    
img_size         = config.img_size * np.array(config.size_factor)
n_num            = config.PSF.Nnum
base_size        = img_size // n_num # lateral size of lf_extra
training_dataset = Dataset(config.TRAIN.target3d_path, config.TRAIN.lf2d_path, config.PSF.n_slices,
                           config.PSF.Nnum, base_size, normalize_mode='percentile')
                           
trainer  = Trainer(training_dataset)
trainer.build_graph(use_cpu)
trainer.train(begin_epoch=0)
