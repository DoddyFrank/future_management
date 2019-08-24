from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Line

app = Flask(__name__, static_folder="templates")

# 每日市值记录
#base_yaxis = [6485.52, 6456.83, 6343.66, 6357.92, 6290.66, 6107.29, 5574.98]

asset_yaxis = [6485.52, 6456.83, 6343.66, 6357.92, 6290.66, 6107.29, 5574.98]

# 日线级别
date_xaxis = ["2017/8/{}".format(i + 1) for i in range(8, 31)]


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
