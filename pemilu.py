print('-' * 25)
print('Pemilihan Umum !')
print('-' * 25)

umur = int(input('Masukan Umur : '))

if umur < 17:
  menikah = input('Menikah [Y/T] : ').upper()
  if menikah == 'Y':
    print('Anda Boleh Ikut Pemilu !')
  elif menikah == 'T':
    print('Anda Tidak Boleh Ikut Pemilu !')
else:
  print('Anda Boleh Ikut Pemilu !')