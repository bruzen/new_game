import new_game.swi
import new_game.server


import sys
def main():
    port = int(sys.argv[1]) if len(sys.argv)>1 else 8080
    addr = ''
    new_game.swi.browser(port)
    new_game.swi.start(new_game.server.Server, port, addr=addr)

if __name__ == '__main__':
    main()
