#!/usr/bin/python3

import sys

def hammingDistance(originalDNA, newDNA):
  if (len(originalDNA) != len(newDNA)):
    return -1

  originalDNAList = list(originalDNA)
  newDNAList = list(newDNA)

  matchCount = 0
  for i in range(len(originalDNA)):
    if (originalDNAList[i] != newDNAList[i]):
      matchCount += 1
  
  return matchCount

if __name__ == "__main__":
  if (len(sys.argv) != 3):
    print("Usage:  {} originalDNA newDNA".format(sys.argv[0]))
    exit()
  print(hammingDistance(sys.argv[1], sys.argv[2]))
