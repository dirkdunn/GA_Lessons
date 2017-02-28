# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
CREDENTIALS:
{
  "url": "https://gateway.watsonplatform.net/language-translator/api",
  "username": "b110f05b-0520-43a3-87a9-fc521c8335f2",
  "password": "CdEimCbBo6iE"
}
"""

import os
from flask import Flask, jsonify, request
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

app = Flask(__name__)

language_translator = LanguageTranslator(
    username='b110f05b-0520-43a3-87a9-fc521c8335f2',
    password='CdEimCbBo6iE')

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/api/translate', methods=['POST'])
# write code to return translation of incoming JSON data
def slackApi():
    sentenceToTranslate = request.form['text']
    translationCommand = request.form['command']

    # .strip() .split('') ''.join(list) .pop(0)
    # sentenceToTranslate = 'french hey whats up'

    newSentence = ' '.join(sentenceToTranslate.strip().split()[1:])
    languageToTranslateTo = ''.join(sentenceToTranslate.strip().split()[0:1]).title()
    myLanguage = language_translator.identify(newSentence)["languages"][0]["language"]
    targetLanguage = None

    for l in language_translator.get_identifiable_languages()["languages"]:
        # l == { name: "French", language: 'fr'}
        if languageToTranslateTo == l["name"]:
            targetLanguage = l["language"]

    translation = language_translator.translate(
                    text=newSentence,
                    source=myLanguage,
                    target=targetLanguage)

    # request.form['text'] = 'french hello'
    # request.form['command'] = '/translate'

    return translation

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
