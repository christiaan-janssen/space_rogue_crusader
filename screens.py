import pygame


class Screen:
	def __init__(self, screen) -> None:
		self.screen = screen

	def render(self) -> None:
		pass

	def handle_input(self) -> bool:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
		return True


class MenuScreen(Screen):
	def __init__(self, screen, font) -> None:
		super().__init__(screen)
		self.font = font

	def render(self) -> None:
		self.screen.fill("red")
		self.font.render_to(self.screen, (40, 50), "Hello World", (0,0,0))

	def handle_input(self) -> bool:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return False


		return True

