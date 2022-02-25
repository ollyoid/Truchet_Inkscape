import inkex
import random
import math


class TruchetPrepper(inkex.EffectExtension):

    def add_arguments(self, pars):
        pars.add_argument("--shape", type=str, default=8, help="Shape")
        pars.add_argument("--length", type=float, default=10.0, help="Edge Length")
        pars.add_argument("--grids", type=bool, default=False, help="Set up page grids")
        return

    def add_grid(self):
        if self.options.grids:
            if (self.options.shape == "tri") or (self.options.shape == "hex"):
                grid = inkex.Grid(type="axonomgrid")
            else:
                grid = inkex.Grid(type="xygrid")
            
            named_view = self.svg.namedview
            for g in named_view.findall("inkscape:grid"):
                g.delete()
            named_view.add(grid)
            named_view.set("showgrid", "true")
        return
    
    def effect(self):

        scale_transform = inkex.Transform(scale=self.options.length)

        current_layer = self.svg.get_current_layer()
        if self.options.shape == 'rect':
             template = inkex.PathElement(d="m -0.5,-0.5 h 1 v 1 h -1 z",
                                    style="fill:#000000;fill-opacity:0.1",
                                    label="truchet_square")
        elif self.options.shape == 'hex':
            template = inkex.PathElement(d="m 0,-1 -0.8660254,0.5 v 1 L 0,1 0.8660254,0.5 v -1 z",
                                    style="fill:#000000;fill-opacity:0.1",
                                    label="truchet_hex")
        elif self.options.shape == 'tri':
            template = inkex.PathElement(d="m 0.28867224,-0.499995 v 0.99999 L -0.57734448,0 Z",
                                    style="fill:#000000;fill-opacity:0.1",
                                    label="truchet_tri")

        template.transform = scale_transform
        template.apply_transform()

        bb = template.bounding_box()
        translate_transform = inkex.Transform(translate=(-round(bb.width), round(bb.height/2)))
        template.transform = translate_transform
        template.apply_transform()

        current_layer.add(template)
        self.add_grid()
        return




if __name__ == '__main__':
    prepper = TruchetPrepper()
    prepper.run()
