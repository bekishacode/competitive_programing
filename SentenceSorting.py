def sortSentence(self, s: str) -> str:
  shuffle = s.split(' ')
  final_sentence = ''
  for i in range(len(shuffle)):
    minimum_index = i
    for j in range(i +1, len(shuffle)):
      if shuffle[j][-1] < shuffle[minimum_index][-1]:
        minimum_index = j
    if i != minimum_index:
      shuffle[minimum_index], shuffle[i] = shuffle[i], shuffle[minimum_index]
    final_sentence += shuffle[i][: -1] + ' '
  return final_sentence[:-1]
