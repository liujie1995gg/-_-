def take_middle_text(txt,txt_s,txt_e):
    # 取出中间文本，真返回中间文本，假返回False
    s_1 = txt.find(txt_s)
    s_2 = txt.find(txt_e)
    if s_1 == -1 or s_2 == -1:
        return False
    l_1 = len(txt_s)
    return txt[s_1+l_1:s_2]
