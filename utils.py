import pygame

infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)


def percent_of_screen_width(percent_w):
    return int(screen_size[0] * (percent_w / 100))


def percent_of_screen_height(percent_h):
    return int(screen_size[1] * (percent_h / 100))
