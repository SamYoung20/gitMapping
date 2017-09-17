'''
Flask webapp for gif speak
'''

from flask import Flask
import os
from flask import render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def starting_page(top_story1=None):
    
    top_story1 = text_input(url1=None,url2=None,url3=None,url4=None,url5=None)
    return render_template('home.html', top_story1=top_story1)

@app.route('/about_us')
def about_team():
    return render_template('about_us.html')

@app.route('/about_project')
def about_project():
    return render_template('about_project.html')

@app.route('/the_app', methods=['GET','POST'])
def the_app(url=None):
    if request.method == 'POST':
        return redirect('home.html')
    return render_template('find_text_2_gif.html', url=url)

@app.route('/text_input', methods=['Get', 'POST'])
def text_input(url1=None,url2=None,url3=None,url4=None,url5=None):
    if request.method == 'POST':
        if request.form['GIF!'] and request.form['url']:
            #this is where the code would go to call sams function
            url_list = ['https://media2.giphy.com/media/9IRX12VhoXoR2/200.gif', 'https://media2.giphy.com/media/9IRX12VhoXoR2/200.gif', 'https://media2.giphy.com/media/9IRX12VhoXoR2/200.gif', 'https://media2.giphy.com/media/9IRX12VhoXoR2/200.gif', 'https://media2.giphy.com/media/9IRX12VhoXoR2/200.gif']
            url1 = url_list[0]
            url2 = url_list[1]
            url3 = url_list[2]
            url4 = url_list[3]
            url5 = url_list[4]

            #urls = 'https://media2.giphy.com/media/9IRX12VhoXoR2/200.gif'

            return render_template('gif_results.html', url1=url1,url2=url2, url3=url3,url4=url4,url5=url5)
        else:
            return render_template('find_text_2_gif.html')

    else:
        return render_template('home.html')
if __name__ == '__main__':
    app.run()
