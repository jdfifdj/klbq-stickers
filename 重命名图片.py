import os
import re

def rename_png_files(img_folder_path):
    # 遍历img文件夹下的所有子文件夹
    for character_folder in os.listdir(img_folder_path):
        # 构建完整的子文件夹路径
        character_path = os.path.join(img_folder_path, character_folder)
        
        # 检查是否为目录
        if not os.path.isdir(character_path):
            continue
        
        print(f"处理文件夹: {character_folder}")
        
        # 获取文件夹中所有.png-1文件
        png_1_files = []
        for file in os.listdir(character_path):
            # 检查是否为.png-1文件
            if file.endswith('.png-1'):
                png_1_files.append(file)
        
        # 按文件名排序
        png_1_files.sort()
        
        # 重命名文件
        renamed_count = 0
        for old_name in png_1_files:
            # 生成新文件名，去掉-1后缀
            new_name = old_name.replace('.png-1', '.png')
            # 构建完整的文件路径
            old_path = os.path.join(character_path, old_name)
            new_path = os.path.join(character_path, new_name)
            
            # 检查新文件名是否已存在
            counter = 1
            temp_new_path = new_path
            while os.path.exists(temp_new_path):
                # 如果已存在，添加数字后缀
                base_name = os.path.splitext(new_name)[0]
                temp_new_path = os.path.join(character_path, f"{base_name}_{counter}.png")
                counter += 1
            
            # 重命名文件
            os.rename(old_path, temp_new_path)
            print(f"  {old_name} -> {os.path.basename(temp_new_path)}")
            renamed_count += 1
        
        print(f"  共处理了 {renamed_count} 个.png-1文件\n")

if __name__ == "__main__":
    # img文件夹的路径
    img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
    
    # 检查img文件夹是否存在
    if not os.path.exists(img_folder):
        print(f"错误: 找不到img文件夹 '{img_folder}'")
        exit(1)
    
    print(f"开始处理.png-1文件...\n")
    rename_png_files(img_folder)
    print("所有.png-1文件已成功重命名为.png！")