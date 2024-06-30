import glob
import os
import numpy as np
import torch
import torch.optim
import torchvision
from PIL import Image
import model
import time


class imgDce:
    def __init__(self):
        self.DCE_net = model.enhance_net_nopool().cuda()
        self.DCE_net.load_state_dict(torch.load('snapshots/Epoch99.pth'))

    def lowlight(self, image_path):
        data_lowlight = Image.open(image_path)
        data_lowlight = (np.asarray(data_lowlight) / 255.0)
        data_lowlight = torch.from_numpy(data_lowlight).float()
        data_lowlight = data_lowlight.permute(2, 0, 1)
        data_lowlight = data_lowlight.cuda().unsqueeze(0)
        _, enhanced_image, _ = self.DCE_net(data_lowlight)
        image_path = image_path.replace('test_data', 'result')
        result_path = image_path
        if not os.path.exists(image_path.replace('/' + image_path.split("/")[-1], '')):
            os.makedirs(image_path.replace('/' + image_path.split("/")[-1], ''))
        torchvision.utils.save_image(enhanced_image, result_path)


if __name__ == '__main__':
    # test_images
    ip = imgDce()
    with torch.no_grad():
        filePath = 'data/test_data/'
        file_list = os.listdir(filePath)
        ts = time.time()
        img_total = 0
        print('Start processing')
        for file_name in file_list:
            test_list = glob.glob(filePath + file_name + "/*")
            img_total += len(test_list)
            for image in test_list:
                ip.lowlight(image)
        te = time.time() - ts
        te = round(te, 2)
        print('Total time:', te, 's')
        print('Total images:', img_total)
        fps = img_total / te
        fps = round(fps, 2)
        print('FPS:', fps)
