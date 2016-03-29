import argparse
import wave
import math
import re
import struct
import sys
import tempfile


morsetab = {
            'A': '.-',              'a': '.-',
            'B': '-...',            'b': '-...',
            'C': '-.-.',            'c': '-.-.',
            'D': '-..',             'd': '-..',
            'E': '.',               'e': '.',
            'F': '..-.',            'f': '..-.',
            'G': '--.',             'g': '--.',
            'H': '....',            'h': '....',
            'I': '..',              'i': '..',
            'J': '.---',            'j': '.---',
            'K': '-.-',             'k': '-.-',
            'L': '.-..',            'l': '.-..',
            'M': '--',              'm': '--',
            'N': '-.',              'n': '-.',
            'O': '---',             'o': '---',
            'P': '.--.',            'p': '.--.',
            'Q': '--.-',            'q': '--.-',
            'R': '.-.',             'r': '.-.',
            'S': '...',             's': '...',
            'T': '-',               't': '-',
            'U': '..-',             'u': '..-',
            'V': '...-',            'v': '...-',
            'W': '.--',             'w': '.--',
            'X': '-..-',            'x': '-..-',
            'Y': '-.--',            'y': '-.--',
            'Z': '--..',            'z': '--..',
            '0': '-----',           ',': '--..--',
            '1': '.----',           '.': '.-.-.-',
            '2': '..---',           '?': '..--..',
            '3': '...--',           ';': '-.-.-.',
            '4': '....-',           ':': '---...',
            '5': '.....',           "'": '.----.',
            '6': '-....',           '-': '-....-',
            '7': '--...',           '/': '-..-.',
            '8': '---..',           '(': '-.--.-',
            '9': '----.',           ')': '-.--.-',
            ' ': ' ',               '_': '..--.-',
    }

reverse_morsetab = {v:k for k,v in morsetab.items()}


def write_signal(wavef, duration, volume=0, rate=44100.0,
                 frequency=1240.0):
        """
        rate = 44100.0 # Sample rate in Hertz
        duration = 0.1       # seconds
        frequency = 1240.0    # hertz
        """
        for i in range(int(duration * rate * duration)):
                # max volume 32767.0
                value = int(volume*math.sin(frequency*math.pi*float(i)/float(rate)))
                data = struct.pack('<h', value)
                wavef.writeframesraw(data)


def text_to_morse(text, seperator=" / "):
        """translate a string to morse code in dot dash form"""
        morse = []
        for word in text.split():
                morse_word = []
                for w in word:
                        morse_word.append(morsetab[w])
                morse.append(' '.join(morse_word))

        return seperator.join(morse)


def morse_to_wav(text, file_=None):

    char2signal = {'.': 0.2, '-': 0.4, '/': 0.5, ' ': 0.2}

    if not file_:
        _, file_ = tempfile.mkstemp(".wav")

    wav = wave.open(file_, 'w')
    wav.setnchannels(1) # mono
    wav.setsampwidth(2)
    rate = 44100.0
    wav.setframerate(rate)

    for char in text:
        write_signal(wav, char2signal[char], volume=32767.0)
        write_signal(wav, 0.2, volume=0)

    wav.writeframes('')
    wav.close()

    return file_


def play(f, card='default'):
    try:
        import alsaaudio
    except ImportError:
        print("You need to install pyalsaaudio")

    device = alsaaudio.PCM(card=card)

    # Set attributes
    f = wave.open(f, 'rb')
    device.setchannels(f.getnchannels())
    device.setrate(f.getframerate())

    # 8bit is unsigned in wav files
    if f.getsampwidth() == 1:
        device.setformat(alsaaudio.PCM_FORMAT_U8)
    # Otherwise we assume signed data, little endian
    elif f.getsampwidth() == 2:
        device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    elif f.getsampwidth() == 3:
        device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
    elif f.getsampwidth() == 4:
        device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
    else:
        raise ValueError('Unsupported format')

    device.setperiodsize(320)

    data = f.readframes(320)
    while data:
        # Read data from stdin
        device.write(data)
        data = f.readframes(320)


def morse_to_text(text, seperator=" / "):
    """translate dash dot morse code to ascii text"""
    translated = []
    words = text.split(seperator)
    for word in words:
            clear = []
            chars = word.split()
            for c in chars:
                    clear.append(reverse_morsetab[c])
            translated.append(''.join(clear))

    return ' '.join(translated)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description='a simple morse generator and translator',
        formatter_class=argparse.HelpFormatter)

    parser.add_argument("-o", help="Specify the output format: text or sound",
                        choices=['text', 'sound'])
    parser.add_argument('-f', help="Specify the file to write", action='store',
                            type=str)
    parser.add_argument('-d', action='store', default='default')
    parser.add_argument('args', nargs=argparse.REMAINDER)

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit()

    if args.o == 'sound':
        morse = text_to_morse(' '.join(args.args))
        f = morse_to_wav(morse, file_=args.f)
        if not args.f:
            play(f)
    else:
        text = ' '.join(args.args)
        if re.search("[a-z]+", text.lower()):
            conv = text_to_morse(text)
        else:
            conv = morse_to_text(text)
        if not args.f:
            sys.stdout.write(''.join(conv))
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            f = open(args.f, 'w')
            f.write(morse+'\n')


