<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_REGION = os.environ.get('AWS_REGION')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    USERS_TABLE_NAME = os.environ.get('USERS_TABLE_NAME')
    PATIENTS_TABLE_NAME = os.environ.get('PATIENTS_TABLE_NAME')
    ACTIVITIES_TABLE_NAME = os.environ.get('ACTIVITIES_TABLE_NAME')

||||||| 7b29ed2
=======
class Config:
    SECRET_KEY = '$2b$12$wOqgvdv6GLJ.mR7lf2/0JuJKi8wvwqhh62.H8ZRBfkIJ1OGcN2wcK'
    AWS_REGION = 'us-east-1'
    AWS_ACCESS_KEY_ID = 'AKIA6GBMGGNJYVWVLEOK'
    AWS_SECRET_ACCESS_KEY = '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'
    USERS_TABLE_NAME = 'clinic_users'
    PATIENTS_TABLE_NAME = 'clinic_patients'
    ACTIVITIES_TABLE_NAME = 'clinic_activities'
>>>>>>> f25679704435cd8aff50694d9122e3461a342d5c
