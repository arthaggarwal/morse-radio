import wave
import numpy as np


alphabet_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "Ä": ".-.-",
    "Ü": "..--",
    "ß": "...--..",
    "À": ".--.-",
    "È": ".-..-",
    "É": "..-..",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    ";": "-.-.-.",
    "?": "..--..",
    "-": "-....-",
    "_": "..--.-",
    "(": "-.--.",
    ")": "-.--.-",
    "'": ".----.",
    "=": "-...-",
    "+": ".-.-.",
    "/": "-..-.",
    "@": ".--.-.",
    "Ñ": "--.--",
    " ": " ",
    "" : ""
}

morse_to_alphabet = {v: k for k, v in alphabet_to_morse.items()}

def removeunusablecharacters(uncorrected_string):
    return filter(lambda char: char in alphabet_to_morse, uncorrected_string.upper())

def encode(decoded):
    morsestring = []

    decoded = "".join(removeunusablecharacters(decoded))
    decoded = decoded.upper()
    words = decoded.split(" ")
    for word in words:
        letters = list(word)

        morseword = []
        for letter in letters:
            morseletter = alphabet_to_morse[letter]
            morseword.append(morseletter)

        word = "/".join(morseword)
        morsestring.append(word)

    return " ".join(morsestring)

def decode(encoded):
    characterstring = []

    words = encoded.split(" ")
    for word in words:
        letters = word.split("/")

        characterword = []
        for letter in letters:
            characterletter = morse_to_alphabet[letter]
            characterword.append(characterletter)

        word = "".join(characterword)
        characterstring.append(word)

    return " ".join(characterstring)

# Constants for morse code sound
DOT_DURATION = 0.1  # in seconds
DASH_DURATION = 0.3  # in seconds
FREQUENCY = 750  # in Hz
SAMPLE_RATE = 44100  
AMPLITUDE = 32767  # max amplitude
SILENCE_DURATION = 0.1  # delay

def morse_to_wav(morse_code, output_file):
    def generate_tone(duration):
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        tone = AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * t)
        return tone.astype(np.int16)

    def generate_silence(duration):
        silence = np.zeros(int(SAMPLE_RATE * duration))
        return silence.astype(np.int16)

    audio = []

    for symbol in morse_code:
        if symbol == ".":
            audio.extend(generate_tone(DOT_DURATION))
        elif symbol == "-":
            audio.extend(generate_tone(DASH_DURATION))
        elif symbol == " ":
            # Add 7 units of silence for word spacing
            audio.extend(generate_silence(SILENCE_DURATION * 7))
        elif symbol == "/":
            # Add 3 units of silence for letter spacing
            audio.extend(generate_silence(SILENCE_DURATION * 3))
        audio.extend(generate_silence(SILENCE_DURATION))  # Add 1 unit of silence after each dot/dash

    audio = np.array(audio, dtype=np.int16)

    # Create the wav file
    with wave.open(output_file, "w") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit audio
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio.tobytes())
        
message = "  ALL GOOD  "
    
morse_code = encode(message)
print(f"Encoded Morse Code: {morse_code}")

output_file = "02_sound.wav"
morse_to_wav(morse_code, output_file)
print(f"WAV file '{output_file}' created successfully.")