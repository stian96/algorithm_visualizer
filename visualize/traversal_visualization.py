from datastructures.trees.binarytree import BinaryTree
import pygame
import sys

# Initialize pygame.
pygame.init()

# Create a window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Tree Traversal")

colors = {
    'green': (0, 150, 0),
    'red': (255, 255, 255),
    'black': (80, 80, 80),
    'gray': (240, 240, 240)
}


def draw_buttons(win, color, x_pos, y_pos, rec_width, rec_height, btn_text):
    # Draw button
    pygame.draw.rect(win, color, (x_pos, y_pos, rec_width, rec_height))

    # Add font.
    btn_font = pygame.font.Font(None, 24)
    text = btn_font.render(str(btn_text), True, colors.get('green'))

    # Add text in the center of the rectangle.
    rect = text.get_rect(center=(x_pos + rec_width // 2, y_pos + rec_height // 2))
    win.blit(text, rect)


def draw_tree(win, tree, node, x, y, z):
    # Draw the root.
    pygame.draw.circle(win, colors.get('green'), (x, y), 20)
    font = pygame.font.Font(None, 24)
    text = font.render(str(node.value), True, (255, 255, 255))
    text_rect = text.get_rect(center=(x, y))

    # Blit the text on the window.
    win.blit(text, text_rect)

    # Draw the children
    if node.left is not None:
        pygame.draw.line(win, colors.get('gray'), (x, y), (x - z, y + 80))
        draw_tree(win, tree, node.left, x - z, y + 80, z // 2)
    if node.right is not None:
        pygame.draw.line(win, colors.get('gray'), (x, y), (x + z, y + 80))
        draw_tree(win, tree, node.right, x + z, y + 80, z // 2)


def traverse_tree(win, tree, node, x, y, z, order):
    if order == "level":
        queue = [(node, x, y, z)]
        while queue:
            curr_node, curr_x, curr_y, curr_z = queue.pop(0)
            if curr_node is None:
                continue
            highlight_node(win, curr_x, curr_y, curr_node.value)
            if curr_node.left is not None:
                queue.append((curr_node.left, curr_x - curr_z, curr_y + 80, curr_z // 2))
            if curr_node.right is not None:
                queue.append((curr_node.right, curr_x + curr_z, curr_y + 80, curr_z // 2))
    else:
        if node is None:
            return

        if order == 'pre':
            highlight_node(win, x, y, node.value)
        traverse_tree(win, tree, node.left, x - z, y + 80, z // 2, order)

        if order == 'in':
            highlight_node(win, x, y, node.value)
        traverse_tree(win, tree, node.right, x + z, y + 80, z // 2, order)

        if order == 'post':
            highlight_node(win, x, y, node.value)


def highlight_node(win, x, y, value):
    pygame.draw.circle(win, (255, 0, 0), (x, y), 20)

    font = pygame.font.Font(None, 24)
    text = font.render(str(value), True, colors.get('red'))
    text_rect = text.get_rect(center=(x, y))

    win.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(600)


def handle_button_hover(win, x_pos, y_pos, rec_width, rec_height, btn_text):
    mouse = pygame.mouse.get_pos()
    if button_hover(mouse[0], mouse[1], x_pos, y_pos, rec_width, rec_height):
        color = colors.get('red')
        hover = True
    else:
        color = colors.get('gray')
        hover = False
    draw_buttons(win, color, x_pos, y_pos, rec_width, rec_height, btn_text)
    return hover


def button_hover(mose_x, mouse_y, x, y, rec_width, rec_height):
    if x < mose_x < x + rec_width and y < mouse_y < y + rec_height:
        return True
    else:
        return False


def pick_traversal_method():
    w = 400
    h = 200

    if handle_button_hover(window, 130, 50, 100, 40, "Preorder"):
        traverse_tree(window, root, root.root, w, h, h, "pre")
    elif handle_button_hover(window, 280, 50, 100, 40, "Inorder"):
        traverse_tree(window, root, root.root, w, h, h, "in")
    elif handle_button_hover(window, 430, 50, 100, 40, "Postorder"):
        traverse_tree(window, root, root.root, w, h, h, "post")
    elif handle_button_hover(window, 580, 50, 100, 40, "Level-order"):
        traverse_tree(window, root, root.root, w, h, h, "level")


# Main code
root = BinaryTree()

# Insert children.
root.insert(10)
root.insert(8)
root.insert(15)
root.insert(14)
root.insert(2)
root.insert(9)
root.insert(22)
root.insert(15)
root.insert(1)
root.insert(7)

traversal_finished = False
clock = pygame.time.Clock()

while not traversal_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pick_traversal_method()

    # Draw tree
    window.fill((colors.get('black')))

    handle_button_hover(window, 130, 50, 100, 40, "Preorder")
    handle_button_hover(window, 280, 50, 100, 40, "Inorder")
    handle_button_hover(window, 430, 50, 100, 40, "Postorder")
    handle_button_hover(window, 580, 50, 100, 40, "Level-order")

    draw_tree(window, root, root.root, 400, 200, 200)
    pygame.display.update()

    clock.tick(60)

pygame.display.quit()
pygame.quit()