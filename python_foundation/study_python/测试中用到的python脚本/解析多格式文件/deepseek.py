#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/3/4
# @Description: [对文件功能等的简要描述（可自行添加）]

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import yaml
import openpyxl
import markdown
from docx import Document
import requests
import re
import os


class APITestTool:
    def __init__(self, master):
        self.master = master
        master.title("智能接口测试工具")
        master.geometry("1200x800")

        # 初始化变量
        self.api_data = []
        self.current_content = ""
        self.setup_ui()

    def setup_ui(self):
        # 创建主布局
        main_paned = tk.PanedWindow(self.master, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=1)

        # 左侧控制面板
        left_panel = ttk.Frame(main_paned, width=300)
        self.setup_left_panel(left_panel)
        main_paned.add(left_panel)

        # 中间预览面板
        center_panel = ttk.Frame(main_paned)
        self.setup_center_panel(center_panel)
        main_paned.add(center_panel)

        # 右侧生成面板
        right_panel = ttk.Frame(main_paned, width=300)
        self.setup_right_panel(right_panel)
        main_paned.add(right_panel)

    def setup_left_panel(self, panel):
        # 文件导入区域
        ttk.Label(panel, text="文件导入").pack(pady=5)
        ttk.Button(panel, text="选择文件", command=self.load_file).pack(fill=tk.X)
        ttk.Button(panel, text="拖拽文件至此", command=self.load_file).pack(fill=tk.X, pady=5)

        # 文件类型选择
        self.file_type = tk.StringVar()
        ttk.Radiobutton(panel, text="HAR", variable=self.file_type, value="har").pack(anchor=tk.W)
        ttk.Radiobutton(panel, text="Swagger", variable=self.file_type, value="swagger").pack(anchor=tk.W)
        ttk.Radiobutton(panel, text="Excel", variable=self.file_type, value="excel").pack(anchor=tk.W)

    def setup_center_panel(self, panel):
        # 文档预览区域
        self.preview_text = scrolledtext.ScrolledText(panel, wrap=tk.WORD)
        self.preview_text.pack(fill=tk.BOTH, expand=True)

        # 解析结果展示
        self.tree = ttk.Treeview(panel, columns=('Method', 'Endpoint'), show='headings')
        self.tree.heading('Method', text='方法')
        self.tree.heading('Endpoint', text='端点')
        self.tree.pack(fill=tk.BOTH, expand=True)

    def setup_right_panel(self, panel):
        # 生成配置
        ttk.Label(panel, text="生成配置").pack(pady=5)
        self.prompt = scrolledtext.ScrolledText(panel, height=5)
        self.prompt.pack(fill=tk.X)

        ttk.Button(panel, text="生成测试用例", command=self.generate_cases).pack(fill=tk.X, pady=5)

        # 导出选项
        ttk.Label(panel, text="导出格式").pack()
        self.export_format = tk.StringVar(value='json')
        formats = [('JSON', 'json'), ('YAML', 'yaml'),
                   ('Excel', 'excel'), ('Markdown', 'md'), ('Word', 'docx')]
        for text, val in formats:
            ttk.Radiobutton(panel, text=text, variable=self.export_format, value=val).pack(anchor=tk.W)

        ttk.Button(panel, text="导出结果", command=self.export_results).pack(fill=tk.X, pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path: return

        try:
            if file_path.endswith(('.har', '.json')):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                self.process_har(data)
            elif file_path.endswith(('.yaml', '.yml')):
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                self.process_swagger(data)
            elif file_path.endswith(('.xlsx', '.xls')):
                self.process_excel(file_path)
            # 其他格式处理...

            self.show_preview(file_path)
            self.extract_endpoints()
        except Exception as e:
            messagebox.showerror("错误", f"文件解析失败: {str(e)}")

    def process_har(self, data):
        self.api_data = []
        for entry in data['log']['entries']:
            request = entry['request']
            self.api_data.append({
                'method': request['method'],
                'url': request['url'],
                'headers': request['headers'],
                'params': request.get('queryString', []),
                'body': request.get('postData', {})
            })

    def process_swagger(self, data):
        self.api_data = []
        for path, methods in data['paths'].items():
            for method, details in methods.items():
                self.api_data.append({
                    'method': method.upper(),
                    'url': data['host'] + path,
                    'parameters': details.get('parameters', []),
                    'responses': details.get('responses', {})
                })

    def process_excel(self, file_path):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        self.api_data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            self.api_data.append({
                'method': row[0],
                'url': row[1],
                'params': row[2] if len(row) > 2 else None
            })

    def extract_endpoints(self):
        self.tree.delete(*self.tree.get_children())
        for api in self.api_data:
            self.tree.insert('', 'end', values=(api['method'], api['url']))

    def generate_cases(self):
        prompt_text = self.prompt.get("1.0", tk.END)
        if not prompt_text.strip():
            messagebox.showwarning("提示", "请输入生成提示词")
            return

        # 调用DeepSeek API（示例）
        try:
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={"Authorization": "Bearer YOUR_API_KEY"},
                json={
                    "model": "deepseek-chat",
                    "messages": [{
                        "role": "user",
                        "content": f"根据以下API信息生成测试用例：\n{self.api_data}\n用户需求：{prompt_text}"
                    }]
                }
            )
            result = response.json()['choices'][0]['message']['content']
            self.show_generated_content(result)
        except Exception as e:
            messagebox.showerror("错误", f"生成失败: {str(e)}")

    def export_results(self):
        file_types = {
            'json': ('JSON 文件', '.json'),
            'yaml': ('YAML 文件', '.yaml'),
            'excel': ('Excel 文件', '.xlsx'),
            'md': ('Markdown 文件', '.md'),
            'docx': ('Word 文档', '.docx')
        }

        path = filedialog.asksaveasfilename(
            filetypes=[file_types[self.export_format.get()]],
            defaultextension=file_types[self.export_format.get()][1]
        )

        if path:
            try:
                if self.export_format.get() == 'json':
                    with open(path, 'w') as f:
                        json.dump(self.api_data, f)
                elif self.export_format.get() == 'yaml':
                    with open(path, 'w') as f:
                        yaml.safe_dump(self.api_data, f)
                # 其他格式导出...
                messagebox.showinfo("成功", "导出完成！")
            except Exception as e:
                messagebox.showerror("错误", f"导出失败: {str(e)}")

    def show_preview(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read(1000)  # 限制预览长度
            self.preview_text.delete(1.0, tk.END)
            self.preview_text.insert(tk.END, content)

    def show_generated_content(self, content):
        top = tk.Toplevel(self.master)
        text = scrolledtext.ScrolledText(top)
        text.insert(tk.END, content)
        text.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = APITestTool(root)
    root.mainloop()