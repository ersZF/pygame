import pygame
from PIL import Image
from random import randrange, choice
from time import time
import tkinter
import sys
import os
import sqlite3


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App:
    def __init__(self, bool_value):
        pygame.init()

        self.BACKGROUND_IMAGE_1_1 = resource_path('images/background_1_1.jpg')
        self.BACKGROUND_IMAGE_2_1 = resource_path('images/background_2_1.jpg')
        self.BACKGROUND_IMAGE_3_1 = resource_path('images/background_3_1.jpg')
        self.BACKGROUND_IMAGE_4_1 = resource_path('images/background_4_1.jpg')

        self.BACKGROUND_IMAGE_1_2 = resource_path('images/background_1_2.jpg')
        self.BACKGROUND_IMAGE_2_2 = resource_path('images/background_2_2.jpg')
        self.BACKGROUND_IMAGE_3_2 = resource_path('images/background_3_2.jpg')
        self.BACKGROUND_IMAGE_4_2 = resource_path('images/background_4_2.jpg')

        self.BACKGROUND_IMAGE_1_3 = resource_path('images/background_1_3.jpg')
        self.BACKGROUND_IMAGE_2_3 = resource_path('images/background_2_3.jpg')
        self.BACKGROUND_IMAGE_3_3 = resource_path('images/background_3_3.jpg')
        self.BACKGROUND_IMAGE_4_3 = resource_path('images/background_4_3.jpg')

        self.BACKGROUND_IMAGE_1_4 = resource_path('images/background_1_4.jpg')
        self.BACKGROUND_IMAGE_2_4 = resource_path('images/background_2_4.jpg')
        self.BACKGROUND_IMAGE_3_4 = resource_path('images/background_3_4.jpg')
        self.BACKGROUND_IMAGE_4_4 = resource_path('images/background_4_4.jpg')

        self.ICON = resource_path('images/icon.bmp')
        self.FONT = resource_path('fonts/font.ttf')
        self.BACKGROUND_MUSIC_MENU = resource_path('sounds/Menu_music.mp3')
        self.BACKGROUND_MUSIC_GAME = resource_path('sounds/Game_music.mp3')
        self.START_SOUND = resource_path('sounds/Start_sound.mp3')
        self.REBOUND_SOUND = resource_path('sounds/Rebound_sound.wav')
        self.VICTORY_SOUND = resource_path('sounds/Victory_sound.mp3')
        self.LOSE_SOUND = resource_path('sounds/Lose_sound.mp3')
        self.HIT_SOUND_1 = resource_path('sounds/Hit_sound_1.wav')
        self.HIT_SOUND_2 = resource_path('sounds/Hit_sound_2.wav')
        self.HIT_SOUND_3 = resource_path('sounds/Hit_sound_3.wav')
        self.HIT_SOUND_4 = resource_path('sounds/Hit_sound_4.wav')
        self.HIT_SOUND_5 = resource_path('sounds/Hit_sound_5.wav')

        self.LIST_HIT_SOUNDS = [
            self.HIT_SOUND_1, self.HIT_SOUND_2, self.HIT_SOUND_3, self.HIT_SOUND_4, self.HIT_SOUND_5]

        if (screen_width, screen_height) == (1440, 900) or (screen_width, screen_height) == (1366, 768) or \
                (screen_width, screen_height) == (1280, 720) or (screen_width, screen_height) == (1280, 800):
            self.BACKGROUND_IMAGE_1 = self.BACKGROUND_IMAGE_1_1
            self.BACKGROUND_IMAGE_2 = self.BACKGROUND_IMAGE_2_1
            self.BACKGROUND_IMAGE_3 = self.BACKGROUND_IMAGE_3_1
            self.BACKGROUND_IMAGE_4 = self.BACKGROUND_IMAGE_4_1
        elif (screen_width, screen_height) == (1600, 900) or (screen_width, screen_height) == (1536, 864):
            self.BACKGROUND_IMAGE_1 = self.BACKGROUND_IMAGE_1_2
            self.BACKGROUND_IMAGE_2 = self.BACKGROUND_IMAGE_2_2
            self.BACKGROUND_IMAGE_3 = self.BACKGROUND_IMAGE_3_2
            self.BACKGROUND_IMAGE_4 = self.BACKGROUND_IMAGE_4_2
        elif (screen_width, screen_height) == (1920, 1080):
            self.BACKGROUND_IMAGE_1 = self.BACKGROUND_IMAGE_1_3
            self.BACKGROUND_IMAGE_2 = self.BACKGROUND_IMAGE_2_3
            self.BACKGROUND_IMAGE_3 = self.BACKGROUND_IMAGE_3_3
            self.BACKGROUND_IMAGE_4 = self.BACKGROUND_IMAGE_4_3
        else:
            self.BACKGROUND_IMAGE_1 = self.BACKGROUND_IMAGE_1_4
            self.BACKGROUND_IMAGE_2 = self.BACKGROUND_IMAGE_2_4
            self.BACKGROUND_IMAGE_3 = self.BACKGROUND_IMAGE_3_4
            self.BACKGROUND_IMAGE_4 = self.BACKGROUND_IMAGE_4_4

        self.WIDTH = int(screen_width * (15 / 64))
        self.HEIGHT = int(screen_height * (5 / 6))

        self.CONN = sqlite3.connect('player_data.db')

        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 60
        self.score = 0
        self.flag_menu = bool_value

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.FONT_PROGRESS_BOARD = pygame.font.Font(self.FONT, self.HEIGHT // 60)

        self.FONT_END_INSCRIPTION = pygame.font.Font(self.FONT, self.HEIGHT // 20)
        self.FONT_VALUES_END_INSCRIPTION = pygame.font.Font(self.FONT, self.HEIGHT // 30)
        self.FONT_RESTART_INSCRIPTION = pygame.font.Font(self.FONT, self.HEIGHT // 40)
        self.FONT_EXIT_MENU = pygame.font.Font(self.FONT, self.HEIGHT // 24)

        self.FONT_HIGH_SCORE = pygame.font.Font(self.FONT, 20)
        self.FONT_START = pygame.font.Font(self.FONT, self.HEIGHT // 20)
        self.FONT_SETTINGS = pygame.font.Font(self.FONT, self.HEIGHT // 30)

        self.FONT_BACK = pygame.font.Font(self.FONT, self.HEIGHT // 24)
        self.FONT_INSCRIPTIONS_IN_SETTINGS = pygame.font.Font(self.FONT, self.HEIGHT // 48)
        self.FONT_NAMES_BACKGROUND_IMAGES = pygame.font.Font(self.FONT, self.HEIGHT // 60)

        self.FONT_QUANTITY_COLUMNS = pygame.font.Font(self.FONT, self.HEIGHT // 20)
        self.FONT_PLUS_AND_MINUS = pygame.font.Font(self.FONT, self.HEIGHT // 10)


        self.PROGRESS_BOARD_HEIGHT = self.HEIGHT // 12 + 20
        self.PROGRESS_BOARD = pygame.Rect(self.WIDTH, self.PROGRESS_BOARD_HEIGHT,
                                          self.WIDTH, self.PROGRESS_BOARD_HEIGHT)
        self.DELTA_V = self.WIDTH // 120
        self.BALL_DELTA_V = self.WIDTH // 200

        self.PLATFORM_WIDTH = int(self.WIDTH * (17 / 60))
        self.PLATFORM_HEIGHT = int(self.HEIGHT * (7 / 240))
        self.PLATFORM_SPEED = self.WIDTH // 50
        self.PLATFORM = pygame.Rect(int(self.WIDTH * (43 / 120)), (self.HEIGHT * (193 / 240)),
                                    self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT)


        self.BALL_RADIUS = int(self.WIDTH * (2 / 35))
        self.BALL_SPEED = self.WIDTH // 150
        self.SIDE_INSCRIBED_SQUARE = int(self.BALL_RADIUS * 2 ** 0.5)
        self.BALL = pygame.Rect(randrange(self.WIDTH // 6, int(self.WIDTH * (5 / 6))), int(self.HEIGHT * (17 / 24)),
                                self.SIDE_INSCRIBED_SQUARE, self.SIDE_INSCRIBED_SQUARE)
        self.DX, self.DY = choice([(1, -1), (-1, -1)])

        self.ROW = 5
        self.BLOCK_WIDTH = self.WIDTH // 6
        self.BLOCK_HEIGHT = self.HEIGHT // 24
        self.INDENT = self.WIDTH // 60
        self.BLOCK_X = self.BLOCK_WIDTH + 2 * self.INDENT
        self.BLOCK_Y = self.BLOCK_HEIGHT + 2 * self.INDENT

    def run(self):
        pygame.display.set_caption('Платформа и шар')
        pygame.display.set_icon(pygame.image.load(self.ICON))

        if self.flag_menu:
            App(True).display_menu()
        quantity_columns = change_quantity_columns()

        def get_tuples_pixels(image):
            set_colors = set()
            image = Image.open(image)
            pixels = image.load()
            x, y = image.size
            for i in range(x):
                for j in range(y):
                    r, g, b, *superfluous = pixels[i, j]
                    set_colors.add((r, g, b))
            return list(set_colors)

        list_tuples_pixels = get_tuples_pixels(change_background_image())

        list_black_blocks = [pygame.Rect(self.INDENT + self.BLOCK_X * j, self.INDENT + self.BLOCK_Y * i,
                                         self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
                             for j in range(self.ROW) for i in range(quantity_columns)]
        list_blocks = [pygame.Rect(self.INDENT + self.BLOCK_X * j, self.INDENT + self.BLOCK_Y * i,
                                   self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
                       for j in range(self.ROW) for i in range(quantity_columns)]
        list_colors = [choice(list_tuples_pixels) for __ in range(self.ROW) for _ in range(quantity_columns)]

        surface_with_progress_board = pygame.Surface((self.WIDTH, self.PROGRESS_BOARD_HEIGHT))
        pygame.draw.rect(surface_with_progress_board, self.BLACK, self.PROGRESS_BOARD)
        self.SCREEN.blit(surface_with_progress_board, (0, self.PROGRESS_BOARD_HEIGHT))

        pygame.mixer.music.load(self.BACKGROUND_MUSIC_GAME)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.7)
        self.REBOUND_SOUND = pygame.mixer.Sound(self.REBOUND_SOUND)
        self.REBOUND_SOUND.set_volume(0.7)

        start_time = time()

        while True:
            game_session_time = int(time() - start_time)

            [sys.exit() for event in pygame.event.get() if event.type == pygame.QUIT]

            self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))

            pygame.draw.rect(self.SCREEN, self.BLACK, self.PLATFORM.inflate(self.DELTA_V, self.DELTA_V))
            pygame.draw.rect(self.SCREEN, self.WHITE, self.PLATFORM)

            pygame.draw.circle(self.SCREEN, self.BLACK, self.BALL.center, self.BALL_RADIUS + self.BALL_DELTA_V)
            pygame.draw.circle(self.SCREEN, self.WHITE, self.BALL.center, self.BALL_RADIUS)

            [pygame.draw.rect(self.SCREEN, self.BLACK, block.inflate(self.DELTA_V, self.DELTA_V))
             for block in list_black_blocks]
            [pygame.draw.rect(self.SCREEN, list_colors[index], block) for index, block in enumerate(list_blocks)]

            self.BALL.x += int(self.BALL_SPEED * self.DX)
            self.BALL.y += int(self.BALL_SPEED * self.DY)

            def detection_collision(dx, dy, ball, rectangle):
                if dx > 0:
                    delta_x = ball.right - rectangle.left
                else:
                    delta_x = rectangle.right - ball.left
                if dy > 0:
                    delta_y = ball.bottom - rectangle.top
                else:
                    delta_y = rectangle.bottom - ball.top

                if delta_x >= delta_y:
                    dy = -dy
                elif delta_x < delta_y:
                    dx = -dx

                return dx, dy

            if self.BALL.centerx < self.BALL_RADIUS or self.BALL.centerx > self.WIDTH - self.BALL_RADIUS:
                self.DX = -self.DX
                self.REBOUND_SOUND.play()
            if self.BALL.centery < self.BALL_RADIUS:
                self.DY = -self.DY
                self.REBOUND_SOUND.play()
            if self.BALL.colliderect(self.PLATFORM) and self.DY > 0:
                self.DX, self.DY = detection_collision(self.DX, self.DY, self.BALL, self.PLATFORM)
                self.REBOUND_SOUND.play()
            if self.BALL.top - self.BALL_RADIUS > self.HEIGHT:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(self.LOSE_SOUND)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                App(None).display_end_inscription('ПОРАЖЕНИЕ!', self.score, self.WIDTH * (3 / 30), game_session_time)

            hit_index = self.BALL.collidelist(list_blocks)
            hit_index_black = self.BALL.collidelist(list_black_blocks)
            if hit_index != -1:
                hit_sound = pygame.mixer.Sound(choice(self.LIST_HIT_SOUNDS))
                hit_sound.set_volume(0.5)
                hit_sound.play()
                hit_rectangle = list_blocks.pop(hit_index)
                self.score += 1
                list_black_blocks.pop(hit_index_black)
                list_colors.pop(hit_index)
                self.DX, self.DY = detection_collision(self.DX, self.DY, self.BALL, hit_rectangle)
                self.BALL_SPEED += self.WIDTH * (1 / 2000) + 0.02
                if self.score == quantity_columns * self.ROW:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(self.VICTORY_SOUND)
                    pygame.mixer.music.set_volume(0.6)
                    pygame.mixer.music.play()
                    App(None).display_end_inscription('ПОБЕДА!', self.score, self.WIDTH * (4 / 15), game_session_time)

            key = pygame.key.get_pressed()
            if key[pygame.K_a] and self.PLATFORM.left > self.WIDTH // 30:
                self.PLATFORM.left -= self.PLATFORM_SPEED
            if key[pygame.K_d] and self.PLATFORM.right < self.WIDTH - self.WIDTH // 30:
                self.PLATFORM.right += self.PLATFORM_SPEED

            self.SCREEN.blit(surface_with_progress_board, (0, int(self.HEIGHT * (11 / 12))))

            render_inscription_score = self.FONT_PROGRESS_BOARD.render(
                f'СЧЕТ: {self.score}', True, self.WHITE, self.BLACK)
            self.SCREEN.blit(render_inscription_score, (self.WIDTH // 60, int(self.HEIGHT * (11 / 12))))

            render_inscription_time = self.FONT_PROGRESS_BOARD.render(
                f'ВРЕМЯ ИГРЫ: {game_session_time}', True, self.WHITE, self.BLACK)
            self.SCREEN.blit(render_inscription_time, (self.WIDTH // 60, int(self.HEIGHT * (113 / 120))))


            pygame.display.update()
            self.CLOCK.tick(self.FPS)

    def display_menu(self):
        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))

        pygame.mixer.music.load(self.BACKGROUND_MUSIC_MENU)
        pygame.mixer.music.play(-1, 0)
        pygame.mixer.music.set_volume(0.7)
        start_sound = pygame.mixer.Sound(self.START_SOUND)

        rect_high_score = pygame.Rect(int(self.WIDTH // 60), int(self.HEIGHT // 120),
                                      int(self.WIDTH * (5 / 12)), int(self.HEIGHT // 16))
        rect_start = pygame.Rect(int(self.WIDTH * (7 / 24)), int(self.HEIGHT * (13 / 24)),
                                 int(self.WIDTH * (5 / 12)), self.HEIGHT // 8)
        rect_settings = pygame.Rect(int(self.WIDTH * (7 / 24)), int(self.HEIGHT * (17 / 24)),
                                    int(self.WIDTH * (5 / 12)), self.HEIGHT // 8)

        black_start, white_start = (0, 0, 0), (255, 255, 255)
        black_settings, white_settings = (0, 0, 0), (255, 255, 255)

        while self.flag_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    if rect_start.collidepoint(event.pos):
                        white_start, black_start = (0, 0, 0), (255, 255, 255)
                    else:
                        black_start, white_start = (0, 0, 0), (255, 255, 255)
                    if rect_settings.collidepoint(event.pos):
                        white_settings, black_settings = (0, 0, 0), (255, 255, 255)
                    else:
                        black_settings, white_settings = (0, 0, 0), (255, 255, 255)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_start.collidepoint(event.pos):
                        pygame.mixer.music.stop()
                        start_sound.play()
                        pygame.time.wait(1000)
                        self.flag_menu = False
                    if rect_settings.collidepoint(event.pos):
                        App(None).display_settings(True)

            pygame.draw.rect(self.SCREEN, (0, 0, 0), rect_high_score, border_radius=int(self.WIDTH * (3 / 40)))
            high_score = self.CONN.cursor().execute("SELECT high_score FROM HighScoreAndTime").fetchone()[0]
            render_high_score_inscription = self.FONT_HIGH_SCORE.render(
                f'РЕКОРД: {high_score}', True, (255, 255, 255))
            self.SCREEN.blit(render_high_score_inscription, (int(self.WIDTH // 20), int(self.HEIGHT // 80)))

            game_session_time = self.CONN.cursor().execute(
                "SELECT game_session_time FROM HighScoreAndTime").fetchone()[0]
            render_game_session_time_inscription = self.FONT_HIGH_SCORE.render(
                f'ВРЕМЯ: {game_session_time}', True, (255, 255, 255))
            self.SCREEN.blit(render_game_session_time_inscription, (int(self.WIDTH // 20), int(self.HEIGHT * (3 / 80))))

            pygame.draw.rect(self.SCREEN, black_start, rect_start, border_radius=int(self.WIDTH * (3 / 40)))
            render_start_inscription = self.FONT_START.render('СТАРТ', True, white_start)
            self.SCREEN.blit(render_start_inscription, (int(self.WIDTH * (19 / 60)), int(self.HEIGHT * (133 / 240))))

            pygame.draw.rect(self.SCREEN, black_settings, rect_settings, border_radius=int(self.WIDTH * (3 / 40)))
            render_settings_inscription = self.FONT_SETTINGS.render('НАСТРОЙКИ', True, white_settings)
            self.SCREEN.blit(render_settings_inscription, (int(self.WIDTH * (10 / 40)), int(self.HEIGHT * (59 / 80))))

            pygame.display.update()

    def display_settings(self, flag_settings):
        global width_quantity_columns
        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))

        rect_back = pygame.Rect(int(self.WIDTH * (41 / 60)), int(self.HEIGHT * (109 / 120)),
                                int(self.WIDTH * (17 / 60)), int(self.HEIGHT * (3 / 40)))

        rect_first_name = pygame.Rect(int(self.WIDTH * (7 / 120)), self.HEIGHT // 12,
                                      int(self.WIDTH * (5 / 12)), self.HEIGHT // 24)
        rect_second_name = pygame.Rect(int(self.WIDTH * (8 / 15)), self.HEIGHT // 12,
                                       int(self.WIDTH * (5 / 12)), self.HEIGHT // 24)
        rect_thirst_name = pygame.Rect(int(self.WIDTH * (7 / 120)), self.HEIGHT // 6,
                                       int(self.WIDTH * (5 / 12)), self.HEIGHT // 24)
        rect_fourth_name = pygame.Rect(int(self.WIDTH * (8 / 15)), self.HEIGHT // 6,
                                       int(self.WIDTH * (5 / 12)), self.HEIGHT // 24)

        rect_plus = pygame.Rect(int(self.WIDTH * (19 / 30)), int(self.HEIGHT * (7 / 24)),
                                self.WIDTH // 6, self.HEIGHT // 12)
        rect_minus = pygame.Rect(self.WIDTH // 5, int(self.HEIGHT * (7 / 24)), self.WIDTH // 6, self.HEIGHT // 12)

        black_back, white_back = (0, 0, 0), (255, 255, 255)

        black_first_name, white_first_name = (0, 0, 0), (255, 255, 255)
        black_second_name, white_second_name = (0, 0, 0), (255, 255, 255)
        black_thirst_name, white_thirst_name = (0, 0, 0), (255, 255, 255)
        black_fourth_name, white_fourth_name = (0, 0, 0), (255, 255, 255)

        black_plus, white_plus = (0, 0, 0), (255, 255, 255)
        black_minus, white_minus = (0, 0, 0), (255, 255, 255)

        if 1 < change_quantity_columns() < 10:
            width_quantity_columns = int(self.WIDTH * (47 / 100))
        elif change_quantity_columns() == 1:
            width_quantity_columns = int(self.WIDTH * (19 / 40))
        elif change_quantity_columns() == 10:
            width_quantity_columns = int(self.WIDTH * (53 / 120))

        while flag_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    if rect_back.collidepoint(event.pos):
                        white_back, black_back = (0, 0, 0), (255, 255, 255)
                    else:
                        black_back, white_back = (0, 0, 0), (255, 255, 255)
                    if rect_first_name.collidepoint(event.pos):
                        white_first_name, black_first_name = (0, 0, 0), (255, 255, 255)
                    else:
                        black_first_name, white_first_name = (0, 0, 0), (255, 255, 255)
                    if rect_second_name.collidepoint(event.pos):
                        white_second_name, black_second_name = (0, 0, 0), (255, 255, 255)
                    else:
                        black_second_name, white_second_name = (0, 0, 0), (255, 255, 255)
                    if rect_thirst_name.collidepoint(event.pos):
                        white_thirst_name, black_thirst_name = (0, 0, 0), (255, 255, 255)
                    else:
                        black_thirst_name, white_thirst_name = (0, 0, 0), (255, 255, 255)
                    if rect_fourth_name.collidepoint(event.pos):
                        white_fourth_name, black_fourth_name = (0, 0, 0), (255, 255, 255)
                    else:
                        black_fourth_name, white_fourth_name = (0, 0, 0), (255, 255, 255)
                    if rect_plus.collidepoint(event.pos):
                        white_plus, black_plus = (0, 0, 0), (255, 255, 255)
                    else:
                        black_plus, white_plus = (0, 0, 0), (255, 255, 255)
                    if rect_minus.collidepoint(event.pos):
                        white_minus, black_minus = (0, 0, 0), (255, 255, 255)
                    else:
                        black_minus, white_minus = (0, 0, 0), (255, 255, 255)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_back.collidepoint(event.pos):
                        flag_settings = False
                    if rect_first_name.collidepoint(event.pos):
                        change_background_image(self.BACKGROUND_IMAGE_1)
                        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))
                    if rect_second_name.collidepoint(event.pos):
                        change_background_image(self.BACKGROUND_IMAGE_2)
                        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))
                    if rect_thirst_name.collidepoint(event.pos):
                        change_background_image(self.BACKGROUND_IMAGE_3)
                        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))
                    if rect_fourth_name.collidepoint(event.pos):
                        change_background_image(self.BACKGROUND_IMAGE_4)
                        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))
                    if rect_plus.collidepoint(event.pos):
                        number = change_quantity_columns() + 1
                        if number >= 10:
                            number = 10
                            width_quantity_columns = int(self.WIDTH * (53 / 120))
                        else:
                            width_quantity_columns = int(self.WIDTH * (47 / 100))
                        change_quantity_columns(number)
                    if rect_minus.collidepoint(event.pos):
                        number = change_quantity_columns() - 1
                        if number == 1 or number == 0:
                            number = 1
                            width_quantity_columns = int(self.WIDTH * (19 / 40))
                        else:
                            width_quantity_columns = int(self.WIDTH * (47 / 100))
                        change_quantity_columns(number)

            pygame.draw.rect(self.SCREEN, self.BLACK, (int(self.WIDTH * (19 / 60)), self.HEIGHT // 48,
                                                       int(self.WIDTH * (23 / 60)), self.HEIGHT // 24),
                             border_radius=self.WIDTH // 30)
            render_inscription = self.FONT_INSCRIPTIONS_IN_SETTINGS.render('ФОН', True, self.WHITE)
            self.SCREEN.blit(render_inscription, (self.WIDTH // 3, self.HEIGHT // 48))

            pygame.draw.rect(self.SCREEN, black_first_name, rect_first_name, border_radius=self.WIDTH // 30)
            render_inscription = self.FONT_NAMES_BACKGROUND_IMAGES.render(
                'ЯСНЫЙ ГОРОД', True, white_first_name)
            self.SCREEN.blit(render_inscription, (self.WIDTH // 12, int(self.HEIGHT * (7 / 80))))

            pygame.draw.rect(self.SCREEN, black_second_name, rect_second_name, border_radius=self.WIDTH // 30)
            render_inscription = self.FONT_NAMES_BACKGROUND_IMAGES.render(
                'НОЧЬ В ЛЕСУ', True, white_second_name)
            self.SCREEN.blit(render_inscription, (int(self.WIDTH * (109 / 200)), int(self.HEIGHT * (7 / 80))))

            pygame.draw.rect(self.SCREEN, black_thirst_name, rect_thirst_name, border_radius=self.WIDTH // 30)
            render_inscription = self.FONT_NAMES_BACKGROUND_IMAGES.render(
                'ВОСХОД В ГОРОДЕ', True, white_thirst_name)
            self.SCREEN.blit(render_inscription, (int(self.WIDTH * (3 / 40)), int(self.HEIGHT * (41 / 240))))

            pygame.draw.rect(self.SCREEN, black_fourth_name, rect_fourth_name, border_radius=self.WIDTH // 30)
            render_inscription = self.FONT_NAMES_BACKGROUND_IMAGES.render(
                'КОСМОС', True, white_fourth_name)
            self.SCREEN.blit(render_inscription, (int(self.WIDTH * (71 / 120)), int(self.HEIGHT * (41 / 240))))

            pygame.draw.rect(self.SCREEN, black_back, rect_back, border_radius=int(self.WIDTH * (7 / 120)))
            render_back = self.FONT_BACK.render('НАЗАД', True, white_back)
            self.SCREEN.blit(render_back, (int(self.WIDTH * (7 / 10)), int(self.HEIGHT * (217 / 240))))

            pygame.draw.rect(self.SCREEN, self.BLACK, (self.WIDTH // 5, int(self.HEIGHT * (11 / 48)),
                                                       int(self.WIDTH * (3 / 5)), self.HEIGHT // 24),
                             border_radius=self.WIDTH // 30)
            render_inscription = self.FONT_INSCRIPTIONS_IN_SETTINGS.render('КОЛ-ВО СТРОК', True, self.WHITE)
            self.SCREEN.blit(render_inscription, (int(self.WIDTH * (9 / 40)), int(self.HEIGHT * (11 / 48))))

            pygame.draw.rect(self.SCREEN, self.BLACK, (int(self.WIDTH * (5 / 12)), int(self.HEIGHT * (7 / 24)),
                                                       self.WIDTH // 6, self.HEIGHT // 12),
                             border_radius=int(self.WIDTH * (7 / 120)))
            render_inscription = self.FONT_QUANTITY_COLUMNS.render(f'{change_quantity_columns()}', True, self.WHITE)
            self.SCREEN.blit(render_inscription, (width_quantity_columns, int(self.HEIGHT * (23 / 80))))

            pygame.draw.rect(self.SCREEN, black_plus, rect_plus, border_radius=int(self.WIDTH * (7 / 120)))
            render_inscription = self.FONT_PLUS_AND_MINUS.render('+', True, white_plus)
            self.SCREEN.blit(render_inscription, (int(self.WIDTH * (2 / 3)), int(self.HEIGHT * (131 / 600))))

            pygame.draw.rect(self.SCREEN, black_minus, rect_minus, border_radius=int(self.WIDTH * (7 / 120)))
            render_inscription = self.FONT_PLUS_AND_MINUS.render('-', True, white_minus)
            self.SCREEN.blit(render_inscription, (int(self.WIDTH * (9 / 40)), int(self.HEIGHT * (11 / 48))))

            pygame.display.update()
            self.CLOCK.tick(self.FPS)

        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))

    def display_end_inscription(self, inscription, score, width, game_session_time):
        if score > self.CONN.cursor().execute(f'SELECT high_score FROM HighScoreAndTime').fetchone()[0]:
            self.CONN.cursor().execute(f'UPDATE HighScoreAndTime SET high_score = {score}')
            self.CONN.cursor().execute(f'UPDATE HighScoreAndTime SET game_session_time = "{game_session_time}"')
            self.CONN.commit()

        self.BALL_SPEED = 0

        self.SCREEN.blit(pygame.image.load(change_background_image()), (0, 0))

        start_sound = pygame.mixer.Sound(self.START_SOUND)

        rect_restart = pygame.Rect(int(self.WIDTH * (41 / 60)), int(self.HEIGHT * (109 / 120)),
                                   int(self.WIDTH * (17 / 60)), int(self.HEIGHT * (3 / 40)))
        rect_menu = pygame.Rect(self.WIDTH // 30, int(self.HEIGHT * (109 / 120)),
                                int(self.WIDTH * (17 / 60)), int(self.HEIGHT * (3 / 40)))

        black_restart, white_restart = (0, 0, 0), (255, 255, 255)
        black_exit_menu, white_exit_menu = (0, 0, 0), (255, 255, 255)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    if rect_restart.collidepoint(event.pos):
                        white_restart, black_restart = (0, 0, 0), (255, 255, 255)
                    else:
                        black_restart, white_restart = (0, 0, 0), (255, 255, 255)
                    if rect_menu.collidepoint(event.pos):
                        white_exit_menu, black_exit_menu = (0, 0, 0), (255, 255, 255)
                    else:
                        black_exit_menu, white_exit_menu = (0, 0, 0), (255, 255, 255)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_restart.collidepoint(event.pos):
                        pygame.mixer.music.stop()
                        start_sound.play()
                        pygame.time.wait(1000)
                        App(False).run()
                    if rect_menu.collidepoint(event.pos):
                        pygame.mixer.music.stop()
                        start_sound.play()
                        pygame.time.wait(1000)
                        App(True).run()

            pygame.draw.rect(self.SCREEN, self.BLACK, (self.WIDTH // 12, self.HEIGHT // 3,
                                                       int(self.WIDTH * (5 / 6)), self.HEIGHT // 4),
                             border_radius=self.WIDTH // 6)

            render_inscription = self.FONT_END_INSCRIPTION.render(inscription, True, self.WHITE)
            self.SCREEN.blit(render_inscription, (int(width), self.HEIGHT // 3))

            render_score = self.FONT_VALUES_END_INSCRIPTION.render(f'СЧЕТ: {score}', True, self.WHITE)
            self.SCREEN.blit(render_score, (int(width), int(self.HEIGHT * (17 / 40))))

            render_time = self.FONT_VALUES_END_INSCRIPTION.render(f'ВРЕМЯ: {game_session_time}', True, self.WHITE)
            self.SCREEN.blit(render_time, (int(width), int(self.HEIGHT * (59 / 120))))

            pygame.draw.rect(self.SCREEN, black_restart, rect_restart, border_radius=int(self.WIDTH * (7 / 120)))
            render_restart_inscription = self.FONT_RESTART_INSCRIPTION.render('ЕЩЕ РАЗ', True, white_restart)
            self.SCREEN.blit(render_restart_inscription, (int(self.WIDTH * (7 / 10)), int(self.HEIGHT * (221 / 240))))

            pygame.draw.rect(self.SCREEN, black_exit_menu, rect_menu, border_radius=int(self.WIDTH * (7 / 120)))
            render_menu_inscription = self.FONT_EXIT_MENU.render('МЕНЮ', True, white_exit_menu)
            self.SCREEN.blit(render_menu_inscription, (int(self.WIDTH * (7 / 120)), int(self.HEIGHT * (217 / 240))))

            pygame.display.update()
            self.CLOCK.tick(self.FPS)


def change_background_image(*arg):
    if arg:
        list_background_images.append(*arg)
        list_background_images.remove(list_background_images[0])
        return list_background_images[0]
    return list_background_images[0]


root = tkinter.Tk()
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

if (screen_width, screen_height) == (1440, 900) or (screen_width, screen_height) == (1366, 768) or \
        (screen_width, screen_height) == (1280, 720) or (screen_width, screen_height) == (1280, 800):
    first_background_image = resource_path('images/background_4_1.jpg')
elif (screen_width, screen_height) == (1600, 900) or (screen_width, screen_height) == (1536, 864):
    first_background_image = resource_path('images/background_4_2.jpg')
elif (screen_width, screen_height) == (1920, 1080):
    first_background_image = resource_path('images/background_4_3.jpg')
else:
    first_background_image = resource_path('images/background_4_4.jpg')
list_background_images = [first_background_image]


def change_quantity_columns(*arg):
    if arg:
        list_quantity_columns.append(*arg)
        list_quantity_columns.remove(list_quantity_columns[0])
        return list_quantity_columns[0]
    return list_quantity_columns[0]


list_quantity_columns = [7]

if __name__ == '__main__':
    app = App(True)
    app.run()
