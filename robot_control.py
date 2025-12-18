import time

def main():
    print("-------------------------")
    print("   JAKA 机械臂控制系统    ")
    print("-------------------------")
    print("[INFO] 系统初始化中...")
    time.sleep(1)
    print("[INFO] 连接成功！")
    
    # --- 新增加的代码 ---
    print("[ACTION] 正在移动到目标点...")
    time.sleep(1)
    print("[ACTION] 抓取物体成功！")
    # ------------------

if __name__ == "__main__":
    main()