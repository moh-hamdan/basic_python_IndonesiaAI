print('PROGRAM EVALUASI')
print('=================================================================================')

theory_scor = float(input('Masukan nilai ujian teori: '))
practice_score = float(input('Masukan nilai ujian praktek: '))

if theory_scor >= 70 and practice_score >= 70:
    print('\nSelamat, anda lulus!') 
elif theory_scor >= 70 and practice_score < 70:
    print('\nAnda harus mengulang ujian praktek.')
elif theory_scor < 70 and practice_score >= 70:
    print('\nAnda harus mengulang ujian teori.')
else:
    print('\nAnda harus mengulang ujian teori dan praktek.')