import open3d as o3d

# Define txt file
txt = '../OUTPUT/surface_unknown.txt'

pcd = o3d.io.read_point_cloud(txt, format='pts')
o3d.io.write_point_cloud(txt.replace('txt', 'ply') , pcd)

print('converted from txt to ply')