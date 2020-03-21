#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
from datetime import datetime
import pickle
app = Flask(__name__)
@app.route('/croute/<int:i1>')
def croute(i1):
    doy = datetime.today().timetuple().tm_yday



    # "day of year" ranges for the northern hemisphere

    #winter = range(, 59)

    summer = range(60, 152)

    fall = range(153, 305)

    # winter = everything else

    if doy in summer:

        season = 1

    elif doy in fall:

        season = 0

    else:

        season = 2
    hour = datetime.now().hour
    if 5 <= hour <= 11:
        hour=2
    elif 12 <= hour <= 17:
        hour=0
    else:
        hour=1
    model=pickle.load(open('coffee.pkl','rb'))
    out=model.predict([[i1,hour,season]])
    return str(out[0])
    
if __name__ =='__main__':
    app.run(debug=True)

