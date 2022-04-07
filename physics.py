
def check_scenario_collision(p1, bg_margins): # checks if player has collided with background elements
    pass

def check_enemy_collision(p1, enemy_list): # checks if player has collides with an enemy
    player_mask = p1.get_mask()
    for enemy in enemy_list:
        enemy_mask = enemy.get_mask()
        distance = (enemy.x_pos - p1.x_pos, enemy.y_pos-p1.y_pos)
        collision = player_mask.overlap(enemy_mask, distance)
        if collision:
            return True
    return False

def check_bullet_kill(p1, enemy_list): # checks if any bullet has reached an enemy
    for enemy in enemy_list:
        for bullet in p1.bullet_list:
            if (bullet.y_pos - enemy.y_pos < enemy.height and enemy.y_pos - bullet.y_pos < bullet.height) and (bullet.x_pos - enemy.x_pos < enemy.width and enemy.x_pos - bullet.x_pos < bullet.width):
                enemy_list.remove(enemy)
                p1.bullet_list.remove(bullet)
                break

