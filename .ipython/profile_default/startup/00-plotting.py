import sys, os

def notify_loaded(module, alias=None):
    msg = f"Module {module} loaded"
    if alias is not None:
        msg += f" with alias {alias}"
    print(msg)
def notify_notfound(module):
    print(f"Warning: module {module} not found")

try:
    import matplotlib as mpl
    from matplotlib import pyplot as plt
    from matplotlib import animation
    if "kitty" in os.environ.get("TERM", "xterm"):
        mpl.use("module://matplotlib-backend-kitty")
    else:
        mpl.use("module://matplotlib-backend-notcurses")
    plt.ion()
    notify_loaded("matplotlib", "mpl")
    notify_loaded("pyplot", "plt")
    notify_loaded("animation")
except ModuleNotFoundError:
    notify_notfound("matplotlib")
    notify_notfound("pyplot")
    notify_notfound("animation")
