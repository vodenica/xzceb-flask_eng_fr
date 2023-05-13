"""Task1: Write a function that translates English text to French in translator.py"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/4c3d081d-0a91-4eaf-b798-61e9c2d87101')

def english_to_french(english_text):
    """
    This function returns text in french that was converted from english
    """
    french_text = language_translator.translate(english_text, model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    This function returns text in english that was converted from french
    """
    english_text = language_translator.translate(french_text, model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
