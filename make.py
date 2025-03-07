
import argparse
import os
# sphinx should be installed
import subprocess
from sphinx.cmd.build import main as sphinx_main


_CUR_ = os.path.abspath(os.path.join(__file__, "../"))

from pathlib import Path

def plot_file_to_run(root):
    lp = []
    for file in root.rglob("*.py"):
        if(file.parent.name == "fig"):
            lp.append(file)
    return lp

def run_plot_file(lpy):
    for path in lpy:
        result = subprocess.run(["python3", str(path)], capture_output=True, text=True)
        if(result.returncode != 0):
            print("std cout", result.stdout)
            print("std err", result.stderr)
        
# run_plot_file(plot_file_to_run(Path(_CUR_ + "/source")))

def pre_build(path):
    fplot = plot_file_to_run(Path(path + "/source"))
    print("Plot py ", len(fplot), "files")
    run_plot_file(fplot)


# 运行另一个 Python 文件
# result = subprocess.run(["python", "another_script.py"], capture_output=True, text=True)

# 输出结果
# print("标准输出:", result.stdout)
# print("标准错误:", result.stderr)
# print("返回码:", result.returncode)

def build_doc(path):
        # 
    doc_source_dir = os.path.abspath(os.path.join(path, "source"))
    doc_build_dir  = os.path.abspath(os.path.join(path, "build"))

    # command
    build_format  = 'html'  # singlehtml
    args = ["-b", str(build_format), str(doc_source_dir), str(doc_build_dir)]
    sphinx_main(args)


if __name__ == '__main__':
    pre_build(_CUR_)
    build_doc(_CUR_)