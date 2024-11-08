import pygame
import src.my_screen
import src.scenes

def main():
	screen_size = (800, 600)
	screen = src.my_screen.init(screen_size)
	running = True
	objects, root = src.scenes.scene_one(screen_size, 7)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill("black")

		mouse_pos = src.my_screen.update_mouse_pos()
		src.my_screen.render(screen, objects, root, mouse_pos)

		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
