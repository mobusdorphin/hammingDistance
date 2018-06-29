#!/usr/bin/python3

import sys

def hammingDistance(originalDNA, newDNA):
  """Determines the hamming distance between the original DNA string and the new DNA string

  originalDNA (str): String containing the original DNA
  newDNA (str): String containing the new DNA

  return: Returns the number of differences found between the strings.  Returns -1 if strings are not the same length

  """
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
