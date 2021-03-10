scene.set_background_image(assets.image("""
    entrance1
"""))
game.show_long_text("One hall is dim, but lit. One hall is pitch black. Which hall will you go down?",
    DialogLayout.BOTTOM)
pause(2000)
game.show_long_text("Press A for the dim hall or B for the dark hall",
    DialogLayout.BOTTOM)
pause(100)
if controller.A.is_pressed():
    scene.set_background_image(assets.image("""
        dimHall
    """))
    game.show_long_text("You hear a humming", DialogLayout.BOTTOM)
    pause(1000)
    scene.set_background_image(assets.image("""
        nice man
    """))
    pause(1000)
    game.show_long_text("The man in front of you is the source of the humming. Do you greet him (press A), or try to sneak past him (press B)?",
        DialogLayout.BOTTOM)
    if controller.A.is_pressed():
        game.show_long_text("You decide to greet him", DialogLayout.BOTTOM)
        pause(1000)
        game.show_long_text("You walk over to the man, tap him on the shoulder, and greet him.",
            DialogLayout.BOTTOM)
        pause(200)
        game.show_long_text("The man frantically gets up and slams you against the wall and says disappointedly \"Yet another creature of this dungeon to slay.\" and points his sword at you.",
            DialogLayout.BOTTOM)
        game.show_long_text("Do you beg (press A), or struggle (press B)? ",
            DialogLayout.BOTTOM)
        pause(100)
        if controller.A.is_pressed():
            game.show_long_text("\"Huh? groveling? Creatures in this dungeon would have struggled or retaliated, lucky for you I know the difference.\" the man says.",
                DialogLayout.BOTTOM)
            pause(1000)
            game.show_long_text("\"Sorry for the trouble\" he says as he lets you go. \"I'm Hedrial, a former knight.\"",
                DialogLayout.BOTTOM)
            pause(200)
            game.show_long_text("\"Sorry, I've been in this dungeon for some time now and I'm a bit paranoid.\" the knight says to you.",
                DialogLayout.BOTTOM)
            pause(200)
            game.show_long_text("\"I have a favor to ask of you.\" the knight says timidly.",
                DialogLayout.BOTTOM)
            pause(200)
            game.show_long_text("\"May I join you in exploring this dungeon, its real lonely down here and I could be of some use in showing you the secret passages I know?\" the knight asks.",
                DialogLayout.BOTTOM)
            pause(200)
            game.show_long_text("Will you allow him to accompany you? Press A for yes and B for no.",
                DialogLayout.BOTTOM)
            if controller.A.is_pressed():
                game.show_long_text("Oh! Thank you, kind adventurer, now we shall explore this horrid place together!",
                    DialogLayout.BOTTOM)
                pause(200)
                game.show_long_text("YOU'VE ACHIEVED THE ADVENTURES WANDER TOGETHER ENDING!",
                    DialogLayout.BOTTOM)
            else:
                game.show_long_text("YOU'VE ACHIEVED THE LONE ADVENTURE ENDING!",
                    DialogLayout.BOTTOM)
        else:
            game.show_long_text("The man stabs you with his sword, ending your journey.",
                DialogLayout.BOTTOM)
    else:
        game.show_long_text("You decide to sneak past the man.", DialogLayout.BOTTOM)
        pause(1000)
        game.show_long_text("You successfully sneak past the man, but you are at a crossroads.",
            DialogLayout.BOTTOM)
        pause(500)
        game.show_long_text("TO BE CONTINUED!", DialogLayout.BOTTOM)
else:
    scene.set_background_image(assets.image("""
        Dark Hall
    """))
    game.show_long_text("You can't see anything, no matter how hard you try",
        DialogLayout.BOTTOM)
    pause(100)
    game.show_long_text("You feel two buttons: a round one and a square one. Which one will you push?",
        DialogLayout.BOTTOM)
    game.show_long_text("Push A for round one, push B for the square one",
        DialogLayout.BOTTOM)
    if controller.A.is_pressed():
        game.show_long_text("You hear a low mechanical noise behind the walls. You decide to wait for it to stop.",
            DialogLayout.BOTTOM)
        pause(100)
        scene.set_background_image(assets.image("""
            BlueHeat
        """))
        game.show_long_text("TO BE CONTINUED!", DialogLayout.BOTTOM)
    else:
        game.show_long_text("TO BE CONTINUED!", DialogLayout.BOTTOM)