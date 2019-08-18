from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Line

app = Flask(__name__, static_folder="templates")

# 每日市值记录
asset_yaxis = [5705.25, 5685.46, 5915.64, 6215.64, 6415.64, 6515.64]

# 日线级别
date_xaxis = ["2017/8/{}".format(i + 2) for i in range(31)]


# date_xaxis.extend(["2017/8/{}".format(i + 1) for i in range(15)])

def line_base() -> Line:
    c = (
        Line()
            .add_xaxis(date_xaxis)
            .add_yaxis("资金曲线",
                       asset_yaxis,
                       is_connect_nones=True,
                       is_symbol_show=False
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title="USDT"))
                             # datazoom_opts=[opts.DataZoomOpts()])
    )
    return c


@app.route("/asset_curve")
def index():
    c = line_base()
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run()
