import sys
import argparse

# print('출력1',sys.argv[0])
# print('출력2',sys.argv[1])
# print('출력3',sys.argv[2])

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='사용자의 이름')
parser.add_argument('--age', help='사용자의 나이')

args = parser.parse_args()
print(args.name, args.age)