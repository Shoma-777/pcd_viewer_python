import sys, os.path
import open3d

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2:
        print("ファイルまたはディレクトリをひとつだけ選択してください")
        sys.exit(0)

    vis = open3d.visualization.Visualizer()
    vis.create_window("Open3D", 1280, 720)

    path = os.path.abspath(args[1])
    if os.path.isdir(path):
        for p in os.listdir(path):
            vis.add_geometry(open3d.read_point_cloud(path + '/' + p))
    else:
        vis.add_geometry(open3d.read_point_cloud(path))

    vis.run()
    vis.destroy_window()
