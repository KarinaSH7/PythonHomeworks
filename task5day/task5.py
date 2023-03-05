# Дан словарь email-адресов студентов, в качестве ключа используется домен, а в качестве значения список имен.
# Необходимо вывести все email-адреса в формате Имя@домен.
# addr = map(lambda k: list(map(lambda name: name + '@' + k, emails[k])), emails)
#
# print('\n'.join(sorted(sum(addr, []))))

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
		  'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
		  'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
		  'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
		  'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
		  'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

addr = map(lambda k: list(map(lambda name: name + '@' + k, emails[k])), emails)

print('\n'.join(sum(addr, [])))
