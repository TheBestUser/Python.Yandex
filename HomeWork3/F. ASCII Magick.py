import argparse


def configParser(parser):
    parser.add_argument("command", choices=["crop", "expose", "rotate"])
    parser.add_argument("-l", "--left", type=int, default=0)
    parser.add_argument("-r", "--right", type=int, default=0)
    parser.add_argument("-t", "--top", type=int, default=0)
    parser.add_argument("-b", "--bottom", type=int, default=0)
    parser.add_argument('p', nargs='?', type=int, default=0)


def getImage(f):
    image = []
    for line in f:
        image.append(line.replace('\n', ''))
    return image


def changeImage(image, args):
    res_str = str()
    if args.command == "crop":
        l, r, t, b = args.left, args.right, args.top, args.bottom
        for i in range(t, len(image) - b):
            res_str += image[i][l:-r] + "\n"
    elif args.command == "expose":
        colors = tuple('@%#*+=-:. ')
        for line in image:
            for char in line:
                ind = colors.index(char) + args.p
                if ind < 0:
                    ind = 0
                elif ind >= len(colors):
                    ind = len(colors)-1
                res_str += colors[ind]
            res_str += "\n"
    elif args.command == "rotate":
        old_im = image
        for _ in range(int(args.p % 360 / 90)):
            new_im = []
            for i in range(len(old_im[0])):
                new_im.append(str())
                for j in range(len(old_im)):
                    c = old_im[j][-i - 1]
                    new_im[i] += c
            old_im = new_im
        for line in old_im:
            res_str += line + '\n'
    return res_str[:-1]


def main():
    parser = argparse.ArgumentParser()
    configParser(parser)

    f = open("input.txt")
    args = parser.parse_args(f.readline().split())
    image = getImage(f)
    print(changeImage(image, args))


main()
