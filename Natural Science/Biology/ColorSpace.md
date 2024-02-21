# 色彩空間

## 生理機制

### 可見光譜(Visible Spectrum)
人類的眼睛有兩種感光細胞：桿狀細胞(rod cell)和錐狀細胞(cone cell)。
* 桿狀細胞
  * 看到的世界是灰階，但是很敏感，比如在夜晚中人眼仍然可以看到周圍的物體。
  * 桿狀細胞偵測範圍大、反應速度快
* 錐狀細胞
  * 能夠檢測到可見光譜中的光，需要較強的光線才能激發
  * 人類只有三種錐細胞，分別是紅色、綠色、藍色。

因此，當有許多不同波長的光結合時，人腦會插值出紅色和藍色之間的顏色。  
然而，如果一種光的波長與紅色和藍色結合，問題在於該顏色不應該是綠色。
為了解決這個問題，人腦創造了洋紅色。

Reference: [这个世界上根本不存在紫色！ ( 眼见为识)](https://www.youtube.com/watch?v=vv79wigS-4I)

### 錐狀細胞敏感度
Green > Red > Blue
<img src="https://qph.cf2.quoracdn.net/main-qimg-de71b9bcbb3a8503ea1b8c968a9f2b29" Height="480" />

## 色彩空間
就像座標系統可能是笛卡爾座標系統或極座標系統一樣，用來描述多為空間的方式。
色彩空間也有許多座標系統用來描述色彩。

### RGB-CMYK
RGB色彩模型是一種加色模型
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Barn_grand_tetons_rgb_separation.jpg/320px-Barn_grand_tetons_rgb_separation.jpg" />

CMYK是一種減色模型  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/CMYK_color_swatches.svg/150px-CMYK_color_swatches.svg.png" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/CMYK_subtractive_color_mixing.svg/150px-CMYK_subtractive_color_mixing.svg.png" />

### [YUV Space](https://en.wikipedia.org/wiki/YUV)
軟體工程，YUV常拿來作影響壓縮，因為人眼的桿細胞因素，人眼對灰階更敏感。
這時候其實色彩跟亮度可以分開處理，亮度敏感不壓縮，色彩較為不敏感，可壓縮色彩。
因此，在傳統相機空間中會嘗試分離灰色和其他顏色。
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Barn-yuv.png/200px-Barn-yuv.png" />

RGB和YUV可以通過矩陣計算，所以是等價空間。

### HSL, HSV Space
HSL和HSV有點像YUV。HSL和HSV也有一個軸是亮度。

* H代表色調，使用0到360度來表示所有顏色
* S是飽和度
* L是亮度
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Hsl-hsv_models.svg/290px-Hsl-hsv_models.svg.png" />

HSL和HSV是等價空間，但是HSL和YUV不是等價空間。

### CIE Space
CIE (International Commission on Illumination) CIE（國際照明委員會）是關於人類視覺的色彩空間。

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/CIE1931xy_gamut_comparison.svg/800px-CIE1931xy_gamut_comparison.svg.png" Height="480" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Colorspace.png/220px-Colorspace.png" Height="480" />

### CIE-LAB space
xyz空間家族，LAB空間也有一個L軸代表亮度，AB軸類似於XY座標系統。  
最重要的是，它同樣屬於CIE，與人眼的敏感度相關的色彩空間。

<img src="https://i.imgur.com/sTDteRp.jpg" />
<img src="https://sensing.konicaminolta.asia/wp-content/uploads/2018/09/Apple%20ab%20Chart.jpg" />


---
tags:
  - [[Color]]
  - [[Biology]]
  - [[Physics]]
  - [[眼见为识]]
  
---