import argparse
import os
import sys
import webbrowser
# sphinx should be installed
import subprocess
from sphinx.cmd.build import main as sphinx_main


_CUR_ = os.path.abspath(os.path.join(__file__, "../"))

from pathlib import Path

def plot_file_to_run(root):
    lp = []
    for file in root.rglob("*.py"):
        if(file.parent.name == "fig_script"):
            lp.append(file)
    return lp

def run_plot_file(lpy):
    for path in lpy:
        cwd = os.getcwd()
        os.chdir(path.parent)
        print(path.parent)
        result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
        if(result.returncode != 0):
            print("std cout", result.stdout)
            print("std err", result.stderr)
        os.chdir(cwd)
        
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


def open_html_home(path):
    html_home = Path(path) / "build" / "index.html"
    if not html_home.is_file():
        print(
            "Error: build/index.html was not found. Run `python make.py` to build the documentation first.",
            file=sys.stderr,
        )
        return 1

    webbrowser.open(html_home.resolve().as_uri())
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build and open the CFD-note documentation.")
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open build/index.html without rebuilding.",
    )
    args = parser.parse_args()

    if args.open:
        sys.exit(open_html_home(_CUR_))

    pre_build(_CUR_)
    build_doc(_CUR_)
