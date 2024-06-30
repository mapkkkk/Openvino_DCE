# 零参照深度曲线估计用于低光图像增强

## 要求
1. Python 3.9
2. Pytorch
3. opencv  
4. torchvision
5. cuda

### 文件结构  
首先下载Openvino_DCE。
以下是基本的文件夹结构。

```
├── data
│   ├── test_data # 测试数据。你可以为你的测试数据创建一个新的文件夹，如LIME、MEF和NPE。
│   │   ├── LIME 
│   │   └── MEF
│   │   └── NPE
│   └── train_data 
├── lowlight_test.py # 测试代码
├── lowlight_train.py # 训练代码  
├── model.py # Zero-DEC网络
├── dataloader.py
├── snapshots
│   ├── Epoch99.pth # 一个预训练的快照（Epoch99.pth）
```

### 测试：

在Openvino_DCE文件夹中：
```
cd Openvino_DCE
python lowlight_test.py 
```
脚本将处理"data"文件夹下子文件夹中的图片，并在"data"文件夹内创建一个新文件夹"result"。你可以在这个"result"文件夹里找到增强后的图像。

### 训练：  
1) cd Openvino_DCE

2) 下载训练数据

3) 下载并把下载的"train_data"文件夹放到"data"文件夹里，然后执行：
```
python lowlight_train.py 
```