from bottle import route, run, request, response
import os

@route('/login')
def hello_again():
        return '''
       <form>
       Category:      <input type="text" name="category" />
       Select a file: <input type="file" name="upload" />
       <input type="submit" value="Start upload" />
      </form>
      '''

@route('/image', method='POST')
def img():
    upload = request.files.get('upload')
    return "<img src=\"" + upload + "\" alt=\"Hello\">"

run(host='localhost', port=8080)

