from absl import app as absl_app
from absl import flags
import tensorflow as tf

from official.utils.flags import core as flags_core


def define_mnist_flags():
    flags_core.define_base()
    flags_core.define_image()
    flags.adopt_module_key_flags(flags_core)
    flags_core.set_defaults(data_dir='/tmp/mnist_data',
                            model_dir='/tmp/mnist_model',
                            batch_size=100,
                            train_epochs=40)


def run_mnist(flags_obj):
    """Run MNIST training and eval loop.
    """
    print(flags_obj)

def main(_):
    run_mnist(flags.FLAGS)


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    define_mnist_flags()
    absl_app.run(main)
