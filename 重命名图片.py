import os
import re

def rename_images_in_folder(img_folder_path):
    # 遍历img文件夹下的所有子文件夹
    for character_folder in os.listdir(img_folder_path):
        # 构建完整的子文件夹路径
        character_path = os.path.join(img_folder_path, character_folder)
        
        # 检查是否为目录
        if not os.path.isdir(character_path):
            continue
        
        print(f"处理文件夹: {character_folder}")
        
        # 获取文件夹中所有图片文件
        image_files = []
        for file in os.listdir(character_path):
            # 检查是否为图片文件
            if re.search(r'\.(jpg|jpeg|png|gif|bmp)$', file, re.IGNORECASE):
                image_files.append(file)
        
        # 按文件创建时间排序（也可以按文件名排序）
        image_files.sort(key=lambda x: os.path.getctime(os.path.join(character_path, x)))
        
        # 重命名文件
        for i, old_name in enumerate(image_files, 1):
            # 获取文件扩展名
            _, ext = os.path.splitext(old_name)
            # 生成新文件名，使用两位数格式
            new_name = f"{i:02d}{ext.lower()}"
            # 构建完整的文件路径
            old_path = os.path.join(character_path, old_name)
            new_path = os.path.join(character_path, new_name)
            
            # 检查新文件名是否已存在
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{i:02d}_{counter}{ext.lower()}"
                new_path = os.path.join(character_path, new_name)
                counter += 1
            
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"  {old_name} -> {new_name}")
        
        print(f"  共处理了 {len(image_files)} 个文件\n")

if __name__ == "__main__":
    # img文件夹的路径
    img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
    
    # 检查img文件夹是否存在
    if not os.path.exists(img_folder):
        print(f"错误: 找不到img文件夹 '{img_folder}'")
        exit(1)
    
    print(f"开始处理图片文件...\n")
    rename_images_in_folder(img_folder)
    print("所有图片已成功重命名！")