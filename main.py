from game import Game


if __name__ == '__main__':
    game = Game()
    # extra frames are played for example in 10th if its a strike and after 10th frame 
    game.run()
    game.log_to_console()