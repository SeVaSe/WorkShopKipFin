# СЛЕЖЕНИЕ ЗА КУРСОРОМ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import pygame  # Импорт библиотеки Pygame
# import sys  # Импорт библиотеки sys
# import random  # Импорт библиотеки random
# import colorsys  # Импорт библиотеки colorsys
#
# # Инициализация Pygame
# pygame.init()
#
# # Размер окна
# WINDOW_WIDTH = 800  # Ширина окна
# WINDOW_HEIGHT = 600  # Высота окна
#
# # Цвета
# BACKGROUND_COLOR = (0, 0, 0)  # Цвет фона (черный)
# LINE_FADE_SPEED = 1  # Скорость затухания линий
# LINE_MOVE_SPEED = 2  # Скорость движения линий к курсору
# LINE_COLOR_CHANGE_SPEED = 0.5  # Скорость изменения цвета линий
#
# # Создание окна
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Создание окна Pygame заданного размера
# pygame.display.set_caption("Линии, следящие за курсором")  # Установка заголовка окна
#
# # Создание класса для линий
# class Line:
#     """КЛАСС СОЗДАНИЯ ЛИНИИ"""
#     def __init__(self, start, color):  # Конструктор класса Line
#         self.start = start  # Установка начальной позиции линии
#         self.end = start  # Установка конечной позиции линии (по умолчанию равна начальной)
#         self.color = color  # Установка цвета линии
#         self.alpha = 255  # Начальная прозрачность
#         self.width = 2  # Начальная ширина линии
#         self.pulsating = False  # Флаг, указывающий, имеет ли линия пульсацию
#
#     def move_towards(self, target):
#         """дживежение линии за курсором"""
#         dx = target[0] - self.end[0]  # Вычисление изменения по горизонтали до цели
#         dy = target[1] - self.end[1]  # Вычисление изменения по вертикали до цели
#         length = max(1, (dx ** 2 + dy ** 2) ** 0.5)  # Расчет длины вектора
#         dx /= length  # Нормализация изменения по горизонтали
#         dy /= length  # Нормализация изменения по вертикали
#         self.end = (self.end[0] + dx * LINE_MOVE_SPEED, self.end[1] + dy * LINE_MOVE_SPEED)  # Движение линии к цели
#         self.alpha -= LINE_FADE_SPEED  # Уменьшение прозрачности
#         if self.pulsating:  # Если линия имеет пульсацию
#             self.width = random.randint(1, 10)  # Изменение ширины линии случайным образом
#
#     def is_faded(self):
#         return self.alpha <= 0  # Проверка, затухла ли линия
#
# # Создание списка линий
# lines = []
#
# # Главный цикл программы
# running = True  # Флаг для выполнения цикла
# pulsate_counter = 0  # Счетчик для пульсации линий
# pulsate_duration = 30  # Интервал пульсации линий
# hue = 0.0  # Начальное значение цвета (Hue)
# hue_speed = 0.001  # Скорость изменения цвета
#
# while running:  # Основной игровой цикл
#     for event in pygame.event.get():  # Обработка событий Pygame, включая закрытие окна
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Заливка фона
#     window.fill(BACKGROUND_COLOR)  # Заполнение окна черным цветом
#
#     # Получение текущей позиции курсора
#     cursor_x, cursor_y = pygame.mouse.get_pos()
#
#     # Удаление линий, которые достигли конца затухания
#     lines = [line for line in lines if not line.is_faded()]
#
#     # Создание новой линии
#     hue += hue_speed  # Изменение цвета линии
#     line_color = tuple(int(255 * x) for x in colorsys.hsv_to_rgb(hue % 1, 1, 1))  # Преобразование цвета в RGB
#     new_line = Line((cursor_x, cursor_y), line_color)  # Создание новой линии
#
#     # Добавление пульсации к каждой десятой линии
#     pulsate_counter += 1
#     if pulsate_counter == pulsate_duration:
#         new_line.pulsating = True  # Включение пульсации для новой линии
#         pulsate_counter = 0
#
#     lines.append(new_line)  # Добавление новой линии в список
#
#     # Обновление и движение линий
#     for line in lines:
#         line.move_towards((cursor_x, cursor_y))  # Движение линии к текущей позиции курсора
#
#     # Отрисовка и обновление линий
#     for line in lines:
#         pygame.draw.line(window, line.color, line.start, line.end, line.width)  # Отрисовка линии
#
#     # Обновление экрана
#     pygame.display.update()  # Обновление отображаемого содержимого
#
# # Завершение Pygame
# pygame.quit()
# sys.exit()



# ИГРА В ЖИЗНЬ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import pygame
# import sys
# import random
#
# # Инициализация Pygame
# pygame.init()
#
# # Размер окна и размер клеток
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# CELL_SIZE = 5
#
# # Цвета
# BACKGROUND_COLOR = (0, 0, 0)
# CELL_COLOR = (255, 255, 255)
#
# # Размер сетки (количество клеток по горизонтали и вертикали)
# GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
# GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE
#
# # Создание окна
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Игра 'Жизнь'")
#
# # Инициализация начального состояния игровой сетки случайными значениями
# grid = [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#
# # Функция для определения следующего состояния клеток
# def update_grid():
#     new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#     for y in range(GRID_HEIGHT):
#         for x in range(GRID_WIDTH):
#             neighbors = [
#                 grid[(y - 1) % GRID_HEIGHT][(x - 1) % GRID_WIDTH],
#                 grid[(y - 1) % GRID_HEIGHT][x],
#                 grid[(y - 1) % GRID_HEIGHT][(x + 1) % GRID_WIDTH],
#                 grid[y][(x - 1) % GRID_WIDTH],
#                 grid[y][(x + 1) % GRID_WIDTH],
#                 grid[(y + 1) % GRID_HEIGHT][(x - 1) % GRID_WIDTH],
#                 grid[(y + 1) % GRID_HEIGHT][x],
#                 grid[(y + 1) % GRID_HEIGHT][(x + 1) % GRID_WIDTH],
#             ]
#             live_neighbors = sum(neighbors)
#             if grid[y][x] == 1:
#                 if live_neighbors < 2 or live_neighbors > 3:
#                     new_grid[y][x] = 0
#                 else:
#                     new_grid[y][x] = 1
#             else:
#                 if live_neighbors == 3:
#                     new_grid[y][x] = 1
#     return new_grid
#
# # Главный цикл программы
# running = True
# paused = False
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 paused = not paused
#
#     if not paused:
#         grid = update_grid()
#
#     # Очистка экрана
#     window.fill(BACKGROUND_COLOR)
#
#     # Отрисовка клеток
#     for y in range(GRID_HEIGHT):
#         for x in range(GRID_WIDTH):
#             if grid[y][x] == 1:
#                 pygame.draw.rect(window, CELL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
#
#     # Обновление экрана
#     pygame.display.update()
#
# # Завершение Pygame
# pygame.quit()
# sys.exit()


# СНЕГ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import pygame
# import sys
# import random
#
# # Инициализация Pygame
# pygame.init()
#
# # Размер окна
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
#
# # Цвета
# BACKGROUND_COLOR = (0, 0, 0)
# SNOW_COLOR = (255, 255, 255)
#
# # Количество снежинок
# NUM_SNOWFLAKES = 200
#
# # Создание окна
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Симуляция снега")
#
# # Класс для снежинки
# class Snowflake:
#     def __init__(self):
#         self.x = random.randint(0, WINDOW_WIDTH)
#         self.y = random.randint(0, WINDOW_HEIGHT)
#         self.size = random.randint(1, 5)
#         self.speed = random.uniform(0.1, 2.0)
#
#     def move(self):
#         self.y += self.speed
#         if self.y > WINDOW_HEIGHT:
#             self.y = 0
#             self.x = random.randint(0, WINDOW_WIDTH)
#
# # Создание списка для хранения снежинок
# snowflakes = [Snowflake() for _ in range(NUM_SNOWFLAKES)]
#
# # Главный цикл программы
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Очистка экрана
#     window.fill(BACKGROUND_COLOR)
#
#     # Рисование снежинок
#     for flake in snowflakes:
#         pygame.draw.circle(window, SNOW_COLOR, (flake.x, flake.y), flake.size)
#         flake.move()
#
#     # Обновление экрана
#     pygame.display.flip()
#
#     # Задержка на 0.02 секунды для улучшения производительности
#     pygame.time.delay(15)
#
# # Завершение Pygame
# pygame.quit()
# sys.exit()




# ПАПОРОТНИК БАРНСЛИ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import pygame
# import random
#
# # Инициализация Pygame
# pygame.init()
#
# # Параметры экрана
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Папоротник Барнсли")
#
# # Параметры папоротника
# x, y = 0, 0  # Начальные координаты
# scale = 60
# iterations = 5000
#
# # Правила для папоротника Барнсли
# def barnsley_fern(x, y):
#     r = random.random()
#     if r <= 0.01:
#         x1, y1 = 0, 0.16 * y
#     elif r <= 0.86:
#         x1, y1 = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
#     elif r <= 0.93:
#         x1, y1 = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
#     else:
#         x1, y1 = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
#     return x1, y1
#
# # Функция для отрисовки папоротника
# def draw_fern(surface, x, y, scale, iterations):
#     fern_color = (34, 139, 34)
#     for _ in range(iterations):
#         x, y = barnsley_fern(x, y)
#         pygame.draw.circle(surface, fern_color, (int(width / 2 + x * scale), int(height - y * scale)), 1)
#
# # Основной цикл
# running = True
# clock = pygame.time.Clock()  # Создаем объект Clock для управления частотой кадров
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0, 0, 0))  # Очистка экрана
#
#     # Обновление параметров на основе ввода
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         scale += 1
#     elif keys[pygame.K_DOWN] and scale > 1:
#         scale -= 1
#     elif keys[pygame.K_SPACE]:
#         iterations = 5000
#     elif keys[pygame.K_RETURN]:
#         iterations = 50000
#     if keys[pygame.K_LEFT]:
#         x -= 10
#     elif keys[pygame.K_RIGHT]:
#         x += 10
#
#     # Отрисовка папоротника с текущими параметрами
#     draw_fern(screen, x, y, scale, iterations)
#
#     pygame.display.flip()
#     clock.tick(30)  # Ограничение частоты кадров до 30 кадров в секунду
#
# # Завершение Pygame
# pygame.quit()



# TKINTER-упрощенные заметки !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import tkinter as tk
# from tkinter import messagebox
#
# # Создаем главное окно
# root = tk.Tk()
# root.title("Заметки")
#
# # Список для хранения заметок
# notes = []
#
# # Функция для добавления новой заметки
# def add_note():
#     note = entry.get()
#     if note:
#         notes.append(note)
#         listbox.insert(tk.END, note)
#         entry.delete(0, tk.END)
#
# # Функция для удаления выбранной заметки
# def delete_note():
#     selected_index = listbox.curselection()
#     if selected_index:
#         index = selected_index[0]
#         listbox.delete(index)
#         notes.pop(index)
#
# # Функция для редактирования выбранной заметки
# def edit_note():
#     selected_index = listbox.curselection()
#     if selected_index:
#         index = selected_index[0]
#         edited_note = entry.get()
#         if edited_note:
#             listbox.delete(index)
#             listbox.insert(index, edited_note)
#             notes[index] = edited_note
#             entry.delete(0, tk.END)
#
# # Создаем и размещаем виджеты на главном окне
# entry = tk.Entry(root, width=40)
# entry.pack(pady=10)
#
# add_button = tk.Button(root, text="Добавить заметку", command=add_note)
# add_button.pack()
#
# edit_button = tk.Button(root, text="Редактировать заметку", command=edit_note)
# edit_button.pack()
#
# delete_button = tk.Button(root, text="Удалить заметку", command=delete_note)
# delete_button.pack()
#
# listbox = tk.Listbox(root, width=40)
# listbox.pack()
#
# # Запускаем цикл обработки событий
# root.mainloop()



# TKINTER-сложные заметки !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import tkinter as tk
# from tkinter import messagebox
# import os
# import time
#
# # Создаем главное окно
# root = tk.Tk()
# root.title("Заметки")
#
# # Список для хранения заметок
# notes = []
#
# # Функция для добавления новой заметки
# def add_note():
#     nowTime = time.strftime("%H:%M:%S")
#     note = entry.get()
#     if note:
#         notes.append(note)
#         listbox.insert(tk.END, f'{nowTime}: {note}')
#         entry.delete(0, tk.END)
#
# # Функция для удаления выбранной заметки
# def delete_note():
#     selected_index = listbox.curselection()
#     if selected_index:
#         index = selected_index[0]
#         listbox.delete(index)
#         notes.pop(index)
#
# # Функция для редактирования выбранной заметки
# def edit_note():
#     nowTime = time.strftime("%H:%M:%S")
#     selected_index = listbox.curselection()
#     if selected_index:
#         index = selected_index[0]
#         edited_note = entry.get()
#         if edited_note:
#             notes[index] = edited_note
#             listbox.delete(index)
#             listbox.insert(index, f'{nowTime}: {edited_note}')
#             entry.delete(0, tk.END)
#
# # Функция для сохранения заметок в файл
# def save_notes():
#     nowTime = time.strftime("%H:%M:%S")
#     with open("notes.txt", "w", encoding='utf-8') as file:
#         for note in notes:
#             file.write(f'{nowTime}: {note} \n')
#
# # Функция для загрузки заметок из файла
# def load_notes():
#     if os.path.exists("notes.txt"):
#         with open("notes.txt", "r", encoding='utf-8') as file:
#             for line in file:
#                 note = line.strip()
#                 notes.append(note)
#                 listbox.insert(tk.END, note)
#
# # Создаем и размещаем виджеты на главном окне
# entry = tk.Entry(root, width=40)
# entry.pack(pady=10)
#
# add_button = tk.Button(root, text="Добавить заметку", command=add_note)
# add_button.pack()
#
# edit_button = tk.Button(root, text="Редактировать заметку", command=edit_note)
# edit_button.pack()
#
# delete_button = tk.Button(root, text="Удалить заметку", command=delete_note)
# delete_button.pack()
#
# listbox = tk.Listbox(root, width=40)
# listbox.pack()
#
# save_button = tk.Button(root, text="Сохранить заметки", command=save_notes)
# save_button.pack()
#
# load_button = tk.Button(root, text="Загрузить заметки", command=load_notes)
# load_button.pack()
#
# # Загружаем заметки при запуске приложения
# load_notes()
#
# # Запускаем цикл обработки событий
# root.mainloop()
