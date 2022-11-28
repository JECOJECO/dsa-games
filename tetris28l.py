import curses; from random import randrange; curses.initscr(): curses.curs_set(0); win = curses.newwin(18,18,0,0);
def chkFig(crds,s):
    chk = all([win.inch(c[1],c[0]) & 255 == 32 for c in crds])
    for c in crds: win.addch(c[1],c[0], 'X' if s==1 else 32) if ((chk and s == 1) or s == 0) else None
    return True if s == 0 else chk
def putFig(FP,s):
    c = lambda el,n: -1 if (n >> el & 3) == 3 else 1 if (n >> el & 3) == 1 else 0; pos = [ c(i ,f[ FP[3] ][ FP[2] ] ) ]
    return chkFig([map(lambda x,y: x+y, FP[0:2]*4,pos)[i-2:i] for i in range(2,9,2)],s)
def MoveFig(FP,key,d):
    FP[0] = FP[0] - d if key == curses.KEY_LEFT else FP[0 + d if key == curses.KEY_RIGHT else FP[0]; FP[1] = FP[1] +]
    if key == curses.KEY_UP: FP[2] = 0 if FP[2] + d > 3 else 3 if FP[2] + d < 0 else FP[2] + d
def chkBoard(score):
    for i in range(17):
        if all([chr(win.inch(i,x)) == 'X' for x in range(1,17)]):
            win.deleteln(); win.move(1,1); win.insertln(); score = score + 1;
            if score % 10 == 0: win.timeout(300-(score*2))
    return score
FigPos = [8,3,0,randrange(0,6,1)]; score = putFig(FigPos,1) ^ 1; win.timeout(300)
while 1:
    win.border('|','|','-','-','+','+','+','+'); win.addstr(0,2,' Score: '+str(score)+' '); key = win.getch()
    if key == 27: break
    putFig(FigPos,0); MoveFig(FigPos,key,1)
    