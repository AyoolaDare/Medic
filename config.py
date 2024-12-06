class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_REGION = os.environ.get('AWS_REGION')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    USERS_TABLE_NAME = os.environ.get('USERS_TABLE_NAME')
    PATIENTS_TABLE_NAME = os.environ.get('PATIENTS_TABLE_NAME')
    ACTIVITIES_TABLE_NAME = os.environ.get('ACTIVITIES_TABLE_NAME')

