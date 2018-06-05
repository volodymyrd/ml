package(
    default_visibility = [
        "//visibility:private",
    ],
)

load("//third_party/tensorflow:tensorflow.bzl", "tf_cc_binary")
load("//third_party/tensorflow:tensorflow.bzl", "tf_cc_test")
load("//third_party/tensorflow:tensorflow.bzl", "tf_py_test")

py_library(
    name = "models",
    srcs = [
        "models.py",
    ],
    srcs_version = "PY2AND3",
    deps = [
        "//third_party/py/numpy",
        "//third_party/py/six",
        "//third_party/py/tensorflow",
    ],
)

py_library(
    name = "input_data",
    srcs = [
        "input_data.py",
    ],
    srcs_version = "PY2AND3",
    deps = [
        "//third_party/py/numpy",
        "//third_party/py/six",
        "//third_party/py/tensorflow",
    ],
)

py_binary(
    name = "train",
    srcs = [
        "train.py",
    ],
    srcs_version = "PY2AND3",
    deps = [
        ":input_data",
        ":models",
        "//third_party/py/numpy",
        "//third_party/py/six",
        "//third_party/py/tensorflow",
    ],
)