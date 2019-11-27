# 获取系统显示尺寸
def get_system_metrics():
    from win32api import GetSystemMetrics
    return GetSystemMetrics(0),GetSystemMetrics(1)

# 计算窗口居中的位置
def get_window_position(width, height):
    system_metrics = get_system_metrics()
    window_x_position = (system_metrics[0] - width) // 2
    window_y_position = (system_metrics[1] - height) // 2
    return window_x_position, window_y_position
