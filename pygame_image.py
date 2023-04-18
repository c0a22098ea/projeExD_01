import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    re_bg_img = pg.transform.flip(bg_img, True, False)
    re_re_bg_img = pg.transform.flip(re_bg_img, True, False)

    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img,  pg.transform.rotozoom(kk_img , 0, 1.0),  pg.transform.rotozoom(kk_img , 10, 1.0)]
    tmr = 0
    


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%3200

        screen.blit(bg_img ,[-x, 0] )
        screen.blit(re_bg_img, [1600-x, 0])
        screen.blit(bg_img ,[3200-x, 0] )
        
        if x%40 > 20:
            screen.blit(kk_imgs[1], [300, 200])
        else:
            screen.blit(kk_imgs[2], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()