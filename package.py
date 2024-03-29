name = "usd_katana_pxr"

version = "19.07"

authors = [
    "Pixar"
]

description = \
    """
    USD plugin for Foundry Katana from Pixar's repository.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "katana-3.2+",
    "usd_core-{version}".format(version=str(version))
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "usd_katana-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python")
    env.KATANA_RESOURCES.append("{root}/third_party/katana/plugin")
    env.KATANA_POST_PYTHONPATH.append("{root}/third_party/katana/lib")

    # Helper environment variables.
    env.USD_KATANA_INCLUDE_PATH.set("{root}/include")
    env.USD_KATANA_LIBRARY_PATH.set("{root}/lib")
