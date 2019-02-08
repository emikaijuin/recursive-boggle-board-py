from random import *

dice = [
  "AAEEGN",
  "ELRTTY",
  "AOOTTW",
  "ABBJOO",
  "EHRTVW",
  "CIMOTU",
  "DISTTY",
  "EIOSST",
  "DELRVY",
  "ACHOPS",
  "HIMNQU",
  "EEINSU",
  "EEGHNW",
  "AFFKPS",
  "HLNNRZ",
  "DEILRX"
]

board = []

def shake():
  global board
  board = [dice[randint(0,5)] for dice in sample(dice,16)]

def print_board(board):
  rows = [board[i*4:i*4+4] for i in range(4)]
  for row in rows:
    print("  ".join(row))

def check(word):
  word = word.upper()
  if word[0] in board:
    for position in find_letter_positions(word[0]):
      return find_next_letter(word, 0, position)
  else:
    return False

def find_letter_positions(letter):
  return [i for i, val in enumerate(board) if val == letter]

def find_next_letter(word, word_index, board_index):
  if word_index == len(word)-1:
    return True
  
  if word[word_index + 1] in adjacent_letters(board_index):
    for next_board_index in adjacent_indices(board_index):
      if board[next_board_index] == word[word_index + 1]:
        if find_next_letter(word, word_index + 1, next_board_index):
          return True

  else:
    return False

def adjacent_letters(board_index):
  return list(map(lambda x: board[x], adjacent_indices(board_index)))

def adjacent_indices(index):
  return {
    0: [1,4,5],
    1: [0,2,4,5,6],
    2: [1,3,5,6,7],
    3: [2,6,7],
    4: [0,1,5,8,9],
    5: [0,1,2,4,6,8,9,10],
    6: [1,2,3,5,7,9,10,11],
    7: [2,3,6,10,11],
    8: [4,5,9,12,13],
    9: [4,5,6,8,10,12,13,14],
    10: [5,6,7,9,11,13,14,15],
    11: [6,7,10,14,15],
    12: [8,9,13],
    13: [8,9,10,12,14],
    14: [9,10,11,13,15],
    15: [10,11,14]
  }[index]

# Driver Code
shake()
while True:
  print_board(board)
  word = input("Guess word. \n")
  if check(word):
    print("You got it! \n")
  else:
    print("Nope :( \n")
