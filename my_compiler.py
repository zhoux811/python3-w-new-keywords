import re, string, os

# f_path = '../PLCs/PLCh4q4.py'
f_path = 'quicksort_written_in_special_grammar.py'
f_path = 'two_sum_monte_carlo_maybe_special.py'


def how_many_ws_begin(ipt):
    ptr, counter = 0, 0
    while ipt[ptr] == ' ' or ipt[ptr] == '\t':
        if ipt[ptr] == ' ':
            counter += 1
            ptr += 1
        elif ipt[ptr] == '\t':
            counter += 4
            ptr += 1
    # print(ptr)
    return counter


f = open(f_path, 'r')

how_many_ws_begin_lines = [how_many_ws_begin(l2) for l2 in f]

# print(how_many_ws_begin_lines)
# print(lines)

lines = [l1 for l1 in f]
l_n = 0
for line in lines:
    print(str(l_n) + '--' + str(how_many_ws_begin(line)) + " :" + line, end='')
    l_n += 1


def parse_but(whole_paragraph_or_single_line_input):
    return re.sub(r'\sbut\s', r' and ', whole_paragraph_or_single_line_input, count=0, flags=re.IGNORECASE)


def parse_before(single_line_input):
    r = re.search(r'(^\s*before|^\s*until)', single_line_input, flags=re.IGNORECASE)
    # print(r)
    if r:
        single_line_input = re.sub(r'before', r'while', single_line_input, flags=re.IGNORECASE)  # only 1 iteration

        def logical_convert(match_obj):
            if match_obj.group(1) is not None:
                return '>'
            if match_obj.group(2) is not None:
                return '<'
            if match_obj.group(3) is not None:
                return '=='
            if match_obj.group(4) is not None:
                return '!='

        return re.sub(r'(<)|(>)|(!=)|(==)', logical_convert, single_line_input)
    return single_line_input


def if_this_line_inside_while_or_for(particular_line_n):
    def if_this_line_start_with_zero_or_more_whitespaces_then_while_or_for(local_scope_line):
        striped_line = local_scope_line.lstrip()
        if striped_line[:5] == 'while' or striped_line[:3] == 'for':
            # print('there is while or for')
            # print(local_scope_line)
            return striped_line

    ptr = particular_line_n
    if how_many_ws_begin_lines[ptr] == 0:
        # print(lines[ptr])
        return False
    else:
        while how_many_ws_begin_lines[ptr] != 0:
            # ptr should reach it now
            # print(lines[ptr])
            print(ptr)
            if if_this_line_start_with_zero_or_more_whitespaces_then_while_or_for(lines[ptr]):
                return True
            else:
                ptr -= 1
        return False


def parse_unless(single_line_input):
    r = re.search(r'(\s*unless)', single_line_input, flags=re.IGNORECASE)
    if r:
        keyword = r.group(0)

        return (how_many_ws_begin(single_line_input) * ' ') + 'if not' + single_line_input[7 + single_line_input.find(keyword):-1] + ':\n' \
               + '\t' + single_line_input[: single_line_input.find(keyword)] + '\n'
    else:
        return single_line_input


def parse_unless_inside_loop(single_line_input):
    r = re.search(r'(\s*unless)', single_line_input, flags=re.IGNORECASE)
    if r:
        keyword = r.group(0)

        return (how_many_ws_begin(single_line_input) * ' ') + 'if not' + single_line_input[7 + single_line_input.find(keyword):-1] + ':\n' \
               + '\t' + single_line_input[: single_line_input.find(keyword)] + '\n' \
               + (how_many_ws_begin(single_line_input) * ' ') + 'else:\n' \
               + (how_many_ws_begin(single_line_input) * ' ') + '\tbreak\n'
    else:
        return single_line_input


f.seek(0)
lines = [l1 for l1 in f]
l_n = 0
for line in lines:
    print(str(l_n) + '--' + str(how_many_ws_begin(line)) + " :" + line, end='')
    l_n += 1

f.seek(0)
l_n = 0
new_lines = []

for sl in f:
    print(l_n)
    if sl == None:
        print('none')
    else:
        if not if_this_line_inside_while_or_for(l_n):
            new_lines.append(parse_unless(parse_before(parse_but(sl))))
            # print((parse_before(parse_but(sl))))
        else:
            new_lines.append(parse_unless_inside_loop(parse_before(parse_but(sl))))
    l_n += 1

print(new_lines)
new_f = open(f_path + '_parsed.py', 'w')
for lll in new_lines:
    new_f.write(lll)
f.close()
new_f.close()
