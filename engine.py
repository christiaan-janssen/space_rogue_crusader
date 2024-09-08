
import pygame
import pygame.freetype

from screens import MenuScreen

class Engine:
	def __init__(self) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((1200,720))
		self.font = pygame.freetype.Font("Game Of Squids.ttf", 24)
		self.clock = pygame.time.Clock()
		self.dt = 0
		self.running = True
		self.game_screen = MenuScreen(self.screen, self.font)

	def run(self) -> None:
		while self.running:
			self.running = self.game_screen.handle_input()
			self.game_screen.render()


			pygame.display.flip()

			self.dt = self.clock.tick(60) / 1000

		self.stop()

	def stop(self) -> None:
		pygame.quit()
