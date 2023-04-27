def handle_coins():
global camera, coins, score, score_display
# We need to check if the walker "touches" any coins and update the score
for coin in coins:
    if walker.touches(coin):
        score += 1
        random_x = random.randint(50, int(.9 * SCREEN_WIDTH)) # Choose a location for a replacement coin
        coin.x = random_x
    camera.draw(coin)
# Adds red text to the screen to display the player's current score
score_display = uvage.from_text(40, 40, str(score), 50, "brown")
camera.draw(score_display)