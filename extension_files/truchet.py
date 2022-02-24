import inkex
import random


class Truchet(inkex.EffectExtension):
    
    def add_arguments(self, pars):
        pars.add_argument("--columns", type=int, default=8, help="Columns")
        pars.add_argument("--rows", type=int, default=8, help="Rows")

    
    def effect(self):

        num_tile_types = len(self.svg.selected)

        # Exit if there aren't any tiles selected
        if (num_tile_types == 0):
            inkex.errormsg("Nothing Selected")
            exit()

        tile_types = []

        for selected in self.svg.selected:
            tile = selected.copy()
            bb = tile.bounding_box()
            transform  = inkex.Transform(translate=(-bb.left, -bb.top))
            tile.transform = transform*tile.transform
            tile_types.append(tile)


        # TODO: Make sure that tiles are the same size


        # Create new empty group for tiles to go in
        group = self.svg.get_current_layer().add(inkex.Group(id=f"truchet"))

        # Generate tiling
        for i in range(self.options.columns):
            for j in range(self.options.rows):
                tile = tile_types[random.randint(0, num_tile_types -1)].copy()
                bb = tile.bounding_box()
                # Transformation done in specific order where rotation is done relative to original postion
                t  = inkex.Transform(translate=(i*bb.width, j*bb.height))
                t.add_rotate(90*random.randint(0, 3), bb.center_x, bb.center_y)
                tile.transform =  t * tile.transform
                group.add(tile)


if __name__ == '__main__':
    truchet = Truchet()
    truchet.run()
