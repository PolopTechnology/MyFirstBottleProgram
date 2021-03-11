from bottle import route, run, template

q = input("Hello or Hola")

if q == "Hello":
    @route("/<name>")
    def index(name):
        return template('<b>Hello {{name}}</b>', name=name)
elif q == "Hola":
      @route("/<name>")
      def index(name):
         return template('<b>Hola {{name}}</b>', name=name)


run(host='localhost', port=8080)
