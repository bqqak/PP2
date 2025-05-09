import pygame

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Just fun")
time = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

count = 0
mx_score = 0
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))
player_surf = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render("Dastan Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 340))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
    if game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_rect.x -= 10
        if keys[pygame.K_RIGHT]: player_rect.x += 10
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))


        score = display_score()
        screen.blit(snail_surf, snail_rect)
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300

        screen.blit(player_surf, player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))

        score_mx_message = test_font.render(f'Your max score: {mx_score}', False, '#FF9933')
        score_mx_message_rect = score_mx_message.get_rect(center = (400, 360))
        screen.blit(game_name, game_name_rect)
        if score == 0: screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
            if score > mx_score:
                mx_score = score
            screen.blit(score_mx_message, score_mx_message_rect)
    pygame.display.update()
    time.tick(60)