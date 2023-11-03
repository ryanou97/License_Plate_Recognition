# License_Plate_Recognition 車牌辨識專案
這是一個用於車牌辨識的Python程式，使用Azure的認知服務與OpenCV根據攝影機即時畫面進行車牌識別。

## 如何使用
### 事前準備

1. 安裝套件
```bash
   pip install opencv-python, requests
```

- base的部分結尾要加上 'vision/v2.0'
  
  ![image](./images/base_notice.png)

### API配置
需要設置 Azure 認知服務的API key和base。我將這些資訊另外存儲在 API_info.py 文件中。
```python
base = 'YOUR_AZURE_ENDPOINT'
key = 'YOUR_AZURE_SUBSCRIPTION_KEY'
```

### 操作
1. 執行程式
2. 待出現攝影畫
3. 將欲辨識的車牌放至攝影機前
4. 按下"S"或"s"可儲存畫面並進行車牌辨識
5. 按下"Q"或"q"可結束程序

## 成果
成功辨識出車牌
  ![image](./images/demo.png)
