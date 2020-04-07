import inspect
from subprocess import run

from coldtype.geometry import Rect
from coldtype.color import normalize_color


class RenderPass():
    def __init__(self, fn, suffix, args):
        self.fn = fn
        self.args = args
        self.suffix = suffix
        self.path = None
    
    async def run(self):
        if inspect.iscoroutinefunction(self.fn):
            return await self.fn(*self.args)
        else:
            return self.fn(*self.args)


class renderable():
    def __init__(self, rect=(1080, 1080), bg=0.1, hide=False, fmt="png"):
        self.hide = hide
        self.rect = Rect(rect)
        self.bg = normalize_color(bg)
        self.fmt = fmt
    
    def __call__(self, func):
        self.func = func
        return self
    
    def folder(self):
        return ""
    
    def passes(self, mode):
        return [RenderPass(self.func, self.func.__name__, [self.rect])]
    
    def package(self, filepath, output_folder):
        pass


class svgicon(renderable):
    def __init__(self, **kwargs):
        super().__init__(fmt="svg", **kwargs)


class iconset(renderable):
    valid_sizes = [16, 32, 64, 128, 256, 512, 1024]

    def __init__(self, sizes=[128, 1024], **kwargs):
        super().__init__(**kwargs)
        self.sizes = sizes
    
    def folder(self):
        return f"{self.func.__name__}_source"
    
    def passes(self, mode):
        sizes = self.sizes
        if mode == "render_all":
            sizes = self.valid_sizes
        return [RenderPass(self.func, str(size), [self.rect, size]) for size in sizes]
    
    def package(self, filepath, output_folder):
        iconset = filepath.parent / f"{filepath.stem}.iconset"
        iconset.mkdir(parents=True, exist_ok=True)

        for png in output_folder.glob("*.png"):
            d = int(png.stem.split("_")[1])
            for x in [1, 2]:
                if x == 2 and d == 16:
                    continue
                elif x == 1:
                    fn = f"icon_{d}x{d}.png"
                elif x == 2:
                    fn = f"icon_{int(d/2)}x{int(d/2)}@2x.png"
                print(fn)
            run(["sips", "-z", str(d), str(d), str(png), "--out", str(iconset / fn)])
        
        run(["iconutil", "-c", "icns", str(iconset)])