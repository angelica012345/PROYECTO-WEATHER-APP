from flask import Flask, render_template, request
import requests


app= Flask(__name__)

def get_weather_data(city):
   APY_KEY ='e046257c07a0053d2e28ef4fb10d967f'
   url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={APY_KEY}'
   r = requests.get(url).json()
   return r

@app.route("/", methods=['POST', 'GET'])
def hello():
  if request.method == 'POST':
      ciudad=str(request.form.get('txtciudad'))
      data=get_weather_data(ciudad)
      return render_template('index.html', context = data)
  else: 
     return render_template('index.html')
 
@app.route("/CV")
def defaz():
    return render_template('CV.html')

if __name__ == "__main__":
   app.run(debug = True)


