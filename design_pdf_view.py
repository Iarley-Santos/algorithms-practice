def design_pdf_view(h, word):
    offset_a = ord('a')
    h_max = 0
    for char in word:
        ind = ord(char) - offset_a

        current_h = h[ind]

        #caso a altura da letra atual seja maior do que a maior altura das ultimas letras
        if current_h > h_max:
            h_max = current_h
    
    area = h_max * len(word)
    return area 

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = "afc"
result = design_pdf_view(h, word)
print(f"Para a palavra {word}, a area é {result}")
            
