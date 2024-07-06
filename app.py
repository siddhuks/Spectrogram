# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import os
# import librosa
# import matplotlib
# matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI environments
# import matplotlib.pyplot as plt
# import numpy as np

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# def generate_spectrogram(audio_file_path, output_image_path):
#     y, sr = librosa.load(audio_file_path)
#     S = librosa.feature.melspectrogram(y=y, sr=sr)
#     S_DB = librosa.power_to_db(S, ref=np.max)

#     plt.figure(figsize=(10, 4))
#     librosa.display.specshow(S_DB, sr=sr, x_axis='time', y_axis='mel')
#     plt.colorbar(format='%+2.0f dB')
#     plt.title('Mel-frequency spectrogram')
#     plt.tight_layout()
#     plt.savefig(output_image_path)
#     plt.close()

# @app.route('/generate-spectrogram', methods=['POST'])
# def generate_spectrogram_endpoint():
#     try:
#         file = request.files['audio']
#         filename = file.filename
#         file_path = os.path.join('uploads', filename)
#         file.save(file_path)

#         output_image_path = os.path.join('spectrograms', filename.replace('.wav', '.png'))

#         if not os.path.exists('spectrograms'):
#             os.makedirs('spectrograms')

#         generate_spectrogram(file_path, output_image_path)
#         print(output_image_path)
#         return jsonify(success=True, image_path=output_image_path)
#     except Exception as e:
#         return jsonify(success=False, message=str(e))

# @app.route('/spectrograms/<filename>')
# def serve_spectrogram(filename):
#     return send_from_directory('spectrograms', filename)

# if __name__ == '__main__':
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     if not os.path.exists('spectrograms'):
#         os.makedirs('spectrograms')
#     app.run(port=8000)



from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import librosa
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI environments
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def generate_spectrogram(audio_file_path, output_image_path):
    y, sr = librosa.load(audio_file_path)
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_DB = librosa.power_to_db(S, ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_DB, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    plt.savefig(output_image_path)
    plt.close()

@app.route('/generate-spectrogram', methods=['POST'])
def generate_spectrogram_endpoint():
    try:
        file = request.files['audio']
        filename = file.filename
        file_path = os.path.join('uploads', filename)
        file.save(file_path)

        output_image_path = os.path.join('spectrograms', filename.rsplit('.', 1)[0] + '.png')

        if not os.path.exists('spectrograms'):
            os.makedirs('spectrograms')

        generate_spectrogram(file_path, output_image_path)
        print(output_image_path)
        return jsonify(success=True, image_path=output_image_path)
    except Exception as e:
        return jsonify(success=False, message=str(e))

@app.route('/spectrograms/<filename>')
def serve_spectrogram(filename):
    return send_from_directory('spectrograms', filename)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('spectrograms'):
        os.makedirs('spectrograms')
    app.run(port=9000)

