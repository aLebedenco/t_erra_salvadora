p_ombo_perdido: Sprite = None
scene.set_background_color(15)
scene.set_background_image(img("""
    ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ......................................................................11111.......11111...........................11111.........................11111...........
        ........11111.........11111............11111..........................11111.......11111...........................11111.........................11111.....11111.
        ........11111.........11111............11111..........................11111.......11111............11111..........11111.........................11111.....11111.
        ........11111.........11111............11111..........................11111.......11111............11111..........11111.........................11111.....11111.
        ........11111.........11111............11111..........11111...........11111.......11111....11111...11111..........11111............11111........11111.....11111.
        ........11111.........11111............11111..........11111................................11111...11111...........................11111..................11111.
        ......................................................11111................11111...........11111...11111...........................11111........................
        ......................................................11111................11111...........11111...................................11111.....11111..............
        ......................................................11111................11111...........11111............11111..................11111.....11111..............
        ...........................................................................11111............................11111......11111.................11111..............
        ...........................................................................11111............................11111......11111.................11111..............
        ..........................................11111.............................................................11111......11111.................11111.....11111....
        ..........................................11111.............................................................11111......11111...........................11111....
        ..........................................11111........................................................................11111..............11111........11111....
        ..........................................11111...........................................................................................11111........11111....
        ....................11111.................11111...........................................................................................11111........11111....
        ....................11111.................................................................................................................11111.................
        ....................11111....................................................................11111................11111...................11111.................
        ....................11111.............................................11111..................11111................11111.........................................
        ....................11111..............................11111..........11111..................11111................11111.........................................
        .......11111...........................................11111..........11111..................11111.....11111......11111...........11111.........................
        .......11111...........................................11111..........11111..................11111.....11111......11111...........11111...........11111.........
        .......11111...........................................11111..........11111............................11111......................11111...........11111.........
        .......11111...........................................11111...........................................11111......................11111...........11111.........
        .......11111...........................................................................................11111......................11111...........11111.........
        ......................11111.......................................................................................................................11111.........
        ......................11111......................................................................................11111.....................................11111
        ......................11111.....111111..................11111...................................11111............11111.....................................11111
        ......................11111.....111111..................11111...................................11111............11111.......11111.....11111...............11111
        ......................11111.....111111..................11111...................................11111............11111.......11111.....11111...............11111
        ................................111111...11111..........11111...................................11111............11111.......11111.....11111...............11111
        ........11111...................111111...11111..........11111...................................11111...11111................11111.....11111......11111.........
        ........11111............................11111...............................11111......................11111................11111.....11111......11111.........
        ........11111............................11111...............................11111......................11111.....................................11111.........
        ........11111............................11111...............................11111......................11111.....................................11111.........
        ........11111................................................................11111......................11111.........11111.......................11111.........
        .............................................................................11111....................................11111.....................................
        ................................................................11111.................................................11111.....................................
        .......................11111....................................11111.................................................11111.....................................
        .......................11111....................................11111.................................................11111.....................................
        .......................11111111.................................11111....................11111..................................................................
        .......................11111111......................11111......11111....................11111...........11111......................11111.......................
        .........11111.........11111111......................11111...............................11111...........11111......................11111.......................
        .........11111............11111......11111...........11111...............................11111...........11111......................11111.......11111...........
        .........11111............11111......11111...........11111...............................11111...........11111......................11111.......11111...........
        .........11111.......................11111...........11111...............................................11111......................11111.......11111...........
        .........11111.......................11111......................................................................................................11111...........
        .....................................11111......................................................................................................11111...........
        ................................................................................................................................................................
        ..........................................................................11111.................................................................................
        ..........................................11111...........................11111.........................................................................11111...
        .......11111.........11111................11111...........................11111.........................................................................11111...
        .......11111.........11111................11111...........................11111.......11111.....................................11111...................11111...
        .......11111.........11111................11111...........................11111.......11111.....................................11111...................11111...
        .......11111.........11111................11111.......................................11111............11111....................11111...................11111...
        .......11111.........11111............................................................11111............11111....................11111...........................
        ......................................................................................11111............11111....................11111...........................
        .......................................................................................................11111....................................................
        ...................................................................11111...............................11111....................................................
        ...................................................................11111........................................................................................
        ...................................................................11111.......................11111............................................................
        ..............11111.11111..........................................11111.......................11111...............11111........................................
        ..............11111.11111..........................................11111....11111..............11111...............11111........................................
        ..............11111.11111...................................................11111..............11111...............11111........................................
        ..............11111.11111...................................................11111..............11111...............11111........................................
        ..............11111.11111...............................11111...............11111..................................11111........................................
        ........................................................11111...............11111...............................................................................
        ........................................................11111...................................................................................................
        ..........................................11111.........11111...................................................................................................
        ..........................................11111.........11111.......................................................................................11111.......
        ..........................................11111...........................................................................................11111.....11111.......
        ..........................................11111......................................................11111.....................11111......11111.....11111.......
        ..........................................11111......................................................11111.....................11111......11111.....11111.......
        .....................................................................................................11111.....................11111......11111.....11111.......
        .....................................................................................................11111..........11111......11111......11111.................
        .....................................................................................................11111..........11111......11111............................
        ....................................................................................................................11111.......................................
        ......................11111.........................................................................................11111.......................................
        ......................11111.........................................................................................11111.......................................
        ......................11111..............................................11111..................................................................................
        ......................11111..............................................11111..................................................................11111...........
        .............11111....11111..............................................11111..................................................................11111...........
        .............11111............11111......................................11111..............................................11111...............11111...........
        .............11111............11111......................................11111..............................................11111...............11111...........
        .............11111............11111.........................................................................................11111...............11111...........
        .............11111............11111.........................................................................................11111...............................
        ..............................11111............................................................................11111........11111...............................
        ...............................................................................................................11111............................................
        ...............................................................................................................11111.....................................11111..
        ........................11111..................................................................................11111.....................................11111..
        ........................11111..................................................................................11111.....................................11111..
        ........................11111..........................................................11111.............................................................11111..
        ........................11111..........................................................11111..................................11111.......11111..........11111..
        ........................11111..........................................................11111..................................11111.......11111.................
        ................................................11111..................................11111..................................11111.......11111.................
        ................................................11111..................................11111..................................11111.......11111.................
        ................................................11111.........................................................................11111.......11111.................
        ................................................11111......11111................................................................................................
        ......11111.....................................11111......11111................................................................................................
        ......11111................................................11111................................................................................................
        ......11111................................................11111................................................................................................
        ......11111.......11111....................................11111................................................................................................
        ......11111.......11111.........................................................................................11111...........................................
        ..................11111.........................................................................................11111...............................11111.......
        ..................11111.........................................................................................11111...............................11111.......
        ..................11111.........................................................................................11111...............................11111111....
        ................................................................................................................11111...............................11111111....
        ...........................................................11111..............................11111.................................................11111111....
        ...........................................11111...........11111..............................11111...............................11111................11111....
        .............................11111.........11111...........11111..............................11111...............................11111................11111....
        .............................11111.........11111...........11111..............................11111...............................11111.........................
        .............................11111.........11111...........11111............11111.............11111...............................11111.........................
        .............................11111.........11111............................11111.................................................11111.........................
        .............................11111..........................................11111...............................................................................
        ............................................................................11111...............................................................................
        ............................................................................11111...............................................................................
        ................................................................................................................................................................
"""))
t_erra = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . 6 6 6 5 5 f f 6 . . . . 
            . . . 7 7 7 7 6 6 f 1 6 6 . . . 
            . . 6 7 7 7 7 8 8 8 8 6 6 6 . . 
            . . 7 7 7 7 7 8 8 8 8 1 . 1 . . 
            . 6 7 7 7 7 8 8 8 8 8 e . . . . 
            . 6 7 7 7 8 8 8 6 6 6 e e . . . 
            . 6 6 7 7 8 8 6 6 6 6 . e e e . 
            . 6 8 7 7 8 8 6 6 6 6 1 . 1 e e 
            . . 6 8 7 7 8 6 6 6 6 8 8 6 . . 
            . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
            . . . 6 8 8 8 8 8 8 8 8 6 . . . 
            . . . . 6 6 8 8 8 8 6 6 . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
t_erra.scale = 4
controller.move_sprite(t_erra, 100, 100)
animation.run_image_animation(t_erra,
    [img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 f f 6 . . . . 
                . . . 7 7 7 7 6 6 f 1 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 8 6 6 6 . . 
                . . 7 7 7 7 7 8 8 8 8 1 . 1 . . 
                . 6 7 7 7 7 8 8 8 8 8 e . . . . 
                . 6 7 7 7 8 8 8 6 6 6 e e . . . 
                . 6 6 7 7 8 8 6 6 6 6 . e e e . 
                . 6 8 7 7 8 8 6 6 6 6 1 . 1 e e 
                . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 f f 6 . . . . 
                . . . 7 7 7 7 6 6 f 1 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 8 6 6 6 . . 
                . . 7 7 7 7 7 8 8 8 8 1 . 1 . . 
                . 6 7 7 7 7 8 8 8 8 8 e . . . . 
                . 6 7 7 7 8 8 8 6 6 6 e e . e e 
                . 6 6 7 7 8 8 6 6 6 6 . e e e . 
                . 6 8 7 7 8 8 6 6 6 6 1 . 1 . . 
                . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . 6 6 6 5 5 f f 6 . . . . 
                . . . 7 7 7 7 6 6 f 1 6 6 . . . 
                . . 6 7 7 7 7 8 8 8 8 6 6 6 . . 
                . . 7 7 7 7 7 8 8 8 8 1 . 1 . . 
                . 6 7 7 7 7 8 8 8 8 8 e . . e e 
                . 6 7 7 7 8 8 8 6 6 6 e e . e . 
                . 6 6 7 7 8 8 6 6 6 6 . e e e . 
                . 6 8 7 7 8 8 6 6 6 6 1 . 1 . . 
                . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                . . . . 6 6 8 8 8 8 6 6 . . . . 
                . . . . . . 6 6 6 6 . . . . . . 
                . . . . . . . . . . . . . . . .
        """)],
    500,
    True)
info.set_score(0)
t_erra.set_stay_in_screen(True)

def on_update_interval():
    global p_ombo_perdido
    p_ombo_perdido = sprites.create(img("""
            ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    .......11111111.................
                    .....1199999999111..............
                    ...1191999999999911.............
                    ..11999199999999991.............
                    .119999999999999991.............
                    .1999999ccccc999991.............
                    119999ccbbbbbc99991.............
                    1999ccddbbbbbbf9991.............
                    199cbbbddbbffbf9991.............
                    1199ffffdbbffbff991.............
                    .119999fbbbbbbbf991.............
                    ..11999fbbbbbbbff91.............
                    ...119ffbbbbbbbbfff11...........
                    ....19f6bbbbbb663ddcc1..........
                    ....1cc66bbbb666dddddc1.........
                    ....1cd36666663dddddddc1........
                    ....1cddd3333dbddddddbcc1.......
                    ....1cddddddddbdddddbbddc1......
                    ....1cddddddddbbdddbbdddbc111...
                    ....11cddddddddbbdbbddddbbccc1..
                    .....1ccddddddddbbbbcccccbbbcc1.
                    .....11ccddddddddddddddbccffff1.
                    ......11cccbddccbddddbbfff11111.
                    .......1c333bb333cbbfff1111.....
                    ........c33cc33cc3fff11.........
        """),
        SpriteKind.projectile)
    p_ombo_perdido.set_velocity(-50, -50)
    p_ombo_perdido.set_position(160, randint(0, 200))
game.on_update_interval(1000, on_update_interval)
while True:
    pause(500)
    