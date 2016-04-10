# figureCut

直接使用pipeline.py中的process函数，输入参数说明
cropperSourceDir: 一个存有cropperSource图片的文件夹，cropper指的是抠出来的子图
holderSourceDir: 一个存有holderSource图片的文件夹，holder指的是抠出来的子图嵌入的宿主
cropperPerImage: 每张cropperSource图片要抠出来的cropper的数量
holderPerCropper: 每个cropper要插入到几个holder中

示例:
```python
import process from pipeline
process('cropperSource', 'holderSource', 10, 1)
```
或
```sh
python pipeline.py cropperSource holderSource 10 1
```

其中cropperSource和holerderSource是该Repo中自带的测试文件夹。
程序运行后会产生额外4个文件夹
cropperSourceResized: 存放resized好的cropperSource图片
holderSourceResized: 存放resized好的holderSource图片
cropperPoolDir: 存放截取下来的cropper
embeddedPoolDir: 存放最终合成的图片
