#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import random
import re
import sys
import io

TOKENIZE = "tokenize"
PROBABILITIES = "probabilities"
GENERATE = "generate"
TEST = "test"
TOK_EX = r'[A-Za-zА-яа-я]+|[0-9]+|[ -\\]'
PRO_EX = r'[A-Za-zА-яа-я]+'
GEN_EX = r'[A-Za-zА-яа-я]+|[0-9]+|[\S]'

token_counter = {}
chains = {}
f_chains = {}
blocks = []


def set_parser(parser_):
    parser_.add_argument("command", choices=[TOKENIZE, PROBABILITIES, GENERATE, TEST])
    parser_.add_argument("--depth", type=int, default=0)
    parser_.add_argument("--size", type=int, default=0)


def tokenize(line_, pattern=TOK_EX):
    return re.findall(pattern, line_)


def probabilities(file, depth, pattern=PRO_EX):
    for line in file:
        block = tokenize(line.strip(), pattern)
        for w in block:
            token_counter[w] = token_counter.get(w, 0) + 1
        blocks.append(block)
        for chain_size in range(1, depth + 1):
            for idx in range(0, len(block) - chain_size):
                chain = tuple(block[idx: idx + chain_size])
                if chain not in chains:
                    chains[chain] = {}
                chains[chain][block[idx + chain_size]] = chains[chain].get(block[idx + chain_size], 0) + 1


def printProbabilities():
    print()
    s = sum(token_counter.values())

    for k, v in sorted(token_counter.items()):
        print("  {}: {:.2f}".format(k, v / s))

    for token, chain in sorted(chains.items()):
        print(' '.join(w for w in token))
        s = sum(chain.values())
        for k, v in sorted(chain.items()):
            print("  {}: {:.2f}".format(k, v / s))


def get_random_start():
    v = chains.values()
    l = len(v)
    ri = random.randint(0, l - 1)
    while True:
        if chains.values()[ri][0].istitle():
            return chains.values()[ri]
        ri = (ri + 1) % l


def get_random_token(d):
    limit = random.randint(0, sum(d.values()))
    index = 0
    for token, freq in d.items():
        index += freq
        if index >= limit:
            return token


def start_token(result_str, depth, res_len):
    result_str.append("\n")
    for s in get_random_start():
        result_str.append(s)
        res_len += len(s)


def generate(depth, size):
    if len(chains) == 0:
        return "Пустой файл",

    result_str = []
    res_len = 0
    start_token(result_str, depth, res_len)

    while res_len < size:
        try:
            t = tuple(result_str[-depth:])
            new_line = get_random_token(chains[t])
        except KeyError:
            if res_len > size:
                break
            start_token(result_str, depth, res_len)
        else:
            result_str.append(new_line)
            res_len += len(new_line)
    return result_str


def main(com_line_args):
    filename = "input.txt"
    if len(com_line_args) > 1:
        filename = com_line_args[1]

    parser = argparse.ArgumentParser()
    set_parser(parser)

    with io.open(filename, 'r', encoding='utf8') as f:
        args = parser.parse_args(f.readline().strip().split(" "))

        if args.command == TOKENIZE:
            for line in f:
                for w in tokenize(line, TOK_EX):
                    print(w)

        elif args.command == PROBABILITIES:
            probabilities(f, args.depth, PRO_EX)
            printProbabilities()

        elif args.command == GENERATE:
            probabilities(f, args.depth, GEN_EX)
            text = generate(args.depth, args.size)
            for w in text:
                if not re.search(r'[\',.!?:\"/\\)]', w):
                    print(' ', end='')
                print(w, end='')

                # for i in range(0, len(text)):
                #     if re.search(, t):

        elif args.command == TEST:
            pass

        else:
            print("Incorrect file! Arguments not found.")


main(sys.argv)
