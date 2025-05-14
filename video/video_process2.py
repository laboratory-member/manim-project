import cv2
import numpy as np

# 设置路径
background_path = "Example.mp4"
overlay_paths = ["Show.mp4"]  # 多个叠加视频路径
output_path = "output2.avi"

# 设置叠加视频的参数
insert_times = [33]  # 每个叠加视频的开始时间（秒）
overlay_height_ratios = [0.7]  # 每个叠加视频占背景高度的比例

# 打开背景视频
bg_cap = cv2.VideoCapture(background_path)
fps = int(bg_cap.get(cv2.CAP_PROP_FPS))
width = int(bg_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(bg_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(bg_cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 创建输出视频写入器
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

if not out.isOpened():
    print("❌ 视频写入器初始化失败！")
    exit()

# 初始化叠加视频
overlay_caps = [cv2.VideoCapture(path) for path in overlay_paths]
overlay_total_frames = [int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) for cap in overlay_caps]

frame_idx = 0
progress_interval = max(total_frames // 100, 1)  # 每写入1%打印一次

while True:
    ret_bg, bg_frame = bg_cap.read()
    if not ret_bg:
        break

    blended_frame = bg_frame.copy()

    for idx, (insert_time, overlay_ratio) in enumerate(zip(insert_times, overlay_height_ratios)):
        ov_cap = overlay_caps[idx]
        insert_frame = int(insert_time * fps)

        if insert_frame <= frame_idx < insert_frame + overlay_total_frames[idx]:
            ret_ov, ov_frame = ov_cap.read()
            if ret_ov:
                overlay_height = int(height * overlay_ratio)
                ov_crop = ov_frame[-overlay_height:, :, :]
                blended_frame[-overlay_height:, :, :] = ov_crop

    out.write(blended_frame)
    frame_idx += 1

    # 显示进度
    if frame_idx % progress_interval == 0 or frame_idx == total_frames:
        percent = int(100 * frame_idx / total_frames)
        print(f"\r▶️  进度：{percent:3d}%", end="")

# 清理资源
bg_cap.release()
for cap in overlay_caps:
    cap.release()
out.release()
cv2.destroyAllWindows()

print("\n✅ 合成完成，输出文件为：", output_path)
