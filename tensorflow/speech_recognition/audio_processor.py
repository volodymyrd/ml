import tensorflow as tf

from tensorflow.contrib.framework.python.ops import audio_ops as contrib_audio
from tensorflow.python.ops import io_ops
from tensorflow.python.platform import gfile
from tensorflow.python.util import compat


class AudioProcessor:

    def processing(self):
        self.wav_filename_placeholder_ = tf.placeholder(tf.string, [])
        wav_loader = io_ops.read_file(self.wav_filename_placeholder_)
        wav_decoder = contrib_audio.decode_wav(wav_loader, desired_channels=1)
        search_path = os.path.join(self.data_dir, BACKGROUND_NOISE_DIR_NAME,
                               '*.wav')
        for wav_path in gfile.Glob(search_path):
            wav_data = sess.run(
                wav_decoder,
                feed_dict={wav_filename_placeholder: wav_path}).audio.flatten()
            self.background_data.append(wav_data)
        if not self.background_data:
            raise Exception('No background wav files were found in ' + search_path)

def main():
    audioProccessor = AudioProcessor()
    donald.processing()


if __name__ == '__main__': main()