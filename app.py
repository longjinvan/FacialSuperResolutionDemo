# -*- coding: utf-8 -*-
"""
# @Time    : 2022/12/7 22:46
# @Author  : Bill
# @File    : app.py.py
# @Comment : Null
"""
import os

import gradio as gr
import PIL
from infer_single import infer_single_image
from PIL import Image

def greet():
    return "hello world!"

def inference(img, gain):
    file_list = os.listdir("./dataset/user/lr_16")
    if len(file_list) > 0:
        os.remove("./dataset/user/lr_16/test.png")
        os.remove("./dataset/user/hr_128/test.png")
        os.remove("./dataset/user/sr_16_128/test.png")
    img_large = img.resize((128, 128), resample=PIL.Image.CUBIC)
    img.save("./dataset/user/lr_16/test.png")
    img_large.save("./dataset/user/hr_128/test.png")
    img_large.save("./dataset/user/sr_16_128/test.png")
    out = infer_single_image()
    out = Image.fromarray(out)
    if gain == '2x':
        out = out.resize((32, 32), resample=PIL.Image.CUBIC)
    elif gain == '4x':
        out = out.resize((64, 64), resample=PIL.Image.CUBIC)
    return out

title = "Face Super-Resolution"
description = "Gradio Demo for face super-resolution"

demo = gr.Interface(
    fn=greet,
    inputs=[gr.inputs.Image(type="pil"), gr.inputs.Radio(['2x', '4x', '8x'], type="value", default='2x', label='Gain')],
    outputs=gr.outputs.Image(type="pil"),
    title=title,
    description=description,
    allow_flagging="never")
demo.launch()