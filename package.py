name = "usd_katana"

version = "19.07"

authors = [
    "Pixar"
]

description = \
    """
    USD plugin for Foundry Katana.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "katana-3.2+",
    "usd-{version}".format(version=str(version))
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "usd_katana-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python")
    env.KATANA_RESOURCES.prepend("{root}/third_party/katana/plugin")
    env.KATANA_POST_PYTHONPATH.prepend("{root}/third_party/katana/lib")

    # Helper environment variables.
    env.USD_KATANA_BINARY_PATH.set("{root}/bin")
    env.USD_KATANA_INCLUDE_PATH.set("{root}/include")
    env.USD_KATANA_LIBRARY_PATH.set("{root}/lib")
