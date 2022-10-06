if __name__ =='__main__':
    egg = 28

    box = egg // 6

    rem = egg % 6

    last_box = 6 - rem

    if rem == 0:
        print(f'%d boxes are needed' % box)
    else:
        print(f'%d eggs are needed to fill the box' % last_box)
        print(f'%d eggs are placed in the last uncompleted box' % rem)

