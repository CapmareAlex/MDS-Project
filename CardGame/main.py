import pygame
from button import button
from PIL import Image

def pil_to_game(img):
    data = img.tobytes("raw", "RGBA")
    return pygame.image.fromstring(data, img.size, "RGBA")

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert("RGBA")

def loadBackground():
    global screen, scrInfo

    backgroundImage = Image.open("Assets\Gifs\poker-full-house.gif")
    currentFrame = 0

    # card = pygame.image.load("Assets\\newCards\Romb10.png")
    while True:
        clock = pygame.time.Clock()
        frame = pil_to_game(get_gif_frame(backgroundImage, currentFrame))
        frame = pygame.transform.scale(frame, (scrInfo.current_w, scrInfo.current_h))
        screen.blit(frame, (0, 0))
        # screen.blit(card, (400, 400))

        currentFrame = (currentFrame + 1) % (backgroundImage.n_frames // 3 - 16)

        if currentFrame == 0:
            break

        pygame.display.flip()
        clock.tick(10)

def loadTitle():
    global screen, scrInfo
    font = pygame.font.Font("Assets\Fonts\Pixeltype.ttf", 300)
    baseSurf = font.render("Minti", True, 'white')
    title = baseSurf.copy()
    titleRect = title.get_rect()
    titleRect.center = (scrInfo.current_w // 2, scrInfo.current_h // 2)

    # outLine = baseSurf.copy()
    # outLineRect = outLine.get_rect()
    # outLineRect.center = (scrInfo.current_w // 2 - 2, 302)

    alpha_surf = pygame.Surface(title.get_size(), pygame.SRCALPHA)
    alpha = 0

    while True:
        clock = pygame.time.Clock()
        title = baseSurf.copy()

        # alpha_surf.fill((0, 0, 0, alpha))
        # outLine.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        alpha_surf.fill((255, 255, 255, alpha))
        title.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # screen.blit(outLine, outLineRect)
        screen.blit(title, titleRect)
        pygame.display.update()

        alpha += 5
        if alpha > 255:
            break

        clock.tick(50)



def menu():
    global screen, currentFrame, backgroundImage, scrInfo

    scrWidth = scrInfo.current_w
    scrHeight = scrInfo.current_h
    buttonsX = scrWidth // 4
    buttonsY = scrHeight // 4
    incrementButtonY = scrHeight // 6
    incrementButtonX = scrWidth // 6

    playButton = button(position=(buttonsX, buttonsY), clr='white', cngclr='#150503', size=(200, 50), text='PLAY', font="Assets\Fonts\Pixeltype.ttf", font_size=30)
    optionsButton = button(position=(buttonsX, buttonsY + 3 * incrementButtonY), clr='white', cngclr='#150503', size=(200, 50), text='OPTIONS', font='Assets\Fonts\Pixeltype.ttf', font_size=30)
    howToPlayButton = button(position=(buttonsX + 3 * incrementButtonX, buttonsY), clr='white', cngclr='#150503', size=(200, 50), text='HOW TO PLAY', font='Assets\Fonts\Pixeltype.ttf', font_size=30)
    quitButton = button(position=(buttonsX + 3 * incrementButtonX, buttonsY + 3 * incrementButtonY), clr='white', cngclr='#150503', size=(200, 50), text='QUIT', font='Assets\Fonts\Pixeltype.ttf', font_size=30)

    playButton.draw(screen)
    optionsButton.draw(screen)
    howToPlayButton.draw(screen)
    quitButton.draw(screen)

    playButton.mouseover()
    optionsButton.mouseover()
    howToPlayButton.mouseover()

    if quitButton.mouseover():
        quitBtnAction()


def howToPlayButton(screen):
    global gameLoop, bgColor
    if pygame.mouse.get_pressed()[0]:
        screen.fill(bgColor)


def quitBtnAction():
    global gameLoop
    if pygame.mouse.get_pressed()[0]:
        gameLoop = False

##############################################################
pygame.init()

# Create game screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)

bgColor = '#251513'
gameLoop = True
scrInfo = pygame.display.Info()

screen.fill(bgColor)
loadBackground()
loadTitle()

while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            gameLoop = False

    menu()
    pygame.display.update()

pygame.quit()