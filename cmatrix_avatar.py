import random

class CMatrixAvatar(object):
    def __init__(self, cmatrix=None) -> None:
        self.cmatrix = cmatrix
        self.cmatrix_lenx = 0
        self.cmatrix_leny = 0
        if self.cmatrix != None:
            assert type(cmatrix) == type("Hello"), "Wrong type"
            cmatrix_lines = self.cmatrix.split("\n")
            for i in cmatrix_lines:
                self.cmatrix_leny += 1
                if len(i) > self.cmatrix_lenx:
                    self.cmatrix_lenx = len(i)
        self.p_black        = "\33[0;30m" # print black
        self.p_red          = "\33[0;31m" # print red
        self.p_green        = "\33[0;32m" # print green
        self.p_yellow       = "\33[0;33m" # print yellow
        self.p_blue         = "\33[0;34m" # print blue
        self.p_magenta      = "\33[0;35m" # print magenta
        self.p_cyan         = "\33[0;36m" # print cyan
        self.p_light_gary   = "\33[0;37m" # print light gary
        self.p_dark_gary    = "\33[0;90m" # print dark gary
        self.p_light_red    = "\33[0;91m" # print light red
        self.p_light_green  = "\33[0;92m" # print light green
        self.p_light_blue  = "\33[0;94m" # print light blue
        self.p_default      = "\33[0m"    # print default

    def set_background_string(self, string=None):
        if string == None:
            self.background_string = [ 
                "Never Lose a Holy Curiosity.",
                "What I cannot create, I do not understand.",
                "A person who never made a mistake never tried anything new.",
                "Not even wrong.",
                "For a successful technology, reality must take precedence over public relations, for nature cannot be fooled.",
                "Know how to solve every problem that has been solved.",
                "I would rather have questions that can't be answered than answers that can't be questioned.",
                "We are trying to prove ourselves wrong as quickly as possible, because only in that way can we find progress.",
                "Education is what remains after one has forgotten everything one has learned in school.",
                "The important thing is not to stop questioning. Curiosity has its own reason for existence. One cannot help but be in awe when he contemplates the mysteries of eternity, of life, of the marvelous structure of reality. It is enough if one tries merely to comprehend a little of this mystery each day.",
                "I owe a lot to my engineering training because it taught me to tolerateapproximations. Previously to that I thought one should just concentrate on exactequations all the time. Then I got the idea that in the actual world all our equations areonly approximate. We must just tend to greater and greater accuracy. In spite of theequations being approximate, they can be beautiful.",
            ]
        elif type(string) == type("Hello"):
            self.background_string = [string]
        elif type(string) == type([1,2,3]):
            for i in string:
                assert type(i) == type("Hello"), "Wrong type"
            self.background_string = string
        
        for i in range(len(self.background_string)):
            self.background_string[i] = self.background_string[i].replace(" ", "")
        self.background_string = "".join(self.background_string)
        tmp = ""
        for i in self.background_string:
            if random.randint(0,1) == 0:
                tmp += i.lower()
            else:
                tmp += i.upper()
        self.background_string = tmp

    def set_embed_string(self, string=None):
        if string == None:
            string = f"""
  __________      ____________ 
 /  _____/  \    /  \______   \\
/   \  __\   \/\/   /|    |  _/
\    \_\  \        / |    |   \\
 \______  /\__/\  /  |______  /
        \/      \/          \/ """

            """
            _____ _    _______ 
            |  __ \ |  | | ___ \
            | |  \/ |  | | |_/ /
            | | __| |/\| | ___ \
            | |_\ \  /\  / |_/ /
            \____/\/  \/\____/ 
            """
            string = string[1:]
        else:
            assert type(string) == type("Hello")
        
        string_lines = string.split("\n")
        string_lines = [list(i) for i in string_lines]
        len_x = 0
        len_y = 0
        for i in string_lines:
            len_x += 1
            if len(i) > len_y:
                len_y = len(i)
        for i in range(len(string_lines)):
            if len(string_lines[i]) < len_y:
                for j in range(len(string_lines[i]), len_y):
                    string_lines[i].append(" ")
        self.embed_string = string_lines
        self.embed_lenx = len_x
        self.embed_leny = len_y

    def gen_cmatrix(self, row_no, col_no):
        cmatrix_horizontal = []
        for i in range(col_no):
            cmatrix_horizontal.append([" "] * row_no)
            if i % 2 == 0:
                length = random.randint(0, row_no)
                first_position = random.randint(0, row_no)
                for j in range(length):
                    tmp = j / length
                    if tmp >= 0 and tmp < 0.2:
                        tmp = 22
                    elif tmp >= 0.2 and tmp < 0.4:
                        tmp = 28
                    elif tmp >= 0.4 and tmp < 0.6:
                        tmp = 34
                    elif tmp >= 0.6 and tmp < 0.8:
                        tmp = 40
                    elif tmp >= 0.8 and tmp < 1.0:
                        tmp = 46
                    cmatrix_horizontal[i][(first_position+j)%row_no] = "\033[38;5;%dm+"%(tmp,)

        cmatrix_vertical = []
        for i in range(row_no):
            cmatrix_vertical.append([" "] * col_no)
        for i in range(row_no):
            for j in range(col_no):
                cmatrix_vertical[i][j] = cmatrix_horizontal[j][i]
        # cmatrix_vertical = ["".join(i) for i in cmatrix_vertical]
        # self.cmatrix = "\n".join(cmatrix_vertical)
        self.cmatrix = cmatrix_vertical
        self.cmatrix_lenx = row_no
        self.cmatrix_leny = col_no

    def mark_latters(self, latters=None):
        if latters == None:
            char_set = ['G', 'g', 'W', 'w', 'B', 'b']
        elif type(latters) == type("Hello"):
            char_set = list(latters.lower)
            char_set += list(latters.upper)
        elif type(latters) == type([1,2,3]):
            char_set = latters.copy()
        char_set = set(char_set)
        char_set = list(char_set)

        for i in range(self.cmatrix_lenx):
            for j in range(self.cmatrix_leny):
                if self.cmatrix[i][j][-1] in char_set:
                    self.cmatrix[i][j] = self.p_yellow + self.cmatrix[i][j][-1] #+ self.p_light_green
        
    def substitute_colum(self, string, col):
        assert type(string) == type("Hello"), "Wrong type"
        cmatrix_lines = self.cmatrix.split("\n")
        cmatrix_lines = [list(i) for i in cmatrix_lines]
        string_len = len(string)
        string = list(string)

        if string_len <= len(cmatrix_lines):
            for i in range(string_len):
                if len(cmatrix_lines[i]) > col:
                    cmatrix_lines[i][col] = string[i]
                else:
                    for j in range(len(cmatrix_lines[i]), col):
                        cmatrix_lines[i].append(" ")
                    cmatrix_lines[i].append(string[i])
        else:
            for i in range(len(cmatrix_lines)):
                if len(cmatrix_lines[i]) > col:
                    cmatrix_lines[i][col] = string[i]
                else:
                    for j in range(len(cmatrix_lines[i]), col):
                        cmatrix_lines[i].append(" ")
                    cmatrix_lines[i].append(string[i])
            for i in range(len(cmatrix_lines), string_len):
                cmatrix_lines.append([])
                for j in range(0, col):
                    cmatrix_lines[i].append(" ")
                cmatrix_lines[i].append(string[i])
            
        cmatrix_lines = ["".join(i) for i in cmatrix_lines]
        self.cmatrix = "\n".join(cmatrix_lines)

    def substitute_all(self):
        says = self.background_string
        cmatrix_list = list(self.cmatrix)
        count_in_says = 0
        for i in range(len(cmatrix_list)):
            if not (cmatrix_list[i] in [" ", "\n"]):
                if count_in_says < len(says):
                    pass
                elif count_in_says >= len(says):
                    count_in_says = 0
                cmatrix_list[i] = says[count_in_says]
                count_in_says += 1
        random_numbers = [random.randint(0, 1) for _i in range(len(cmatrix_list))]
        cmatrix_list = [cmatrix_list[i].upper() if random_numbers[i] == 1 else cmatrix_list[i].lower() for i in range(len(cmatrix_list))]
        self.cmatrix = "".join(cmatrix_list)

    def substitute_all_with_embed(self):
        len_x = self.embed_lenx
        len_y = self.embed_leny
        embed_string_lines = self.embed_string
        if len_x <= self.cmatrix_lenx and len_y <= self.cmatrix_leny:
            start_x = self.cmatrix_lenx//2 - len_x//2
            start_y = self.cmatrix_leny//2 - len_y//2
            cmatrix_lines = self.cmatrix
            for i in range(len_x):
                for j in range(len_y):
                    cmatrix_lines[i+start_x][j+start_y] = self.p_light_blue + embed_string_lines[i][j]
            
            background_str_count = 0
            start_x = self.cmatrix_lenx//2 - len_x//2
            start_y = self.cmatrix_leny//2 - len_y//2
            for i in range(self.cmatrix_lenx):
                for j in range(self.cmatrix_leny):
                    if i >= start_x and i< start_x + len_x and j >= start_y and j < start_y + len_y:
                        pass
                    elif "+" in cmatrix_lines[i][j]:
                        if background_str_count >= len(self.background_string):
                            background_str_count = 0
                        # print(cmatrix_lines[i][j])
                        cmatrix_lines[i][j] = cmatrix_lines[i][j].replace("+", self.background_string[background_str_count])
                        background_str_count += 1
            
            self.cmatrix = cmatrix_lines
        else:
            assert False, "Wrong size"

    def centered_embed(self, string=None):
        len_x = 0
        len_y = 0
        string_lines = self.embed_string.split("\n")
        for i in string_lines:
            len_x += 1
            if len(i) > len_y:
                len_y = len(i)
        string_lines = [list(i) for i in string_lines]
        if len_x <= self.cmatrix_lenx and len_y <= self.cmatrix_leny:
            start_x = self.cmatrix_lenx//2 - len_x//2
            start_y = self.cmatrix_leny//2 - len_y//2
            cmatrix_lines = self.cmatrix.split("\n")
            cmatrix_lines = [list(i) for i in cmatrix_lines]
            for i in range(len_x):
                for j in range(len_y):
                    string_lines[i][j]
                    cmatrix_lines[i+start_x][j+start_y] = string_lines[i][j]
            
            cmatrix_lines = ["".join(i) for i in cmatrix_lines]
            self.cmatrix = "\n".join(cmatrix_lines)
        else:
            assert False, "Wrong size"

    def show(self):
        count = 0
        for i in range(self.cmatrix_lenx):
            for j in range(self.cmatrix_leny):
                if not (" " in self.cmatrix[i][j]):
                    count += 1
        print("Latter count:", count)
        print("\n")
        tmp = ["".join(i) for i in self.cmatrix]
        tmp = "\n".join(tmp)
        print(tmp + self.p_default)


if __name__ == "__main__":
    cmatrix = CMatrixAvatar()
    cmatrix.set_background_string()
    cmatrix.set_embed_string()
    cmatrix.gen_cmatrix(43//3*2, 86//3*2)
    cmatrix.show()
    # cmatrix.substitute_all()
    # cmatrix.centered_embed()
    cmatrix.substitute_all_with_embed()
    cmatrix.show()
    cmatrix.mark_latters()
    cmatrix.show()
    # print("\033[38;5;22mA \033[38;5;28mA \033[38;5;34mA \033[38;5;40mA \033[38;5;46mA \033[0m")
