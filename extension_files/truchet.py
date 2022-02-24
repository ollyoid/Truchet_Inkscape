import inkex
import random


class Truchet(inkex.EffectExtension):
    
    def add_arguments(self, pars):
        pars.add_argument("--columns", type=int, default=8, help="Columns")
        pars.add_argument("--rows", type=int, default=8, help="Rows")

    
    def effect(self):
        # Check that something is infact selected
        if (len(self.options.ids) == 0):
            inkex.errormsg("Nothing selected")
            exit()


        # Create new empty group for tiles to go in
        group = self.svg.get_current_layer().add(inkex.Group(id=f"truchet"))

        # Generate tiling
        for i in range(self.options.columns):
            for j in range(self.options.rows):
                tile = self.svg.selected[0].copy()
                bb = tile.bounding_box()
                # Transformation done in specific order where rotation is done relative to original postion
                t  = inkex.Transform()
                t.add_translate(-bb.left + (i*bb.width), -bb.top +(j*bb.height))
                t.add_rotate(90*random.randint(0,3  ), bb.center_x, bb.center_y)
                tile.transform =  t * tile.transform
                group.add(tile)


if __name__ == '__main__':
    truchet = Truchet()
    truchet.run()
