import webvtt
from googletrans import Translator
import os


def load_and_save_vtt():
    sbv_path = os.path.join(
        '/Volumes/Lacie/Python/Self Learning/Youtube_Captions_Translator/Youtube_Captions_Translator', 'captions.sbv')
    vtt = webvtt.from_sbv(sbv_path)
    vtt.save()
    return vtt


def translate_captions(vtt, translator):
    translated = webvtt.WebVTT()
    for caption in vtt:
        translation = translator.translate(caption.text, src='es', dest='en')
        result = webvtt.Caption(caption.start, caption.end, translation.text)
        translated.captions.append(result)
    return translated


def main():
    translator = Translator()

    vtt = load_and_save_vtt()

    translated = translate_captions(vtt, translator)

    translated.save('captions_translated')


if __name__ == "__main__":
    main()
