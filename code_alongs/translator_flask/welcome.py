import os
from flask import Flask, jsonify, request
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

app = Flask(__name__)
language_translator = LanguageTranslator(
    username="512d9ca5-ba8a-4b69-ad39-c4ee49d53d25",
    password="clPlhUcs6rlY")

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/api/translate', methods=['POST'])
def translate():
    # Parse language to translate to, and the sentece (activity)
    sentenceToTranslate = ' '.join(request.form['text'].strip().split(' ')[1:])
    languageParam = request.form['text'].strip().split(' ')[0].title()

    try:
        language = language_translator.identify(request.form['text'])['languages'][0]['language']
        languages = language_translator.get_identifiable_languages()['languages']
        languageTarget = 'en'

        for l in languages:
            if languageParam == l['name']:
                languageTarget = l['language']

        translation = language_translator.translate(
                        text=sentenceToTranslate,
                        source=language,
                        target=languageTarget)

        return jsonify(response_type="in_channel",text=translation)

    except Exception as ex:
        message = """
        An exception of type %s occured.
        Arguments:\n%s sentenceToTranslate: %s languageParam: %s""" % (type(ex).__name__, ex.args, sentenceToTranslate, languageParam)

        return """The language you have entered is not valid. make sure your command looks likes this:
                /translate language hello!
                Error: %s""" % (message)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
