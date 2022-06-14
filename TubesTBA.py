import string

# input
sentence = input("Ketik Kalimat : ")
input_string = sentence.lower() + '#'

# initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18',
              'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

# space before input string
transition_table['q0', ' '] = 'q0'

# update the transition table for the following token : nakke
transition_table[('q0', 'n')] = 'q1'
transition_table[('q1', 'a')] = 'q7'
transition_table[('q7', 'k')] = 'q16'
transition_table[('q16', 'k')] = 'q34'
transition_table[('q34', 'e')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# update the transition table for the following token : amma
transition_table[('q0', 'a')] = 'q4'
transition_table[('q4', 'm')] = 'q12'
transition_table[('q12', 'm')] = 'q36'
transition_table[('q36', 'a')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'
# update the transition table for the following token : katte
transition_table[('q0', 'k')] = 'q3'
transition_table[('q3', 'a')] = 'q9'
transition_table[('q9', 't')] = 'q18'
transition_table[('q18', 't')] = 'q34'
transition_table[('q34', 'e')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# update the transition table for the following token : je'ne
transition_table[('q0', 'j')] = 'q2'
transition_table[('q2', 'e')] = 'q8'
transition_table[('q8', "'")] = 'q17'
transition_table[('q17', 'n')] = 'q34'
transition_table[('q34', 'e')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# update the transition table for the following token : snggara
transition_table[('q0', 's')] = 'q6'
transition_table[('q6', 'n')] = 'q14'
transition_table[('q14', 'g')] = 'q21'
transition_table[('q21', 'g')] = 'q27'
transition_table[('q27', 'a')] = 'q32'
transition_table[('q32', 'r')] = 'q36'
transition_table[('q36', 'a')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# update the transition table for the following token : balla
transition_table[('q0', 'b')] = 'q5'
transition_table[('q5', 'a')] = 'q13'
transition_table[('q13', 'l')] = 'q26'
transition_table[('q26', 'l')] = 'q36'
transition_table[('q36', 'a')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'


# update the transition table for the following token : a'jappa
transition_table[('q0', 'a')] = 'q4'
transition_table[('q4', "'")] = 'q11'
transition_table[('q11', 'j')] = 'q20'
transition_table[('q20', 'a')] = 'q25'
transition_table[('q25', 'p')] = 'q29'
transition_table[('q29', 'p')] = 'q36'
transition_table[('q36', 'a')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# update the transition table for the following token : nangai
transition_table[('q0', 'n')] = 'q1'
transition_table[('q1', 'a')] = 'q7'
transition_table[('q7', 'n')] = 'q15'
transition_table[('q15', 'g')] = 'q22'
transition_table[('q22', 'a')] = 'q33'
transition_table[('q33', 'i')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# update the transition table for the following token : anginung
transition_table[('q0', 'a')] = 'q4'
transition_table[('q4', 'n')] = 'q10'
transition_table[('q10', 'g')] = 'q19'
transition_table[('q19', 'i')] = 'q24'
transition_table[('q24', 'n')] = 'q28'
transition_table[('q28', 'u')] = 'q31'
transition_table[('q31', 'n')] = 'q35'
transition_table[('q35', 'g')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# update the transition table for the following token : anganre
transition_table[('q0', 'a')] = 'q4'
transition_table[('q4', 'n')] = 'q10'
transition_table[('q10', 'g')] = 'q19'
transition_table[('q19', 'a')] = 'q23'
transition_table[('q23', 'n')] = 'q30'
transition_table[('q30', 'r')] = 'q34'
transition_table[('q34', 'e')] = 'q37'
transition_table[('q37', '#')] = 'accept'
transition_table[('q37', ' ')] = 'q38'
transition_table[('q38', '#')] = 'accept'

# transition for new token
transition_table[('q38', 'n')] = 'q1'
transition_table[('q38', 'j')] = 'q2'
transition_table[('q38', 'k')] = 'q3'
transition_table[('q38', 'a')] = 'q4'
transition_table[('q38', 'b')] = 'q5'
transition_table[('q38', 's')] = 'q6'

# lexical analysis
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept':
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    # if state == '37':
    print('current token: ', current_token, ', valid')
    #current_token = ''
    if state == 'error':
        print('error, token tidak valid')
        break
    idx_char = idx_char + 1

# conclusion
if state == 'accept':
    print('semua token di input: ', sentence, ', valid')
