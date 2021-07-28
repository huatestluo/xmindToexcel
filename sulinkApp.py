import tkinter
import re
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

from xmind_to_xls import XmindToXsl


class MainUI(object):

    def __init__(self, title="sulink", geometrysize="350x250", geometry="+800+350"):
        self.top = tkinter.Tk()  # 生成主窗口
        self.top.title(title)  # 设置窗口的标题
        self.top.geometry(geometrysize)  # 设置窗口的大小
        self.top.geometry(geometry)  # 设置窗口出现的位置
        self.top.resizable(0, 0)  # 将窗口大小设置为不可变
        self.path = tkinter.StringVar()  # 生成一个StringVar 对象，来保存下面输入框中的内容
        self.person = tkinter.StringVar()
        self.version = tkinter.StringVar()

        # 调用自己写的create_widgets()方法
        self.create_widgets()

    def get_value(self):
        """获取文本框中数据，并调用XmindToXsl类"""

        path = self.path.get()
        per = self.person.get()
        ver = self.version.get()
        # print(f"地址：{path}，测试人员：{per}，测试版本：{ver}")
        regvalue = '.*\.xmind$'
        xmind_reg = re.match(regvalue, path)
        if xmind_reg:
            # xmind转换成xls
            xmind_to_xls = XmindToXsl(path)
            xmind_to_xls.write_excel(performer=per, editionname=ver)
            messagebox.showinfo(title='提示', message='任务执行成功，请查看生成的用例！')
        else:
            messagebox.showinfo(title='提示', message='请选择正确的xmind文件，谢谢！')

    def select_path(self):
        """选择要转换成excel的xmind地址"""

        path_ = askopenfilename()
        self.path.set(path_)

    def create_widgets(self):
        """创建窗口中的各种元素"""

        # 文件的路径
        first_label = tkinter.Label(self.top, text='目标路径：')  # 生成一个标签
        first_label.grid(row=0, column=0)  # 使用grid布局，标签显示在第一行，第一列

        first_entry = tkinter.Entry(self.top, textvariable=self.path)  # 生成一个文本框，内容保存在上面变量中
        first_entry.grid(row=0, column=1)  # 使用grid布局，文本框显示在第一行，第二列
        way_button = tkinter.Button(self.top, text="路径选择", command=self.select_path)
        way_button.grid(row=0, column=2)  # 使用grid布局，按钮显示在第一行，第三列

        # 测试人员
        second_label = tkinter.Label(self.top, text="创建人：")
        second_label.grid(row=1, column=0)
        second_entry = tkinter.Entry(self.top, textvariable=self.person)
        second_entry.grid(row=1, column=1)

        # 版本
        third_label = tkinter.Label(self.top, text="需求ID：")
        third_label.grid(row=2, column=0)
        third_entry = tkinter.Entry(self.top, textvariable=self.version)
        third_entry.grid(row=2, column=1)

        # 提交按钮
        f_btn = tkinter.Frame(self.top, bg='red')  # 设置一个frame框架，并设置背景颜色为红色
        f_btn.place(x=0, y=160, width=350, height=45)  # 设置框架的大小，及在top窗口显示位置
        submit_button = tkinter.Button(f_btn, text="提交", command=self.get_value, width=49, height=2,
                                       bg="#00FFFF")  # 设置按钮的文字，调用方法，大小，颜色，显示框架
        submit_button.grid(row=0, column=2)  # 使用grid布局，按钮显示在第一行，第一列

        # 退出按钮
        t_btn = tkinter.Frame(self.top,bg='red')
        t_btn.place(x=0, y=205, width=350, height=45)
        sub_button = tkinter.Button(t_btn, text='退出',command=t_btn.quit,width=49, height=2,
                                       bg="red")
        sub_button.grid(row=0, column=2)
        # 进入消息循环（必需组件）
        self.top.mainloop()


if __name__ == "__main__":
    mu = MainUI(title="sulinkAPP")