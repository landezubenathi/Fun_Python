import pygame
import GetDate

pygame.init()

screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("My First GUI")

font = pygame.font.Font(None,41)
fname = font.render("Time Now", True, ("darkcyan"))
mname = font.render("Is", True, ("Cyan"))
sname = font.render(str(GetDate.get_current_time()), True, ("Light Cyan"))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((0,0,0))
        screen.blit(fname,(100, 100))
        screen.blit(mname,(100, 125))
        screen.blit(sname,(100, 150))
        pygame.display.flip()

pygame.quit()
