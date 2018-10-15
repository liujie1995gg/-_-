def take_middle_text(txt,txt_s,txt_e='',seeks=0,seeke=0):
    # 取出中间文本，真返回中间文本，假返回False
    # seeks有传参，会按照取前几位取值
    # seeke有传参，会按照取后几位取值
    try:
        if txt_e or seeks or seeke:
            pass
        else:
            raise 1
        s_1 = txt.find(txt_s)
        if s_1 == -1:
            raise 1
        l_1 = len(txt_s)
        if txt_e:
            s_2 = txt.find(txt_e)
            if s_1 == -1 or s_2 == -1:
                return False
            return txt[s_1+l_1:s_2]
        if seeks:
            return txt[s_1-seeks:s_1]
        if seeke:
            return txt[s_1+l_1:s_1+l_1+seeke]
    except:
        return '传参错误或未找到传参文本'
