from controller import Controller

if __name__ == "__main__":
    # call instance of controller and fire run function in controller class
    app = Controller()
    # it's a running loop only breaks when user enter exit command or press ctrl+c
    app.run()