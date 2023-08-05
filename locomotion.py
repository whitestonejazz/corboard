
# If 'max_dist' were any bigger, we'd lose floating point precision when multiplying.
max_dist = 128

# Common subsegments of locomotive commands.
preface = 'execute as @e[type=armor_stand] '
score_op = 'run scoreboard players operation '
condition = 'if score @s temp >= @s dist '

# Moves all armor stands to (0, 0, 0) then shifts them to their scoreboard coordinates.
def absolute_locomotion():


    # Prepares for positive 'x' movement.
    pos_x_commands = [
        preface + score_op + '@s dist = max_dist global',
        preface + score_op + '@s dist *= scale global',
        preface + score_op + '@s dist /= two global',
        preface + score_op + '@s temp = @s xpos',
    ]

    # Repeatedly cuts 'dist' in half and compares it to 'temp'.
    dist = max_dist / 2
    for _ in range(15):
        pos_x_commands.append(preface + 'at @s ' + condition + 'run tp ~' + str(dist) + ' ~ ~')
        pos_x_commands.append(preface + condition + score_op + '@s temp -= @s dist')
        pos_x_commands.append(preface + score_op + '@s dist /= two global')
        dist /= 2


    # Prepares for positive 'y' movement.
    pos_y_commands = [
        preface + score_op + '@s dist = max_dist global',
        preface + score_op + '@s dist *= scale global',
        preface + score_op + '@s dist /= two global',
        preface + score_op + '@s temp = @s ypos',
    ]

    # Repeatedly cuts 'dist' in half and compares it to 'temp'.
    dist = max_dist / 2
    for _ in range(15):
        pos_y_commands.append(preface + 'at @s ' + condition + 'run tp ~ ~' + str(dist) + ' ~')
        pos_y_commands.append(preface + condition + score_op + '@s temp -= @s dist')
        pos_y_commands.append(preface + score_op + '@s dist /= two global')
        dist /= 2


    # Prepares for positive 'z' movement.
    pos_z_commands = [
        preface + score_op + '@s dist = max_dist global',
        preface + score_op + '@s dist *= scale global',
        preface + score_op + '@s dist /= two global',
        preface + score_op + '@s temp = @s zpos',
    ]

    # Repeatedly cuts 'dist' in half and compares it to 'temp'.
    dist = max_dist / 2
    for _ in range(15):
        pos_z_commands.append(preface + 'at @s ' + condition + 'run tp ~ ~ ~' + str(dist))
        pos_z_commands.append(preface + condition + score_op + '@s temp -= @s dist')
        pos_z_commands.append(preface + score_op + '@s dist /= two global')
        dist /= 2


    # Prepares for negative 'x' movement.
    neg_x_commands = [
        preface + score_op + '@s dist = max_dist global',
        preface + score_op + '@s dist *= scale global',
        preface + score_op + '@s dist /= two global',
        preface + score_op + '@s temp = zero global',
        preface + score_op + '@s temp -= @s xpos',
    ]

    # Repeatedly cuts 'dist' in half and compares it to 'temp'.
    dist = max_dist / 2
    for _ in range(15):
        neg_x_commands.append(preface + 'at @s ' + condition + 'run tp ~-' + str(dist) + ' ~ ~')
        neg_x_commands.append(preface + condition + score_op + '@s temp -= @s dist')
        neg_x_commands.append(preface + score_op + '@s dist /= two global')
        dist /= 2


    # Prepares for negative 'y' movement.
    neg_y_commands = [
        preface + score_op + '@s dist = max_dist global',
        preface + score_op + '@s dist *= scale global',
        preface + score_op + '@s dist /= two global',
        preface + score_op + '@s temp = zero global',
        preface + score_op + '@s temp -= @s ypos',
    ]

    # Repeatedly cuts 'dist' in half and compares it to 'temp'.
    dist = max_dist / 2
    for _ in range(15):
        neg_y_commands.append(preface + 'at @s ' + condition + 'run tp ~ ~-' + str(dist) + ' ~')
        neg_y_commands.append(preface + condition + score_op + '@s temp -= @s dist')
        neg_y_commands.append(preface + score_op + '@s dist /= two global')
        dist /= 2


    # Prepares for negative 'z' movement.
    neg_z_commands = [
        preface + score_op + '@s dist = max_dist global',
        preface + score_op + '@s dist *= scale global',
        preface + score_op + '@s dist /= two global',
        preface + score_op + '@s temp = zero global',
        preface + score_op + '@s temp -= @s zpos',
    ]

    # Repeatedly cuts 'dist' in half and compares it to 'temp'.
    dist = max_dist / 2
    for _ in range(15):
        neg_z_commands.append(preface + 'at @s ' + condition + 'run tp ~ ~ ~-' + str(dist))
        neg_z_commands.append(preface + condition + score_op + '@s temp -= @s dist')
        neg_z_commands.append(preface + score_op + '@s dist /= two global')
        dist /= 2


    engine = [
        ['execute as @e[type=armor_stand] run tp @s 0 0 0'],
        pos_x_commands,
        pos_y_commands,
        pos_z_commands,
        neg_x_commands,
        neg_y_commands,
        neg_z_commands,
    ]

    return engine