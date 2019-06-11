# pcd_viewer_python
pcd, ply, xyz, xyzrgb, xyzn, ptsの拡張子の点群データを表示だけするツール。

## Usage
```
python pcd_viewer.py ./cloud.pcd
```
上記のように第一引数に読み込みたいデータを指定するとビューワーで表示することができる。  
ディレクトリを指定した場合その中の読み込めるファイルすべてをマージして表示。

### Requirements
- Open3D