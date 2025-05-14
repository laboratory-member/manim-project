import cv2

for i in range(5):
    # 构造文件名
    input_path = f"{i}.png"

    # 读取图像
    image = cv2.imread(input_path)

    if image is None:
        print(f"未找到图像 {input_path}，跳过。")
        continue

    # 图像反相
    inverted_image = 255 - image

    # 保存结果（覆盖原图或改名）
    cv2.imwrite(input_path, inverted_image)

    print(f"已保存反相图像为 {input_path}")
