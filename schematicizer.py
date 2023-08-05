from litemapy import Region, BlockState, TileEntity
from nbtlib import parse_nbt


# Blocks being used.
command_block = BlockState("minecraft:command_block", properties={'facing':'south'})
chain_command_block = BlockState("minecraft:chain_command_block", properties={'facing':'south'})
repeating_command_block = BlockState("minecraft:repeating_command_block", properties={'facing':'south'})
stone = BlockState('minecraft:stone')
smooth_stone = BlockState('minecraft:smooth_stone')
lamp = BlockState('minecraft:redstone_lamp')
torch = BlockState('minecraft:redstone_wall_torch', properties={'facing':'south'})


# Takes a list of Minecraft commands (technically a list of lists of Minecraft commands...)
# and makes a schematic of command blocks with those commands pre-filled.
def schematicize(chapter, title):

    # Makes sure chapter is a list and not an iterator.
    chapter = list(chapter)

    # Gets dimensions with some buffer space for control circuits.
    x_length = len(chapter) + 4
    z_length = max(len(paragraph) for paragraph in chapter) + 1

    # Constructs a region/schematic object with Litemapy.
    reg = Region(0, 0, 0, x_length, 1, z_length)
    schem = reg.as_schematic(name=title, author="WSJ")

    # Adds the commands to the schematic as command blocks.
    for par_idx, paragraph in enumerate(chapter):
        for sen_idx, sentence in enumerate(paragraph):

            # X/Z dimensions match up with paragrpahs/sentences.
            x = par_idx + 4
            z = sen_idx + 1

            # Places the appropriate kind of command blocks.
            block = chain_command_block if sen_idx else repeating_command_block
            reg.setblock(par_idx + 4, 0, sen_idx + 1, block)

            # Creates NBT data as a string.
            nbt_str = '{Command: "' + sentence + '"'
            nbt_str += ', x:' + str(x) + ', y:0, z:' + str(z)
            nbt_str += ', auto:' + ('1' if sen_idx else '0') + '}'

            # Adds the NBT data to the schematic as a TileEntity.
            reg.tile_entities.append(TileEntity(parse_nbt(nbt_str)))

    # Adds a control circuit.
    reg.setblock(0, 0, 0, lamp)
    reg.setblock(1, 0, 0, smooth_stone)
    reg.setblock(1, 0, 1, torch)
    reg.setblock(2, 0, 0, command_block)
    reg.setblock(2, 0, 1, command_block)

    # TileEntity data for the control circuit.
    nbt_str = '{Command:"fill ~2 ~ ~ ~' + str(x_length - 3) + ' ~ ~ redstone_block"'
    nbt_str += ', x:2, y:0, z:0, auto:0}'
    reg.tile_entities.append(TileEntity(parse_nbt(nbt_str)))
    nbt_str = '{Command:"fill ~2 ~ ~-1 ~' + str(x_length - 3) + ' ~ ~-1 stone"'
    nbt_str += ', x:2, y:0, z:1, auto:0}'
    reg.tile_entities.append(TileEntity(parse_nbt(nbt_str)))

    # Pre-fills the control circuit to 'off'.
    for x in range(4, x_length):
        reg.setblock(x, 0, 0, stone)

    # Saves everything as a schematic file.
    schem.save(title + '.litematic')
