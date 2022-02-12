from PIL import Image

# ABRIR IMAGENS
potato = Image.open('parts/potato.png')
hair   = Image.open('parts/hair/hair_goku_01.png')

# PRINT TAMANHO IMAGEM
print(potato.size)
print(hair.size)

# RESIZE IMAGEM
new_hair = hair.resize((900,900))
new_hair.save('output/new_hair.png')



potato.paste(new_hair, (-90, -90), mask=new_hair)
potato.save('output/potato_01.png')
potato.show()

