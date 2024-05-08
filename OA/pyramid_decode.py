def decode(message_file):

    with open(message_file, 'r') as file:
        lines = file.readlines()

    lines = [line.strip().split(" ") for line in lines if line]

    lines.sort(key=lambda x: int(x[0]))

    decoded_words = []
    step = 0
 
    i = 0
    for step in range(2, len(lines)):
      if i < len(lines):
          decoded_words.append(lines[i][1])
          i += step 
        
    print("decoded", decoded_words)

if __name__ == '__main__':
    decode("coding_qual_input.txt")
