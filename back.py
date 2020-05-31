#Import personality Insights SDK
from watson_developer_cloud import PersonalityInsightsV3
#import json
import json
#import googletrans
#from googletrans import Translator
#import pandas
import pandas as pd
#import webrowser
import webbrowser

url='https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/c6aa4e32-e9be-4d4e-8ce3-8b8abf5aa155'
apikey='-P2pUTGEF30hXdiS4iUQH05400USV7imPKkZa9aN82Zq'
print('Iniciando...')
service = PersonalityInsightsV3(url=url, iam_apikey=apikey, version='2020-05-31')

def start(text):
	profile = service.profile(text, content_type = 'text/plain').get_result()
	x = convierte_df(action_back('personality',profile))
	y = convierte_df(action_back('needs',profile))
	z = convierte_df(action_back('values',profile))
	crea_html(x,y,z)
	return 0

def convierte_df(df_marks):
  html = df_marks.to_html()
  if html is None:
    html = DEFAULT_VALUE
  return html

def crea_html(p,n,v):
	f = open('gener.html','wb')
	mensaje = """<html><head></head><body><div><h1>Personalidad</h1>"""+str(p)+"""</div><div><h1>Necesidades</h1>"""+str(n)+"""</div><div><h1>Valores</h1>"""+str(v)+"""</div><!--Div that will hold the pie chart--><!--div id="chart_div"></div--></body></html>"""
	s = mensaje.encode()
	f.write(s)
	f.close()
	webbrowser.open_new_tab('gener.html')
	return 0
	
def action_back(name_insight, profile):
	insight = {p['name']:p['percentile'] for p in profile[name_insight]}
	df_insight = pd.DataFrame.from_dict(insight, orient='index')
	df_insight.reset_index(inplace=True)
	df_insight.columns=[name_insight,'percentile']
	return df_insight

def test():
	text = """holy fuck... same here, in my country it was the most crucial from mid march to 
	beginning of this month and tbh for these month and a half i havent felt so at peace in a 
	VERY long time, no stress on future or finding for jobs since everything was basically frozen 
	in time, there weren't people outside and i LOVED riding around my small town on a bike, just 
	enjoying solitude for hours, so calm and peaceful idk how else to describe it an, it was so good 
	without being nervous about future and not doing anything with my life since everyone is doing the 
	same

when i heard that they are going to ease up on this quarantine thing i felt sick the entire day i swear, 
was so sad and defeated because they said in early april that maybe in july things will go to better, 
then out of the blue poof, 1st of may people swarmed the town like flies, barber shops, coffee shops, 
all these people being social, just enjoying depression free lifestyle and i'm constantly reminded how 
anti social i am

i was always this nostalgic and sentimental person and i already miss what happened a month ago, i can 
no longer buy couple of beers and sit on my own in a park and drink it while listening to some g-funk 
and just chill there, i mean i can do it now too, but i hate everytiem i try and talk and maybe meet new 
people i always end up failing because im a 25 year old with a mentality of 18, plus im poor, no car or 
rivings license, no friends and even if i manage to talk to some cutie she will soon realize how pathetic i am"""
	start(text)
test()