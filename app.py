from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
app = Flask(__name__)
person = {
    'name': '张冰心',
    'major':'计算机专业',
    'address' : '亚洲某个国家',
    'summary':'对待工作认真负责，善于沟通、协调有较强的组织能力与团队精神;活泼开朗、乐观上进、有爱心并善于施教并行;上进心强、勤于学习能不断提高自身的能力与综合素质',
    'tel': '15965847563',
    'email': '1235845684@.com',
    'school':'哈佛大学',
    'edtime':'2018-2022',
    'birthday':'2021.1.1',
    'sex':'男',
    'hobby':'业余爱好',
    'data':'本人拥有广泛的兴趣爱好，阅读、思考、运动、社交等为主要爱好，良好的生活与学习习惯！',
    'git':'https://github.com',

    'ename1':'python爬虫与可视化',
    'dlanguage1':'Python',
    'time1':'2020-2021',
    'tool1':'Pycharm',
    'details1' : '爬取短文网的数据，对数据清洗后用柱状图，饼图和词云的形式进行可视化',

    'ename2': 'web商城',
    'dlanguage2': 'Java,JavaScript',
    'time2': '2020-2021',
    'tool2': 'NetBeans IDE 8.2',
    'details2': '能实现商城的基本功能，显示商品基本信息，用户可以选择商品并加入购物车',
    'hobby':'本人拥有广泛的兴趣爱好，阅读、思考、运动、社交等为主要爱好，良好的生活与学习习惯！',
}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)
@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return (gm(request.args.get('data')))

@app.route('/callback1', methods=['POST', 'GET'])
def cb1():
	return (gm1(request.args.get('data')))

@app.route('/callback2', methods=['POST', 'GET'])
def cb2():
	return (gm2(request.args.get('data')))

@app.route('/callback3', methods=['POST', 'GET'])
def cb3():
	return (gm3(request.args.get('data')))

@app.route('/callback4', methods=['POST', 'GET'])
def cb4():
	return (gm4(request.args.get('data')))


@app.route('/chart')
def index():
	return render_template('chartsajax.html', graphJSON=gm1(),graphJSON5=gm5())

def gm(data='everyday'):
    df = pd.read_csv('./static/img/data.csv')
    fig = px.line(df[df['date'] ==data], x="hour", y="count")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm1(data='everyday'):
    df = pd.read_csv('./static/img/data.csv')
    fig = px.bar(df[df['date'] ==data], x="hour", y="temp")
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

def gm2(data='everyday'):
    df = pd.read_csv('./static/img/data.csv')
    fig = px.bar(df[df['date'] ==data], x="hour", y="atemp")
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

def gm3(data='everyday'):
    df = pd.read_csv('./static/img/data.csv')
    fig = px.bar(df[df['date'] ==data], x="hour", y="humidity")
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

def gm4(data='everyday'):
    df = pd.read_csv('./static/img/data.csv')
    fig = px.bar(df[df['date'] ==data], x="hour", y="windspeed")
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1
def gm5():
    df = pd.read_csv('./static/img/data.csv')
    fig5 =px.scatter(df, x="datetime", y="count",color="season")
    graphJSON5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5

@app.route('/chartdl')
def index1():
    return render_template('chartdl.html', graphJSON=dl(), graphJSON1=dl1(),graphJSON3=dl3())
def dl():
    df = pd.DataFrame(px.data.gapminder())
    fig = px.choropleth(df, locations="iso_alpha", color="lifeExp",
                        hover_name="country", animation_frame="year",
                        range_color=[20, 80], projection="natural earth")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def dl1():
    df = pd.DataFrame(px.data.gapminder())
    fig = px.scatter(df  # 绘图使用的数据
           ,x="gdpPercap" # 横纵坐标使用的数据
           ,y="lifeExp"
           ,color="continent"  # 区分颜色的属性
           ,size="pop"   # 区分圆的大小
           ,size_max=60  # 圆的最大值
           ,hover_name="country"  # 图中可视化最上面的名字
           ,animation_frame="year"  # 横轴滚动栏的属性year
           ,animation_group="country"
           ,facet_col="continent"   # 按照国家country属性进行分格显示
           ,log_x=True
           ,range_x=[100,100000]
           ,range_y=[25,90]
           ,labels=dict(pop="Populations",  # 属性名字的变化，更直观
                       gdpPercap="GDP per Capital",
                       lifeExp="Life Expectancy"))
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1
def dl3():
    df = pd.DataFrame(px.data.gapminder())
    fig = px.area(df, x="year", y="pop", color="continent", line_group="country")
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3

@app.route('/charttip')
def index2():
    return render_template('charttip.html', graphJSON=tip(),graphJSON1=tip1(),graphJSON2=tip2())
def tip():
    df = pd.DataFrame(px.data.tips())
    fig = px.histogram(
        df,  # 绘图数据集
        x="sex",  # 横轴为性别
        y="tip",  # 纵轴为费用
        histfunc="avg",  # 直方图显示的函数
        color="smoker",  # 颜色
        barmode="group",  # 柱状图模式
        facet_row="time",  # 行取值
        facet_col="day",  # 列取值
        category_orders={  # 分类顺序
            "day": ["Thur", "Fri", "Sat", "Sun"],
            "time": ["Lunch", "Dinner"]}
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def tip1():
    df = pd.DataFrame(px.data.tips())
    fig1=px.box(df, x="day", y="total_bill", color="smoker")
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1
def tip2():
    df = pd.DataFrame(px.data.tips())
    fig2=px.scatter(df, x="total_bill", y="tip", facet_row="time", facet_col="day", color="smoker", trendline="ols",
                     category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2
if __name__ == '__main__':
    app.run(debug= True,port=5000,threaded=True)
