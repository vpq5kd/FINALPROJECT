# this code is for the coins 

def coin_count():
    global camera, coins, score, score_display
    for coin in coins:
        if mariosprite.touches(coin):
            score += 1
            random_x = # choose a new location for the coin
            coin.x = random_x
        camera.draw(coin)