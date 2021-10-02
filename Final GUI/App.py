from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivy.garden.matplotlib import FigureCanvasKivyAgg



Window.size = (1000, 600)


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('App.kv')
		#return water_temp()
	
	#def water_temp(self):
		#temp=[14.1 ,14.6 ,16.4 ,18.9 ,22 ,24.9,26.8,27.3,26,23.2,19.7,16]
		#month = ['January' , 'February' , 'March' , 'April' , 'May' , 'June', 'July' , 'August' , 'Septemper' , 'October' , 'November' , 'December']
		#plt.plot(month,temp)
		#plt.title('Water Temperature Average Through Year')
		#plt.ylabel('Temperature')
		#plt.xlabel('Month')
		#return self.add_widget(FigureCanvasKivyAgg(plt.gcf()))
	

	

#class speedmeter ()
	
	
MainApp().run()