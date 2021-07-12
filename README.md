# 欧洲卡车模拟器 2 模组模板
## 获取与初始化
您可以通过 Git 克隆或下载 zip 文件获得模板文件夹。如果您获得的是压缩格式的文件夹，请先解压。

您需要下载 [Mod Studio](https://www.mods.studio/) 来制作涂装。

请注意，建议您解压后，复制一份本文件夹。然后，填写 `config.toml`。

TOML 文件中 `tailers` 项，表示的是适配的挂车类型，填写规则请参见 [挂车命名规则](#挂车命名规则) 一节。


## 目录结构
目录            | 说明
----------------|------------
`assets`        | 存放最终用于生成模组的文件，若不存在请创建
`assets_raw`    | 存放下载下来的素材；其中的 `scs` 文件夹包含了所有的涂装模板
`dist`          | 存放生成文件的最终目录
`dist/v<v>.scs` | 最终生成的 `scs` 格式的模组文件，`v` 为版本号（该文件是导出模组时应选择的导出路径）
`dist/workshop` | 存放生成文件的最终目录，用于上传创意工坊
`icons`         | 存放相关图标

**图标与图片要求**
文件                | 大小  |说明
--------------------|-------|------------
`icons/workshop.jpg`|640x360| Steam 创意工坊的封面
`icons/mod_icon.jpg`|276x162| 游戏内“模组管理器”显示的图片
`icons/paint_*.png` |256x64 | 游戏内购买涂装时，显示的图片，强烈建议只有左边 150px 有内容，右边留为透明。

## 模组制作流程
 1. **确保正确配置好 `config.toml` 文件**
 2. 修改 `README_STEAM.txt`，填写基本的模组信息
 3. 运行 `make_desc.py`，生成 `mod.ms2` 文件
 4. 启动 Mod Studio，**切记不要双击 `mod.ms2` 启动，而是在开始菜单启动**
 5. Mod 基本信息已经填写完毕，如有需要可以按需要修改。
 6. 制作 `icons/mod_icon.jpg` 文件
 7. 左上角 `Add Template` 选择 `Trailer Skin`，增加挂车涂装部分
    1. Trailer 页：选择挂车类型，一般是 `SCS Box` 即可
    2. Basic 页
        - Internal Name，内部材质名称，推荐命名方式 `jcz_8为哈希`
        - Skin Name，皮肤显示名称，可以填中文
        - Price，皮肤价格，不能为 0
        - Base Color，基颜色，可以不选，除非游戏中出现比较大的错误
    3. Icon 页：制作好 `icons/paint_*.png` 图片并选择。
    4. Images 页：选择材质，右边根据 `config.toml` 选择正确的挂车类型
 8. Export Mod，建议存放在 `dist/v<x.y.z>.scs` 。然后把 `scs` 文件丢进 `%userprofile%\Documents\Euro Truck Simulator 2\mod` 进行调试。**记得截张图，以备以后使用。**
 9. 制作 `icons/workshop.jpg`。
 9. 调试完成后，再次修改 README，预先算好开源发布地址并填入。记得再次执行 `make_desc.py`，然后生成最终的 `scs` 文件。
 11. 运行 `make_publish.py` 进行发布。
     1. Folder 选择 `dist/workshop`
     2. Preview Image 选择 `icons/workshop.jpg`
     3. 填入 `config.toml` 中的名称，左侧 Type 如果是涂装选择 Trainlers，选择正确的分类。
     4. 将 `READM_STEAM_OUT.txt` 的内容黏贴到说明栏中。
     5. 在 Workshop 中更改语言。
     6. 在开源页面进行发布。



## 挂车命名规则
```
<挂车类型><挂车长度><挂车功能>
```

如：`["D136N", "D78M"]`

**挂车类型**
Code | Description
-----|------------
`C`  | Curtain
`D`  | Dry Van
`I`  | Insulated
`F`  | Refrigerated
`T`  | Food Tank (Apply to SCS Food Tank Cylinder Model only)

**挂车长度**
Length| Description
------|------------
`2`   | Full length food tank (Apply to SCS Food Tank Cylinder Model only)
`136` | Full length trailer
`78`  | Half length trailer, for semi-trailer & short trailer of B-Double

**挂车功能**
Code | Description
-----|------------
`N`  | Normal
`B`  | B-Double
`M`  | Moving Floor
`S`  | Side Door
`C`  | Chrome (Apply to SCS Food Tank Cylinder Model only)

## 版权协议
请在制作模组时，注意相关版权、商标权、专利权的规定。

除了 `assets/SCS` 文件夹的内容，是由 SCS Software 所著并授权模组创作者使用外，其他文件均为本人所著。

本模板所有本人所著文件均采用 `绫依公共许可证（第一版）` ，详情请参见 `LICENSE` 文件。
