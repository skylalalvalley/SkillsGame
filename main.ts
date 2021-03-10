controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    scene.setBackgroundImage(assets.image`Dark Hall`)
    game.showLongText("You can't see anything, no matter how hard you try", DialogLayout.Bottom)
    pause(100)
    game.showLongText("You feel two buttons: a round one and a square one. Which one will you push?", DialogLayout.Bottom)
    game.showLongText("Push A for round one, push B for the square one", DialogLayout.Bottom)
    if (controller.A.isPressed()) {
        game.showLongText("You hear a low mechanical noise behind the walls. You decide to wait for it to stop.", DialogLayout.Bottom)
        pause(100)
        game.showLongText("TO BE CONTINUED!", DialogLayout.Bottom)
    } else {
        game.showLongText("TO BE CONTINUED!", DialogLayout.Bottom)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    scene.setBackgroundImage(assets.image`dimHall`)
    game.showLongText("You hear a humming", DialogLayout.Bottom)
    pause(1000)
    scene.setBackgroundImage(assets.image`nice man`)
    pause(1000)
    game.showLongText("The man in front of you is the source of the humming. Do you greet him (press A), or try to sneak past him (press B)?", DialogLayout.Bottom)
    if (controller.A.isPressed()) {
        game.showLongText("You decide to greet him", DialogLayout.Bottom)
        pause(1000)
        game.showLongText("You walk over to the man, tap him on the shoulder, and greet him.", DialogLayout.Bottom)
        pause(200)
        game.showLongText("The man frantically gets up and slams you against the wall and says disappointedly \"Yet another creature of this dungeon to slay.\" and points his sword at you.", DialogLayout.Bottom)
        game.showLongText("Do you beg (press A), or struggle (press B)? ", DialogLayout.Bottom)
        pause(100)
        if (controller.A.isPressed()) {
            game.showLongText("\"Huh? groveling? Creatures in this dungeon would have struggled or retaliated, lucky for you I know the difference.\" the man says.", DialogLayout.Bottom)
            pause(1000)
            game.showLongText("\"Sorry for the trouble\" he says as he lets you go. \"I'm Hedrial, a former knight.\"", DialogLayout.Bottom)
            pause(200)
            game.showLongText("\"Sorry, I've been in this dungeon for some time now and I'm a bit paranoid.\" the knight says to you.", DialogLayout.Bottom)
            pause(200)
            game.showLongText("\"I have a favor to ask of you.\" the knight says timidly.", DialogLayout.Bottom)
            pause(200)
            game.showLongText("\"May I join you in exploring this dungeon, its real lonely down here and I could be of some use in showing you the secret passages I know?\" the knight asks.", DialogLayout.Bottom)
            pause(200)
            game.showLongText("Will you allow him to accompany you? Press A for yes and B for no.", DialogLayout.Bottom)
            if (controller.A.isPressed()) {
                game.showLongText("Oh! Thank you, kind adventurer, now we shall explore this horrid place together!", DialogLayout.Bottom)
                pause(200)
                game.showLongText("YOU'VE ACHIEVED THE ADVENTURES WANDER TOGETHER ENDING!", DialogLayout.Bottom)
            } else {
                game.showLongText("YOU'VE ACHIEVED THE LONE ADVENTURE ENDING!", DialogLayout.Bottom)
            }
        } else {
            game.showLongText("The man stabs you with his sword, ending your journey.", DialogLayout.Bottom)
        }
    } else {
        game.showLongText("You decide to sneak past the man.", DialogLayout.Bottom)
        pause(1000)
        game.showLongText("You successfully sneak past the man, but you are at a crossroads.", DialogLayout.Bottom)
        pause(500)
        game.showLongText("TO BE CONTINUED!", DialogLayout.Bottom)
    }
})
scene.setBackgroundImage(assets.image`entrance1`)
game.showLongText("One hall is dim, but lit. One hall is pitch black. Which hall will you go down?", DialogLayout.Bottom)
pause(2000)
game.showLongText("Press A for the dim hall or B for the dark hall", DialogLayout.Bottom)
pause(100)
