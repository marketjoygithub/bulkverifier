import pandas as pd
import numpy as np
from flask import Flask, request, render_template,make_response
from bulk_verifier import verifier

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'),encoding='ISO-8859-1',)
        df = pd.DataFrame(df)

        df['status'] = df['Email'].apply(verifier)
        
        resp = make_response(df.to_csv(index=False))
        resp.headers["Content-Disposition"] = "attachment; filename=Verified_list.csv"
        resp.headers["Content-Type"] = "text/csv"

        return resp
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=3133)