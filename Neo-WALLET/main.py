from ROUTER import Router

# port= 3306 #server port


if __name__ == '__main__':
    Router.app.run(debug=True, port= 8080)