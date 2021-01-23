from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET']) # This is the root route
def root():
    if request.method == "POST":

        location = request.form.get("Location")
        maxtemp = int(request.form.get("tempmax"))
        mintemp = int(request.form.get("tempmin"))
        winspeed = int(request.form.get("windspeed"))
        relspeed = int(request.form.get("relativespeed"))
        relhum = int(request.form.get("relativehum"))

        if ( winspeed == -1 and  relspeed == -1 and relhum == -1):
            return render_template("contact2.html",
            loc=f"Location: {location}",
            maxtemp=f"Max Temp: {maxtemp}",
            mintemp=f"Min Temp: {mintemp}")

        elif ( relspeed == -1 and relhum == -1):
            return render_template("contact2.html",
            loc=f"Location: {location}",
            maxtemp= f"Max Temp: {maxtemp}",
            mintemp=f"Min Temp: {mintemp}",
            winspeed = f"Windspeed: {winspeed}")

        elif (winspeed == -1 and relspeed == -1):
            return render_template("contact2.html",
            loc=f"Location: {location}",
            maxtemp= f"Max Temp: {maxtemp}",
            mintemp=f"Min Temp: {mintemp}",
            winspeed=f"Relativehumidity: {relhum}")

        elif (winspeed == -1 and relhum == -1 ):
            return render_template("contact2.html",
            loc=f"Location: {location}",
            maxtemp= f"Max Temp: {maxtemp}",
            mintemp=f"Min Temp: {mintemp}",
            winspeed = f"Relativespeed: {relspeed}")

        elif (relspeed == -1):
            return render_template("contact2.html",
            loc=f"Location: {location}",
            maxtemp= f"Max Temp: {maxtemp}",
            mintemp=f"Min Temp: {mintemp}",
            winspeed = f"Windspeed: {winspeed}",
            relspeed=  f"Relativehumidity: {relhum}")

        elif (winspeed == -1):
            return render_template("contact2.html",
            loc=f"Location: {location}",
            maxtemp= f"Max Temp: {maxtemp}",
            mintemp=f"Min Temp: {mintemp}",
            winspeed = f"Relativespeed: {relspeed}",
            relspeed=  f"Relativehumidity: {relhum}")

        elif (relhum == -1):
            return render_template("contact2.html",
            loc=f"Location: {location}",
            maxtemp= f"Max Temp: {maxtemp}",
            mintemp=f"Min Temp: {mintemp}",
            winspeed = f"Windspeed: {winspeed}",
            relspeed = f"Relativespeed: {relspeed}")

    return render_template('contact.html') # render_template sends the HTML file to the browser

if __name__=="__main__":
	app.run(debug=False, host='0.0.0.0)