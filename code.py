import pygame

# Define window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Create windows until the user closes them
running = True
while running:
    # Create a new Pygame window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user closes the window, stop the program
            running = False
    
    # Fill the window with a color
    window.fill((255, 255, 255))
    
    # Update the contents of the window
    pygame.display.flip()

# Quit Pygame
pygame.quit()
