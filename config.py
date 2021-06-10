from easydict import EasyDict as edict

config = edict()
config.TRAIN = edict()
config.PSF = edict()
config.VALID = edict()

config.img_size     = 1984                                                          # LF 2D image size for training
config.size_factor  = [0.125,0.125]                    # Real img_size = img_size * size_factor
config.PSF.n_slices = 61                                                            # Number of z slices of the 3-D reconstruction
config.PSF.Nnum     = 31                                                            # N number of the light field psf
config.n_channels   = 1                                                             # Number of channels of the training and validation data
config.use_cpu      = 1                                                            # to use cpu vs gpu where available
config.TRAIN.batch_size  = 10
config.TRAIN.ckpt_saving_interval = 1

label                             = 'test2'                       # Distingiushable label for saving the checkpoint files and validation result
config.label                      = label

# config.model                      = 'structure'     #normlize_mode='max'
# config.model                      = 'function'      #normlize_mode='constant'
config.model                      = 'beta_v'        # custom(percentile or max ....)
config.normalize_mode             = 'percentile'

config.TRAIN.target3d_path        = 'C:\\Users\\admin\\Dropbox\\Imaging\\beadLibrary05182021\\WF\\'                   # 3-D targets for training
config.TRAIN.lf2d_path            = 'C:\\Users\\admin\\Dropbox\\Imaging\\beadLibrary05182021\\LFrectified_images\\' 
# config.TRAIN.target3d_path        = '/Users/timothyspellman/Dropbox/Python/VCD-Net/vcd-example-data/data/train2/WF/'                   # 3-D targets for training
# config.TRAIN.lf2d_path            = '/Users/timothyspellman/Dropbox/Python/VCD-Net/vcd-example-data/data/train2/LF/' 

config.TRAIN.test_saving_path     = "C:\\Users\\admin\\Dropbox\\Python\\VCD-Net\\vcdnet\\sample\\test2\\{}\\".format(label)
# config.TRAIN.test_saving_path     = "/Users/timothyspellman/Dropbox/Python/VCD-Net/vcdnet/sample/test/{}/".format(label)

config.TRAIN.ckpt_dir             = "C:\\Users\\admin\\Dropbox\\Python\\VCD-Net\\vcd-example-data\\checkpoint\\{}\\".format(label)
# config.TRAIN.ckpt_dir             = "/Users/timothyspellman/Dropbox/Python/VCD-Net/vcd-example-data/checkpoint/{}/".format(label)

config.TRAIN.log_dir              = "C:\\Users\\admin\\Dropbox\\Python\\VCD-Net\\vcdnet\\log\\{}\\".format(label)
# config.TRAIN.log_dir              = "/Users/timothyspellman/Dropbox/Python/VCD-Net/vcdnet/log/{}/".format(label)

config.TRAIN.device               = 0                                               # gpu device used for training, 0 means the 1st device is used.
config.TRAIN.valid_on_the_fly     = False
config.TRAIN.using_edge_loss      = False                                           # use the edges loss to promote the quality of the reconstructions

config.TRAIN.lr_init     = 1e-4
config.TRAIN.beta1       = 0.9
config.TRAIN.n_epoch     = 200
config.TRAIN.lr_decay    = 0.1
config.TRAIN.decay_every = 50

## Inference/Prediction
config.VALID.ckpt_dir             = config.TRAIN.ckpt_dir                          # use trained checkpoint 
config.VALID.lf2d_path            = "E:\\Dropbox\\Python\\VCD-Net\\vcd-example-data\\data\\beads\\beads_Crop1984\\"
config.VALID.saving_path          = "E:\\Dropbox\\Python\\VCD-Net\\vcd-example-data\\data\\beads\\beads_Crop1984_Results"  #config.TRAIN.target3d_path[0:-1]+'_Results/'





