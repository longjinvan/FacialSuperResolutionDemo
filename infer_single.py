# -*- coding: utf-8 -*-
"""
# @Time    : 2022/12/10 17:42
# @Author  : Bill
# @File    : infer_single.py
# @Comment : Null
"""
import torch
import data as Data
import model as Model
import core.logger as Logger
import core.metrics as Metrics

def infer_single_image():
    args = {
        "config": "./config/sr_sr3_16_128.json",
        "phase": "val",
        "gpu_ids": "0",
        "enable_wandb": False,
        "debug": False
    }
    opt = Logger.parse(args)
    # Convert to NoneDict, which return None for missing key.
    opt = Logger.dict_to_nonedict(opt)

    # logging
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True

    # dataset
    for phase, dataset_opt in opt['datasets'].items():
        if phase == 'val':
            val_set = Data.create_dataset(dataset_opt, phase)
            val_loader = Data.create_dataloader(
                val_set, dataset_opt, phase)

    diffusion = Model.create_model(opt)

    diffusion.set_new_noise_schedule(
        opt['model']['beta_schedule']['val'], schedule_phase='val')

    idx = 0

    final_img = None
    for _, val_data in enumerate(val_loader):
        idx += 1
        diffusion.feed_data(val_data)
        diffusion.test(continous=True)
        visuals = diffusion.get_current_visuals(need_LR=False)
        sr_img = visuals['SR']
        final_img = Metrics.tensor2img(sr_img[0])
    return final_img

