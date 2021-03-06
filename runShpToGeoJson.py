# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:52:39 2021
Shapefile转GeoJSON
@author: LW
"""
import geopandas as gpd

def shp2gj(input_file, output_file):
    data = gpd.read_file(input_file)
    
    ###进行重新组装
    
    data.to_file(output_file, driver="GeoJSON", encoding='UTF-8') # 指定utf-8编码，防止中文乱码
    print('Success: File '+input_file.split('\\') [-1] + ' conversion completed')

if __name__ == "__main__": 
    
    # 生成不同作物样本点的光谱或植被指数值
    inputs=r'F:\工作文件\博士研究\研究区域\山东\Shapefile\yantai.shp'
    outputs=r'H:\Temp\ResearchArea\Shandong\yantai.geojson'
    shp2gj(inputs,outputs)
    