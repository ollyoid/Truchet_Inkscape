import inkex
import random
import math


class Truchet(inkex.EffectExtension):
    
    def add_arguments(self, pars):
        pars.add_argument("--columns", type=int, default=8, help="Columns")
        pars.add_argument("--rows", type=int, default=8, help="Rows")
        pars.add_argument("--shape", type=str, default=8, help="Shape")

    
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


        # # To be used to make sure all tile dimensions are the same
        # bb1 = tile_types[0].bounding_box()
        # for tile in tile_types:
        #     bb = tile.bounding_box()
        #     if (bb.height != bb1.height) or (bb.width != bb1.width):
        #         inkex.errormsg("Tile dimensions don't match")
        #         exit()
        
        # TODO: Make sure that all input objects are valid


        # Create new empty group for tiles to go in
        group = self.svg.get_current_layer().add(inkex.Group(id=f"truchet"))

        # Generate tiling
        if self.options.shape == "rect":
            for i in range(self.options.columns):
                for j in range(self.options.rows):
                    tile = tile_types[random.randint(0, num_tile_types -1)].copy()
                    bb = tile.bounding_box()
                    # Transformation done in specific order where rotation is done relative to original postion
                    t  = inkex.Transform(translate=(i*bb.width, j*bb.height))
                    t.add_rotate(90*random.randint(0, 3), bb.center_x, bb.center_y)
                    tile.transform =  t * tile.transform
                    group.add(tile)
        elif self.options.shape == "hex":
            bb1 = tile_types[0].bounding_box()
            h_offset = bb1.width/2*math.sqrt(3)/3
            for i in range(self.options.columns):
                for j in range(self.options.rows):
                    tile = tile_types[random.randint(0, num_tile_types -1)].copy()
                    bb = tile.bounding_box()
                    # Transformation done in specific order where rotation is done relative to original postion
                    t  = inkex.Transform(translate=(i*bb.width+((j%2)*bb.width/2), j*(bb.height-h_offset)))
                    t.add_rotate(60*random.randint(0, 5), bb.center_x, bb.center_y)
                    tile.transform =  t * tile.transform
                    group.add(tile)


if __name__ == '__main__':
    truchet = Truchet()
    truchet.run()
