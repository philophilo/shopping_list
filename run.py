from app import app


#Run the application
if __name__ == "__main__":
    app.secret_key = "ofkoefnononjnibjmcmdndvndsnvd"
    app.config['SESSION_TYPE'] = "filesystem"
    app.run(port=8080, debug=True)
