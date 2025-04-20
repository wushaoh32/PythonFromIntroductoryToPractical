#开源的数据可视化库
#官方文档https://gallery.pyecharts.org/#/README
#基本饼图，导入这个模块的东西
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

#准备数据
lst = [['华为',125],['小米',120],['OPPO',100],['苹果',100],['VIVO',80],['三星',100]]

c = (
    Pie()#绘制饼图
    .add("",lst)#这句话是一个二维列表，所以我需要准备数据
    .set_global_opts(title_opts=opts.TitleOpts(title="2028年手机出库占比情况"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
)

