import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Bananagrams")
icon = pygame.image.load("Tile Pictures/B.png")
pygame.display.set_icon(icon)

# main menu pics
title = pygame.image.load("Extra Pics/title.png")
playButton = pygame.image.load("Extra Pics/playButton.png")
optionsButton = pygame.image.load("Extra Pics/optionsButton.png")
quitButton = pygame.image.load("Extra Pics/quitButton.png")

titleR = pygame.transform.rotozoom(title, 0, .5)
playButtonR = pygame.transform.rotozoom(playButton, 0, .5)
optionsButtonR = pygame.transform.rotozoom(optionsButton, 0, .5)
quitButtonR = pygame.transform.rotozoom(quitButton, 0, .5)

titleX = 50
titleY = 50
playButtonX = 600
playButtonY = 200
optionsButtonX = 600
optionsButtonY = 300
quitButtonX = 600
quitButtonY = 400

# options page pics
optionsTitle = pygame.image.load("Extra Pics/optionsTitle.png")
backButton = pygame.image.load("Extra Pics/backButton.png")

optionsTitleR = pygame.transform.rotozoom(optionsTitle, 0, .5)
backButtonR = pygame.transform.rotozoom(backButton, 0, .5)

optionsTitleX = 50
optionsTitleY = 50
backButtonX = 100
backButtonY = 400

# gameplay page pics
settingsIcon = pygame.image.load("Extra Pics/settingsIcon.png")

settingsIconR = pygame.transform.rotozoom(settingsIcon, 0, .5)

settingsIconX = 50
settingsIconY = 50


def main_menu_pics():
    screen.blit(titleR, (titleX, titleY))
    screen.blit(playButtonR, (playButtonX, playButtonY))
    screen.blit(optionsButtonR, (optionsButtonX, optionsButtonY))
    screen.blit(quitButtonR, (quitButtonX, quitButtonY))


def options_page_pics():
    screen.blit(optionsTitleR, (optionsTitleX, optionsTitleY))
    screen.blit(backButtonR, (backButtonX, backButtonY))


def game_page_pics():
    screen.blit(settingsIconR, (settingsIconX, settingsIconY))


def main_menu():
    global event
    running = True
    while running:
        screen.fill((178, 137, 107))

        print(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # play button, coords top left: (633, 216) bottom right: (945, 295)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_over(((633, 216), (945, 295)), pygame.mouse.get_pos()):
                print('play')
                game()

        # options button, coords top left: (633, 316) bottom right: (945, 395)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_over(((633, 316), (945, 395)), pygame.mouse.get_pos()):
                print('options')
                options()

        # quit button, coords top left: (633, 416) bottom right: (945, 495)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_over(((633, 416), (945, 495)), pygame.mouse.get_pos()):
                print('quit')
                running = False

        main_menu_pics()

        pygame.display.update()


def is_over(target, pos):
    if pos[0] > target[0][0] and pos[0] < target[1][0]:
        if pos[1] > target[0][1] and pos[1] < target[1][1]:
            return True
    return False


def options():
    global event
    running = True
    while running:
        screen.fill((178, 137, 107))
        options_page_pics()
        pygame.display.update()

        print(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # back button, coords top left: (633, 216) bottom right: (945, 295)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_over(((133, 416), (445, 495)), pygame.mouse.get_pos()):
                print('back')
                running = False


def game():
    global event
    running = True
    while running:
        screen.fill((178, 137, 107))
        game_page_pics()
        pygame.display.update()

        print(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # settings icon button, coords top left: (633, 216) bottom right: (945, 295)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_over(((50, 50), (130, 130)), pygame.mouse.get_pos()):
                print('back')
                running = False
                options()


main_menu()
