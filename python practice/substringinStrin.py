
y= " Reads the string and display the longest substring"

length = len(y)

maxlength = 0
maxsub= ''
sub = ''
lensub = 0
for a in range(length):
    if y[a]  in 'aeiou' or y[a]  in 'AEIOU':
        if lensub>maxlength:
            maxsub=sub
            maxlength=lensub
            sub=''
            lensub= 0

        else:
            sub+= y[a]
            lensub=len(sub)
        a+=1
print("Maximum length consonant substring is:", maxsub, end= ' ')
print("with", maxlength, "characters")