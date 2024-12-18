from flask import Flask, render_template, send_file

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Plant Disease Detection</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            p {
                line-height: 1.6;
                color: #666;
            }
            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                color: white;
                background-color: #007bff;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            .btn:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Plant Disease Detection Project</h1>
            <p>
                This project aims to detect plant diseases using a deep learning model. 
                The model leverages the PlantVillage dataset and achieves an accuracy of 93%.
            </p>
            <a href="/model" class="btn">View Model</a>
        </div>
    </body>
    </html>
    '''

# Route for the model page
@app.route('/model')
def model():
    # Serve the pre-generated HTML file
    return send_file('plant_disease_detection_complete.html')

if __name__ == '__main__':
    app.run(debug=True)
