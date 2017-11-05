from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import AverageDollarVolume
from quantopian.pipeline.factors import AnnualizedVolatility
from quantopian.pipeline.factors import SimpleMovingAverage
from quantopian.pipeline.factors import BollingerBands
import pandas as pd
import numpy as np

"""
Quiero el top %10 de acciones que han tocado mas veces las bollinger bands up and down en el año.
"""
 
def initialize(context):
    # Create and attach an empty Pipeline.
    pipe = make_pipeline()
    attach_pipeline(pipe, 'pipe')
    context.stock = pd.DataFrame(index=np.arange(500), columns=['name', 'Bollinger Up', 'Bollinger Down', 'Long_Order', 'Short_Order'])
    context.stock.fillna(value=0) 
    dollar_volume = AverageDollarVolume(window_length=30)
    high_dollar_volume = dollar_volume.percentile_between(97, 100)
    pipe.set_screen(high_dollar_volume)
    latest_close = USEquityPricing.close.latest
    pipe.add(latest_close, 'Close')
    BB = BollingerBands(window_length = 30, k=1)
    pipe.add(BB, 'Bollinger Bands')
    schedule_function(
    func=myfunc,
    date_rule=date_rules.every_day(),
    time_rule=time_rules.market_open(minutes=120),
  )
    
    
    
def make_pipeline(): 
    return Pipeline()

def before_trading_start(context, data):
    results = pipeline_output('pipe')
    #context.pipeline_results = results
    results.reset_index(level=0, inplace=True)
    context.stock['name'] = results['index']
    for i in range(len(results)):
        if results['Close'][i]>results['Bollinger Bands'][i][2]:
            context.stock.set_value(index=[i], col=['Bollinger Up'], value=context.stock['Bollinger Up'][i]+1)
            if context.stock['Bollinger Up'][i]+context.stock['Bollinger Down'][i] >= 4:
                context.stock.set_value(index=[i], col=['Long_Order'], 1)
        elif results['Close'][i]<results['Bollinger Bands'][i][0]:
            context.stock.set_value(index=[i], col=['Bollinger Down'], value=context.stock['Bollinger Down'][i]+1)
            if context.stock['Bollinger Up'][i]+context.stock['Bollinger Down'][i] >= 4:
                context.stock.set_value(index=[i], col=['Long_Order'], 1)

    context.tradeable = context.stock[(context.stock.Long_Order != 0) | (context.stock.Short_Order != 0)]
            """ cuando un touch llega a 5 agregarlo a la lista de tradeables"""
 
def my_func(context,data):
    for i in range(len(context.tradeable)):
        if context.tradeable['Long_Order'][i] = 1:
            order(context.tradeable['name'][i].sid, %1)
            context.stock.set_value(index=[i], col=['Long_Order'], 0)
        elif context.tradeable['Short_Order'][i] = 1:
            order(context.stock['name'][i].sid, %-1)
            context.stock.set_value(index=[i], col=['Short_Order'], 0)

def handle_data(context,data):
     pass
