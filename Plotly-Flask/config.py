# keep this file and other files used by the create_app function free of inner-project import statements to help
# prevent circular imports.  Setting up cache in a separate cache.py file similar to this config.py file is very helpful.

class Config:
    # user configurations
    #This configuration variable determines whether Flask runs in debug mode. Debug mode provides useful information 
    #for debugging and development but should be turned off in production environments for security reasons.
    flask_debug = False 
    dash_debug = False
  
    dash_auto_reload = False

    # flask configurations
    # It's used to cryptographically sign the session cookie
    SECRET_KEY = 'askjdfkajsdfksdf'
