import pygame
import random
from collections import deque
import time
import math

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 900, 700
ROWS, COLS = 30, 30
GRID_SIZE = 500
CELL_SIZE = GRID_SIZE // COLS
GRID_OFFSET_X = (WIDTH - GRID_SIZE) // 2
GRID_OFFSET_Y = 80

# Modern Color Palette
COLORS = {
    'bg': (15, 15, 25),
    'surface': (25, 25, 40),
    'primary': (64, 224, 255),
    'success': (50, 255, 126),
    'danger': (255, 107, 107),
    'warning': (255, 193, 7),
    'text_primary': (15, 15, 25),
    'text_secondary': (200, 200, 220),
    'wall': (45, 45, 65),
    'path': (240, 240, 245),
    'solution': (64, 224, 255),
    'start': (50, 255, 126),
    'end': (255, 107, 107),
    'border': (70, 70, 90)
}

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Maze Generator & Solver")

# Clock and fonts
clock = pygame.time.Clock()
font_title = pygame.font.Font(None, 32)
font_button = pygame.font.Font(None, 24)
font_status = pygame.font.Font(None, 20)

# Grid creation
grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]  # 1 = wall, 0 = path
solution_path = []  # Store the solution path

def draw_rounded_rect(surface, color, rect, radius=8):
    """Draw rounded rectangle for modern UI"""
    x, y, w, h = rect
    if w < 2 * radius: radius = w // 2
    if h < 2 * radius: radius = h // 2
    
    pygame.draw.rect(surface, color, (x + radius, y, w - 2*radius, h))
    pygame.draw.rect(surface, color, (x, y + radius, w, h - 2*radius))
    pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + radius, y + h - radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + h - radius), radius)

def draw_glow_effect(surface, center, radius, color):
    """Draw subtle glow effect"""
    for i in range(3):
        alpha = 40 - i * 12
        if alpha > 0:
            glow_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*color[:3], alpha), (radius, radius), radius - i * 2)
            surface.blit(glow_surf, (center[0] - radius, center[1] - radius))

def draw_grid():
    """Enhanced grid drawing with modern styling"""
    # Grid background card
    grid_bg = pygame.Rect(GRID_OFFSET_X - 15, GRID_OFFSET_Y - 15, GRID_SIZE + 30, GRID_SIZE + 30)
    draw_rounded_rect(win, COLORS['surface'], grid_bg, 12)
    pygame.draw.rect(win, COLORS['border'], grid_bg, 2, 12)
    
    # Draw maze cells
    for row in range(ROWS):
        for col in range(COLS):
            x = GRID_OFFSET_X + col * CELL_SIZE
            y = GRID_OFFSET_Y + row * CELL_SIZE
            
            color = COLORS['path'] if grid[row][col] == 0 else COLORS['wall']
            pygame.draw.rect(win, color, (x, y, CELL_SIZE, CELL_SIZE))
            
            # Subtle grid lines
            if CELL_SIZE > 8:
                pygame.draw.rect(win, COLORS['border'], (x, y, CELL_SIZE, CELL_SIZE), 1)
    
    # Draw solution path if it exists
    for r, c in solution_path:
        x = GRID_OFFSET_X + c * CELL_SIZE
        y = GRID_OFFSET_Y + r * CELL_SIZE
        draw_glow_effect(win, (x + CELL_SIZE//2, y + CELL_SIZE//2), CELL_SIZE//2, COLORS['solution'])
        pygame.draw.rect(win, COLORS['solution'], (x, y, CELL_SIZE, CELL_SIZE))
    
    # Enhanced start and end points
    start_x = GRID_OFFSET_X + 1 * CELL_SIZE
    start_y = GRID_OFFSET_Y + 1 * CELL_SIZE
    end_x = GRID_OFFSET_X + (COLS-2) * CELL_SIZE
    end_y = GRID_OFFSET_Y + (ROWS-2) * CELL_SIZE
    
    # Start point with glow
    draw_glow_effect(win, (start_x + CELL_SIZE//2, start_y + CELL_SIZE//2), CELL_SIZE, COLORS['start'])
    pygame.draw.rect(win, COLORS['start'], (start_x, start_y, CELL_SIZE, CELL_SIZE))
    
    # End point with glow
    draw_glow_effect(win, (end_x + CELL_SIZE//2, end_y + CELL_SIZE//2), CELL_SIZE, COLORS['end'])
    pygame.draw.rect(win, COLORS['end'], (end_x, end_y, CELL_SIZE, CELL_SIZE))

def neighbors(r, c):
    dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    result = []
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            result.append((nr, nc))
    return result

def generate_maze():
    global solution_path
    # Reset grid
    for row in range(ROWS):
        for col in range(COLS):
            grid[row][col] = 1
    
    # Clear solution path
    solution_path = []
    
    # Initialize start and end points
    grid[1][1] = 0  # Start
    grid[ROWS-2][COLS-2] = 0  # End

    stack = [(1, 1)]
    while stack:
        r, c = stack[-1]
        unvisited = [(nr, nc) for nr, nc in neighbors(r, c) if grid[nr][nc] == 1]
        if unvisited:
            nr, nc = random.choice(unvisited)
            grid[(r + nr) // 2][(c + nc) // 2] = 0
            grid[nr][nc] = 0
            stack.append((nr, nc))
        else:
            stack.pop()
    
    print(f"Start cell (1,1): {grid[1][1]}")
    print(f"End cell ({ROWS-2},{COLS-2}): {grid[ROWS-2][COLS-2]}")

def solve_maze(start, end):
    global solution_path
    queue = deque([start])
    visited = {start: None}
    found = False

    while queue:
        current = queue.popleft()
        if current == end:
            found = True
            break
        r, c = current
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited[(nr, nc)] = current
                queue.append((nr, nc))

    if not found:
        print("No path found!")
        print(f"Visited {len(visited)} cells")
        return False

    # Build and store path
    solution_path = []
    cur = end
    while cur != start:
        solution_path.append(cur)
        cur = visited[cur]
    solution_path.append(start)
    solution_path.reverse()

    # Draw path during solving
    for r, c in solution_path:
        x = GRID_OFFSET_X + c * CELL_SIZE
        y = GRID_OFFSET_Y + r * CELL_SIZE
        draw_glow_effect(win, (x + CELL_SIZE//2, y + CELL_SIZE//2), CELL_SIZE//2, COLORS['solution'])
        pygame.draw.rect(win, COLORS['solution'], (x, y, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        pygame.time.delay(20)
    return True

def create_modern_button(text, x, y, width, height, color, text_color, hover_color=None):
    """Create stylish button with hover effects"""
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    is_hovering = button_rect.collidepoint(mouse_pos)
    
    current_color = hover_color if (hover_color and is_hovering) else color
    
    # Button shadow
    shadow_rect = pygame.Rect(x + 3, y + 3, width, height)
    draw_rounded_rect(win, (0, 0, 0, 80), shadow_rect, 8)
    
    # Main button
    draw_rounded_rect(win, current_color, button_rect, 8)
    
    # Hover glow
    if is_hovering:
        glow_rect = pygame.Rect(x - 2, y - 2, width + 4, height + 4)
        for i in range(3):
            alpha = 30 - i * 10
            glow_surf = pygame.Surface((width + 4 + i*2, height + 4 + i*2), pygame.SRCALPHA)
            draw_rounded_rect(glow_surf, (*current_color[:3], alpha), 
                            pygame.Rect(0, 0, width + 4 + i*2, height + 4 + i*2), 10)
            win.blit(glow_surf, (x - 2 - i, y - 2 - i))
        draw_rounded_rect(win, current_color, button_rect, 8)
    
    # Button text
    text_surf = font_button.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button_rect.center)
    win.blit(text_surf, text_rect)
    
    return button_rect

def draw_header():
    """Draw modern header with title"""
    # Main title
    title_surf = font_title.render("MODERN MAZE SOLVER", True, COLORS['text_secondary'])
    title_rect = title_surf.get_rect(center=(WIDTH//2, 35))
    
    # Title glow effect
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        glow_surf = font_title.render("MODERN MAZE SOLVER", True, COLORS['primary'])
        win.blit(glow_surf, (title_rect.x + dx, title_rect.y + dy))
    
    win.blit(title_surf, title_rect)
    
    # Accent line
    line_rect = pygame.Rect(WIDTH//2 - 100, 55, 200, 3)
    draw_rounded_rect(win, COLORS['primary'], line_rect, 2)

def draw_status_bar():
    """Draw status information bar"""
    status_rect = pygame.Rect(50, HEIGHT - 100, WIDTH - 100, 60)
    draw_rounded_rect(win, COLORS['surface'], status_rect, 10)
    pygame.draw.rect(win, COLORS['border'], status_rect, 1, 10)
    
    # Status text
    status_text = "Ready to generate and solve mazes"
    status_surf = font_status.render(status_text, True, COLORS['text_secondary'])
    status_text_rect = status_surf.get_rect(center=(WIDTH//2, HEIGHT - 80))
    win.blit(status_surf, status_text_rect)
    
    # Instructions
    instr_text = "Click buttons to generate new maze or solve current one"
    instr_surf = font_status.render(instr_text, True, COLORS['text_secondary'])
    instr_rect = instr_surf.get_rect(center=(WIDTH//2, HEIGHT - 60))
    win.blit(instr_surf, instr_rect)

def draw_buttons(solved):
    button_y = HEIGHT - 150
    button_height = 35
    
    if not solved:
        # Solve button
        solve_button = create_modern_button(
            "SOLVE MAZE", WIDTH//2 - 200, button_y, 120, button_height,
            COLORS['primary'], COLORS['text_primary'],
            tuple(min(255, c + 30) for c in COLORS['primary'])
        )
        
        # Generate button  
        generate_button = create_modern_button(
            "NEW MAZE", WIDTH//2 - 60, button_y, 120, button_height,
            COLORS['success'], COLORS['text_primary'],
            tuple(min(255, c + 30) for c in COLORS['success'])
        )
        
        # Quit button
        quit_button = create_modern_button(
            "QUIT", WIDTH//2 + 80, button_y, 120, button_height,
            COLORS['danger'], COLORS['text_primary'],
            tuple(min(255, c + 30) for c in COLORS['danger'])
        )
        
        return solve_button, quit_button, generate_button
    else:
        # Generate New button (wider when solved)
        generate_button = create_modern_button(
            "GENERATE NEW", WIDTH//2 - 130, button_y, 150, button_height,
            COLORS['warning'], COLORS['text_primary'],
            tuple(min(255, c + 30) for c in COLORS['warning'])
        )
        
        # Quit button
        quit_button = create_modern_button(
            "QUIT", WIDTH//2 + 30, button_y, 120, button_height,
            COLORS['danger'], COLORS['text_primary'],
            tuple(min(255, c + 30) for c in COLORS['danger'])
        )
        
        return None, quit_button, generate_button

def main():
    random.seed(time.time())  # Ensure different maze each run
    generate_maze()
    run = True
    solved = False

    while run:
        clock.tick(60)
        win.fill(COLORS['bg'])
        draw_header()
        draw_grid()
        draw_status_bar()

        # Always get all three buttons, but solve_button may be None if solved
        solve_button, quit_button, generate_button = draw_buttons(solved)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Only allow solving if not already solved and button exists
                if not solved and solve_button is not None and solve_button.collidepoint(pos):
                    success = solve_maze((1, 1), (ROWS-2, COLS-2))
                    if success:
                        solved = True
                        # Redraw the entire screen to show the solved maze
                        win.fill(COLORS['bg'])
                        draw_header()
                        draw_grid()
                        draw_status_bar()
                        draw_buttons(solved)
                        pygame.display.update()
                # Always allow quitting
                elif quit_button is not None and quit_button.collidepoint(pos):
                    run = False
                # Allow generating a new maze, resetting solved state
                elif generate_button is not None and generate_button.collidepoint(pos):
                    random.seed(time.time())
                    generate_maze()
                    solved = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()