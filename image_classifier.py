import os
import shutil

def classify_images_by_date(source_dir, target_dir):
    """
    将源目录中的图片按照日期分类并复制到目标目录。

    :param source_dir: 源目录路径
    :param target_dir: 目标目录路径
    """

    if not source_dir or not target_dir:
        print("错误：必须提供源目录和目标目录。")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"目标目录 {target_dir} 已创建。")

    # 遍历源目录中的每个子目录
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)
        if os.path.isdir(subdir_path):
            # 遍历子目录中的每个文件
            for filename in os.listdir(subdir_path):
                if filename.endswith('.png'):
                    # Extract the date from the filename
                    date_str = filename.split(' ')[0]

                    # Create a new directory with the date as the name
                    date_dir = os.path.join(target_dir, date_str)
                    if not os.path.exists(date_dir):
                        os.makedirs(date_dir)
                        print(f"日期目录 {date_dir} 已创建。")

                    # Define source and target file paths
                    source_file = os.path.join(subdir_path, filename)
                    target_file = os.path.join(date_dir, filename)

                    # Check if the target file already exists
                    if not os.path.exists(target_file):
                        shutil.copy2(source_file, target_file)
                        # print(f"文件 {source_file} 已复制到 {target_file}。")
                    # else:
                    # print(f"文件 {target_file} 已存在，跳过复制。")

if __name__ == "__main__":
    source_directory = ''
    target_directory = ''
    if not source_directory or not target_directory:
        print("错误：必须提供源目录和目标目录。")
    else:
        print("开始分类图片...")
        classify_images_by_date(source_directory, target_directory)
        print("图片分类完成。")
