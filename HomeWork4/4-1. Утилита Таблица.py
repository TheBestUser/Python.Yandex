import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="subparserName")

head_parser = subparser.add_parser("head")
tail_parser = subparser.add_parser("tail")
cut_parser = subparser.add_parser("cut")
paste_parser = subparser.add_parser("paste")
head_parser.add_argument("-n", action="store", nargs=2, default=0)
tail_parser.add_argument("-n", action="store", nargs=2, default=0)
cut_parser.add_argument("-f", action="store", nargs="?", default=0)
paste_parser.add_argument("-n", action="store", nargs=2, default=0)

resh = parser.parse_args("head -n 2 test.tsv".split())
# resn = parser.parse_args("tail -n 2 test.tsv".split())
# resc = parser.parse_args("cut -f 1,1,3,2 test.tsv".split())
# resp = parser.parse_args("paste test1.tsv test2.tsv".split())

if resh.subparserName == "head":
    print("head " + resh.n[0] + resh.n[1])
