#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
个人简历网站本地开发服务器
简化版本，适用于 Windows/Mac 系统

使用方法:
    python server.py

作者: 沧海
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import socket
from datetime import datetime

# Windows系统编码处理
if sys.platform.startswith('win'):
    import io
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

def find_free_port(start_port=8000, max_attempts=10):
    """查找可用端口"""
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    return None

def check_index_file():
    """检查index.html文件是否存在"""
    if not os.path.exists('index.html'):
        print("错误: 未找到 index.html 文件")
        print("请确保您在包含网站文件的正确目录中运行此脚本。")
        return False
    return True

def print_banner():
    """打印启动横幅"""
    print("\n" + "="*50)
    print("沧海的个人简历网站 - 本地开发服务器")
    print("="*50)

def print_server_info(host, port):
    """打印服务器信息"""
    print(f"\n服务器启动成功!")
    print(f"本地地址: http://{host}:{port}")
    print(f"网络地址: http://localhost:{port}")
    
    print(f"\n访问说明:")
    print(f"   * 在浏览器中打开上述地址")
    print(f"   * 修改文件后刷新浏览器即可看到效果")
    print(f"   * 按 Ctrl+C 停止服务器")
    print(f"\n服务状态:")
    print(f"   * 服务器时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   * 工作目录: {os.getcwd()}")
    print("\n" + "-"*50)

def main():
    """主函数"""
    print_banner()
    
    # 检查必要文件
    if not check_index_file():
        sys.exit(1)
    
    # 设置服务器参数
    HOST = '127.0.0.1'
    DEFAULT_PORT = 8000
    
    # 查找可用端口
    port = find_free_port(DEFAULT_PORT)
    if port is None:
        print(f"错误: 无法找到可用端口 (尝试了 {DEFAULT_PORT}-{DEFAULT_PORT+9})")
        sys.exit(1)
    
    try:
        # 创建简单的HTTP服务器
        handler = http.server.SimpleHTTPRequestHandler
        
        with socketserver.TCPServer((HOST, port), handler) as httpd:
            print_server_info(HOST, port)
            
            # 自动打开浏览器
            try:
                webbrowser.open(f'http://localhost:{port}')
                print("正在打开默认浏览器...")
            except Exception as e:
                print(f"无法自动打开浏览器，请手动打开: http://localhost:{port}")
            
            print(f"服务器运行中，等待连接...\n")
            
            # 启动服务器
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\n\n服务器已停止")
        print("感谢使用!")
    except Exception as e:
        print(f"\n服务器错误: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()