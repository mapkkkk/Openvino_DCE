# 零参照深度曲线估计用于低光图像增强

## 要求
1. Python 3.9
2. Pytorch
3. opencv  
4. torchvision
5. cuda

零参照（Zero-DCE）不需要特殊的配置，只需要基本的环境。 

### 文件结构  
首先下载Zero-DCE_code。
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

在Zero-DCE_code文件夹中：
```
cd Zero-DCE_code
python lowlight_test.py 
```
脚本将处理"data"文件夹下子文件夹中的图片，并在"data"文件夹内创建一个新文件夹"result"。你可以在这个"result"文件夹里找到增强后的图像。

### 训练：  
1) cd Zero-DCE_code

2) 下载训练数据 <a href="https://drive.google.com/file/d/1GAB3uGsmAyLgtDBDONbil08vVu5wJcG3/view?usp=sharing">google drive</a> 或者 <a href="https://pan.baidu.com/s/11-u_FZkJ8OgbqcG6763XyA">百度云 [密码: 1234]</a>

3) 下载并把下载的"train_data"文件夹放到"data"文件夹里，然后执行：
```
python lowlight_train.py 
```